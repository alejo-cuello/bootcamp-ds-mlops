import pandas as pd
import mlflow

logged_model = 'runs:/deb28e98e6944d469e7a9b762c92df9f/random_forest_model'
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Input data
Age = 34
EmploymentType = 1
GraduateOrNot = 1
AnnualIncome = 500000
FamilyMembers = 4
ChronicDiseases = 1
FrequentFlyer = 0
EverTravelledAbroad = 0

aux_data = [[Age, EmploymentType, GraduateOrNot, AnnualIncome, FamilyMembers, ChronicDiseases, FrequentFlyer, EverTravelledAbroad]]

# aux_data = {
#     "Air_temperature": 298.9,
#     "Process_temperature": 309.1,
#     "Rotational_speed": 2861,
#     "Torque": 4.6,
#     "Tool_wear": 143,
#     "Type_H": 1,
#     "Type_L": 0,
#     "Type_M": 0
# }

df = pd.DataFrame(aux_data)
df = df.astype(object) 

response = loaded_model.predict(df)
print(response)