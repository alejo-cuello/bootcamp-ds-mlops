import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Cargar dataset
data = pd.read_csv("TravelInsurancePrediction.csv", sep=',', index_col=0)

# Preparar y acondicionar las columnas
class_map = {'No':0, 'Yes':1}
columns_booleans = ['GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']

for name_column in columns_booleans:
    data[name_column] = data[name_column].map(class_map)

class_map = {'Government Sector':0, 'Private Sector/Self Employed':1}
data['Employment Type'] = data['Employment Type'].map(class_map)

data.rename(columns = {'Employment Type':'EmploymentType'}, inplace = True)

data_x = data.drop('TravelInsurance', axis=1)
data_y = data['TravelInsurance']

# Separar data para entrenamiento / testing
x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3)

# Creamos 1000 decision trees
rf = RandomForestClassifier(n_estimators = 1000, random_state = 99)

rf.fit(x_train, y_train)

# Visualizar matrix de confusión
y_pred1=rf.predict(x_train)

conf_mat1=pd.crosstab(index=y_train,    # filas = valor real
                     columns=y_pred1,   # columnas = valor predicho
                     rownames=['Actual'],
                     colnames=['Pred'],
                     normalize='index')

print(conf_mat1)

# Guardar en el disco
filename = 'rf.pkl'
pickle.dump(rf, open(filename, 'wb')) # rf = nuestro modelo