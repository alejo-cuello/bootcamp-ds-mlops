import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow.sklearn
from mlflow.models.signature import infer_signature


if __name__ == "__main__":
    mlflow.set_experiment(experiment_name="EDVai_MLFlow_clase11_tarea")

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

    mlflow.log_param("Tamaño dataset", data.shape)

    # 3) Clasificación (para MLFlow al igual que para HuggingFace, va en formato array de numpy, no dataframe)
    data_x = data.drop('Target', axis=1).values
    data_y = data['Target'].values

    TEST_SIZE = 0.3

    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=TEST_SIZE)

    mlflow.log_param("Tamaño de Test", TEST_SIZE)

    # Creamos 500 decision trees
    N_ESTIMATORS = 500
    RANDOM_STATE = 42
    rf = RandomForestClassifier(n_estimators = N_ESTIMATORS, random_state = RANDOM_STATE)

    mlflow.log_param("Cantidad estimators", N_ESTIMATORS)
    mlflow.log_param("Random State", RANDOM_STATE)

    rf.fit(x_train, y_train)

    # Matriz de confusión
    y_pred_tr=rf.predict(x_train)
    y_pred_ts=rf.predict(x_test)


                # Ajuste tamaño de letra (var global)
    conf_mat1=pd.crosstab(index=y_train,    # filas = valor real
                        columns=y_pred_tr,   # columnas = valor predicho
                        rownames=['Actual'], 
                        colnames=['Pred'], 
                        normalize='index')

    print(conf_mat1)

    # Accuracy
    model_accuracy_train = accuracy_score(y_train, y_pred_tr)
    model_accuracy_test = accuracy_score(y_test, y_pred_ts)

    mlflow.log_metric("Accuracy Train", model_accuracy_train)
    mlflow.log_metric("Accuracy Test", model_accuracy_test)

    # 4) Guardar el modelo
    ## Definir la firma
    signature = infer_signature(x_train, rf.predict(x_train))

    ## Definir un ejemplo de input
    columnas = data.columns[:-1] # todas menos la última que es el target, no uso data_x porque es un array numpy sin nombre de columnas
    X_train_df = pd.DataFrame(x_train, columns=columnas)
    input_example = X_train_df.head(5)

    ## Guardar modelo con firma y ejemplo
    mlflow.sklearn.log_model(
        sk_model=rf,
        name="mi_modelo",
        signature=signature,
        input_example=input_example
    )

    # 5) Guardar el nombre de las columnas
    # Guardamos las columnas x (sin Target)
    with open('categories_ohe.pickle', 'wb') as handle:
        pickle.dump(data.columns[:-1], handle, protocol=pickle.HIGHEST_PROTOCOL)