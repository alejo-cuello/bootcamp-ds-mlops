import mlflow.sklearn
import pandas as pd

from mlflow.models.signature import infer_signature
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split

# Parámetros a probar
test_size = 0.3
n_estimators = 500
random_state_rf = 42

# Setear experimento ML Flow
mlflow.set_experiment(experiment_name="proyecto_bootcamp_jueves")

# 1) Cargamos los datos
data = pd.read_csv("ejercicios-de-ejemplo/06/predictive_maintenance.csv", sep=',')

# 2) Preparación de la data
data = data.drop(['UDI', 'Product ID', 'Failure Type'], axis=1)

data.rename(
    columns = {
        'Air temperature [K]':'Air_temperature',
        'Process temperature [K]':'Process_temperature',
        'Rotational speed [rpm]':'Rotational_speed',
        'Torque [Nm]':'Torque',
        'Tool wear [min]':'Tool_wear',
        }, 
    inplace = True)

data = pd.get_dummies(data)


# 3) Clasificación
data_x = data.drop('Target', axis=1).values
data_y = data['Target'].values

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=test_size)

# Creamos el modelo y lo entrenamos
rf = RandomForestClassifier(n_estimators = n_estimators, random_state = random_state_rf)
rf.fit(x_train, y_train)

# Matriz de confusión
y_train_pred = rf.predict(x_train)
y_test_pred = rf.predict(x_test)

# Métricas
accuracy_tr = accuracy_score(y_train, y_train_pred)
accuracy_test = accuracy_score(y_test, y_test_pred)

# Guardar parámetros solicitados
mlflow.log_param("Tamaño dataset", data_x.shape)
mlflow.log_param("Porcentaje test", test_size)
mlflow.log_param("Número de estimadores", n_estimators)
# Guardar métricas solicitadas
mlflow.log_metric("Random state rf", random_state_rf)
mlflow.log_metric("Accuracy train", accuracy_tr)
mlflow.log_metric("Accuracy test", accuracy_test)

# 4) Guardar el modelo
filename = 'rf.pkl'

signature = infer_signature(x_train, rf.predict(x_train))

columns = data.columns[:-1]
x_train_df = pd.DataFrame(x_train, columns=columns)
input_example = x_train_df.head(5)

mlflow.sklearn.log_model(
    sk_model=rf,
    name="random_forest_model",
    signature=signature,
    input_example=input_example
    # registered_model_name='predictive_maintenance_rf_model'
)