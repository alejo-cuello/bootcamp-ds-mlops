import pandas as pd
import mlflow

logged_model = 'runs:/005a122d632b47bd9dfe06e2c26a95d0/random_forest_model'
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Input data
# Age = 34
# EmploymentType = 1
# GraduateOrNot = 1
# AnnualIncome = 500000
# FamilyMembers = 4
# ChronicDiseases = 1
# FrequentFlyer = 0
# EverTravelledAbroad = 0

# data = [[Age, EmploymentType, GraduateOrNot, AnnualIncome, FamilyMembers, ChronicDiseases, FrequentFlyer, EverTravelledAbroad]]

aux_data = {
    "Air_temperature": 298.9,
    "Process_temperature": 309.1,
    "Rotational_speed": 2861,
    "Torque": 4.6,
    "Tool_wear": 143,
    "Type_H": 1,
    "Type_L": 0,
    "Type_M": 0
}

response = loaded_model.predict(pd.DataFrame([aux_data]))
print(response)