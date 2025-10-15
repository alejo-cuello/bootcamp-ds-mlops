import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 


# 1) Cargamos los datos
data = pd.read_csv("predictive_maintenance.csv", sep=',')

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
data_x = data.drop('Target', axis=1)
data_y = data['Target']

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3)

# Creamos 500 decision trees
rf = RandomForestClassifier(n_estimators = 500, random_state = 42)

rf.fit(x_train, y_train)

# Matriz de confusión
y_pred1=rf.predict(x_train)
              # Ajuste tamaño de letra (var global)
conf_mat1=pd.crosstab(index=y_train,    # filas = valor real
                     columns=y_pred1,   # columnas = valor predicho
                     rownames=['Actual'], 
                     colnames=['Pred'], 
                     normalize='index')

print(conf_mat1)

# 4) Guardar el modelo
filename = 'rf.pkl'
pickle.dump(rf, open(filename, 'wb')) # rf = nuestro modelo

# Lo cargamos para usarlo en otro momento. 
rf_loaded = pickle.load(open(filename, 'rb'))

# 5) Guardar el nombre de las columnas
# Guardamos las columnas x (sin Target)
with open('categories_ohe.pickle', 'wb') as handle:
    pickle.dump(data_x.columns, handle, protocol=pickle.HIGHEST_PROTOCOL)