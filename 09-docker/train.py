import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 


# 1) Cargamos los datos
data = pd.read_csv("water_potability.csv", sep=',')

# 2) Preparación de data
data['ph'], saved_bins_ph = pd.qcut(data['ph'], q=10, duplicates='drop', retbins=True)
data['Sulfate'], saved_bins_sulfate = pd.qcut(data['Sulfate'], q=10, duplicates='drop', retbins=True)
data['Trihalomethanes'], saved_bins_trihalomethanes = pd.qcut(data['Trihalomethanes'], q=10, duplicates='drop', retbins=True)

data['ph']=data['ph'].cat.add_categories("desconocido")
data['ph']=data['ph'].fillna(value="desconocido")

data['Sulfate']=data['Sulfate'].cat.add_categories("desconocido")
data['Sulfate']=data['Sulfate'].fillna(value="desconocido")

data['Trihalomethanes']=data['Trihalomethanes'].cat.add_categories("desconocido")
data['Trihalomethanes']=data['Trihalomethanes'].fillna(value="desconocido")

data = pd.get_dummies(data) 

# 3) Clasificación
data_x = data.drop('Potability', axis=1)
data_y = data['Potability']

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3)

# Creamos 1000 decision trees
rf = RandomForestClassifier(n_estimators = 1000, random_state = 99)

rf.fit(x_train, y_train)

# 4) Matriz de Confusión
y_pred1=rf.predict(x_train)

conf_mat1 = pd.crosstab(index=y_train,    # filas = valor real
                        columns=y_pred1,   # columnas = valor predicho
                        rownames=['Actual'],
                        colnames=['Pred'],
                        normalize='index'
                        )

print(conf_mat1)

# 5) Guardar el modelo
filename = 'rf.pkl'
pickle.dump(rf, open(filename, 'wb')) # rf = nuestro modelo

# 6) Guardar los bins
with open('saved_bins_ph.pickle', 'wb') as handle:
    pickle.dump(saved_bins_ph, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('saved_bins_sulfate.pickle', 'wb') as handle:
    pickle.dump(saved_bins_sulfate, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('saved_bins_trihalomethanes.pickle', 'wb') as handle:
    pickle.dump(saved_bins_trihalomethanes, handle, protocol=pickle.HIGHEST_PROTOCOL)

# 7) Guardar el One Hot Encoding
with open('categories_ohe.pickle', 'wb') as handle:
    pickle.dump(data_x.columns, handle, protocol=pickle.HIGHEST_PROTOCOL)
