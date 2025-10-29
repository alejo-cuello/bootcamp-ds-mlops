# 0) Dataset 🔧🚜

Nos basamos en el dataset de Kaggle: [Machine Predictive Maintenance Classification](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification).

Fue el utilizado para entrenar el modelo de la semana 7: Gradio.
<br>Así que usen el notebook `machine_maintenance.ipynb`

# 1) Consideraciones para MLFlow

- Llamen a su experimento `proyecto_bootcamp_jueves`.
- Parámetros a guardar: 
  <br>Tamaño dataset del dataset: `data.shape`
  <br>Porcentaje que se utiliza del dataset para el test: `test_size`
  <br>Número de estimadores del Random Forest
  <br>Random_state del Random Forest
- Métricas a guardar:
  <br>Accuracy en train: `accuracy_train`
  <br>Accuracy en test: `accuracy_test`
- Guarden su modelo en MLFlow con el nombre `mi_modelo`

# 2) Para call model

- Realicen el llamado al modelo `by_request` y `by_run`.
- Consideren como input
    ```
    # Input data
    Air_temperature	= 298.9
    Process_temperature	= 309.1
    Rotational_speed = 2861
    Torque = 4.6
    Tool_wear = 143
    Type_H = 1 
    Type_L = 0 
    Type_M = 0

    # Reformat data
    aux_data = [[Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Type_H, Type_L, Type_M]]
    ```

- Para call_model_by_run_id.py, añadir está línea de código adicional:
  ```
  # Construye el DataFrame con dtype=object (coincide con la firma que grabaste)
  ## Lo hacemos porque tenemos una mezcla de tipo de datos por el One Hot Encoding
  ## Este paso solo es para el call_model_by_run_id
  data = pd.DataFrame(aux_data, dtype=object)

  # Predict on a Pandas DataFrame.
  response = loaded_model.predict(pd.DataFrame(data))
  print(response)
  ```

- Para call_model_by_request:
  ```
  request_data = {
      "dataframe_records": aux_data
  }

  response = requests.post(url,json=request_data, timeout=10)
  print (response.json())
  ```