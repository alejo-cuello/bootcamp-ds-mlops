import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score

import mlflow.sklearn
from mlflow.models.signature import infer_signature


mlflow.set_experiment(experiment_name="proyecto_bootcamp_ds6_clase_martes")

# 1) Cargamos los datos
data = pd.read_csv("TravelInsurancePrediction.csv", sep=',', index_col=0)

# 2) Preparación de la data
class_map = {'No':0, 'Yes':1}
columns_booleans = ['GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']

for name_column in columns_booleans:
    data[name_column] = data[name_column].map(class_map)

class_map = {'Government Sector':0, 'Private Sector/Self Employed':1}
data['Employment Type'] = data['Employment Type'].map(class_map)

data.rename(columns = {'Employment Type':'EmploymentType'}, inplace = True)

# 3) Clasificación
data_x = data.drop('TravelInsurance', axis=1).values
data_y = data['TravelInsurance'].values

mlflow.log_param("Tamaño dataset", data_x.shape)


test_size_value = 0.25
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=test_size_value)

mlflow.log_param("Porcentaje de test", test_size_value)

# Creamos 1000 decision trees
number_of_estimators = 5000
mlflow.log_param("Número de estimadores", number_of_estimators)
mlflow.log_param("Valor semilla", 99)
rf = RandomForestClassifier(n_estimators = number_of_estimators, random_state = 99)
rf.fit(x_train, y_train)

mlflow.log_param("Número de estimadores", number_of_estimators)

# atención, asume 0.5 como punto de corte
y_pred=rf.predict(x_train)
conf_mat1=pd.crosstab(index=y_train,    # filas = valor real
                     columns=y_pred,    # columnas = valor predicho
                     rownames=['Actual'],
                     colnames=['Pred'],
                     normalize='index')
print(conf_mat1)

model_accuracy = accuracy_score(y_train, y_pred)

model_auc = roc_auc_score(y_train, y_pred)

model_precision = precision_score(y_train, y_pred)

model_recall = recall_score(y_train, y_pred)

print("Accuracy del modelo: ", model_accuracy)
print("AUC ROC del modelo: ", model_auc)
print(f'Precisión del modelo: {model_precision}')
print(f'Recall del modelo: {model_recall}')


mlflow.log_metric("accuracy_tr", model_accuracy)
mlflow.log_metric("auc_roc_tr", model_auc)
mlflow.log_metric("precision_tr", model_precision)
mlflow.log_metric("recall_tr", model_recall)


# 4) Guardar el modelo
## Definir la firma
signature = infer_signature(x_train, rf.predict(x_train))

## Definir un ejemplo de input
columnas = data.columns[:-1]
X_train_df = pd.DataFrame(x_train, columns=columnas)
input_example = X_train_df.head(5)

## Guardar modelo con firma y ejemplo
mlflow.sklearn.log_model(
    sk_model=rf,
    name="rf_5000",
    signature=signature,
    input_example=input_example,
    registered_model_name='travel_insurance'

)
