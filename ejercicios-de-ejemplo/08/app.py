import gradio as gr
import pandas as pd
import pickle


# Definir parámetros
PARAMS_NAME = [
    "Type",
    "Air_temperature",
    "Process_temperature",
    "Rotational_speed",
    "Torque",
    "Tool_wear"
]

# Cargar el modelo
with open("model/rf.pkl", "rb") as f:
    model = pickle.load(f)

# Cargar el nombre de las columnas
COLUMNS_PATH = "model/categories_ohe.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)


def predict(*args):
    answer_dict = {}

    for i in range(len(PARAMS_NAME)):
        answer_dict[PARAMS_NAME[i]] = [args[i]]

    single_instance = pd.DataFrame.from_dict(answer_dict)
    
    # Reformat columns
    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
    
    prediction = model.predict(single_instance_ohe)

    response = format(prediction[0], '.2f')
    #print(response)
    return ("Falla" if response == "1.00" else "No Falla")


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Mantenimiento de Máquinas 🔧🚜
        """
    )

    with gr.Row():
        with gr.Column():

            gr.Markdown(
                """
                ## Predecir si una máquina va a fallar o no.
                """
            )
            
            Type = gr.Radio(
                label="Tipo de Herramienta",
                choices=["L", "H", "M"],
                value="H"
                )
            
            Air_temperature = gr.Slider(label="Temperatura del aire", minimum=295, maximum=304, step=1, randomize=True)

            Process_temperature = gr.Slider(label="Temperatura del proceso", minimum=306, maximum=312, step=2, randomize=True)

            Rotational_speed = gr.Dropdown(
                label="Velocidad de Rotación",
                choices=[1168.0, 1423.0, 1503.0, 1612.0, 2886.0],
                multiselect=False,
                value=1168.0,
                )
            
            Torque = gr.Dropdown(
                label="Torque",
                choices=[3.8, 33.2, 40.1, 46.8, 76.6],
                multiselect=False,
                value=3.8,
                )

            Tool_wear = gr.Slider(label="Desgaste", minimum=0, maximum=250, step=50, randomize=True)
            
        with gr.Column():

            gr.Markdown(
                """
                ## Predicción
                """
            )

            label = gr.Label(label="Score")
            predict_btn = gr.Button(value="Evaluar")
            predict_btn.click(
                predict,
                inputs=[
                   Type,
                   Air_temperature,
                   Process_temperature,
                   Rotational_speed,
                   Torque,
                   Tool_wear,
                ],
                outputs=[label],
                api_name="prediccion"
            )
    gr.Markdown(
        """
        <p style='text-align: center'>
            <a href='https://www.escueladedatosvivos.ai/cursos/bootcamp-de-data-science' 
                target='_blank'>Proyecto demo creado en el bootcamp de EDVAI 🤗
            </a>
        </p>
        """
    )

demo.launch(share = True)
