import pandas as pd
import mlflow

# Reemplazar por tu RUN ID
# logged_model = 'runs:/< TU RUN ID>/< NOMBRE DE TU MODELO>'
logged_model = 'runs:/7f2fbef44f5a4b1e9d47a46108d30140/primer_run_rf'

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
