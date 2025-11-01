import pandas as pd
import mlflow

# Reemplazar por tu RUN ID
# logged_model = 'runs:/< TU RUN ID>/< NOMBRE DE TU MODELO>'
logged_model = 'runs:/8880e8c5523a45bf89890a74a3c15d30/rf_5000'

# Load model as a PyFuncModel.
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

data = [[Age, EmploymentType, GraduateOrNot, AnnualIncome, FamilyMembers, ChronicDiseases, FrequentFlyer, EverTravelledAbroad]]

# Predict on a Pandas DataFrame.
response = loaded_model.predict(pd.DataFrame(data))
print(response)
