import gradio as gr
import json
import pandas as pd
import pickle
# from pydantic import BaseModel

PARAM_NAMES = {
    "Age",
    "Class",
    "Wifi",
    "Booking",
    "Seat",
    "Checkin"   
}

# class Answer(BaseModel): 
#     Age:int
#     Class:int
#     Wifi:int
#     Booking:int
#     Seat:int
#     Checkin:int

with open("08-hugging-face-y-gradio/model/rf.pkl", "rb") as handle:
    model = pickle.load(handle)

with open("08-hugging-face-y-gradio/model/categories_ohe.pkl", "rb") as handle:
    columns_ohe = pickle.load(handle)

with open("08-hugging-face-y-gradio/model/min_max_input_values.json", "r") as handle:
    min_max_input_values = json.load(handle)

# Tienen que adaptar los datos de input respecto a los datos que recibe el modelo. Entonces tienen que agregarle / reformatear el nombre de las columnas.
# single_instance = pd.DataFrame.from_dict(answer_dict)
# # Reformat columns
# single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = columns_ohe).fillna(0)
# prediction = model.predict(single_instance_ohe)
    
def predict(*args):
    return "Mock"

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Satisfacción aerolínea
        """
    )
    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                ### ¿Cliente satisfecho?
                """
            )
            
            Age = gr.Slider(
                label="Edad",
                minimum=min_max_input_values["Age"]["Min"],
                maximum=min_max_input_values["Age"]["Max"],
                value=min_max_input_values["Age"]["Min"],
                step=1)
            Class = gr.Radio(
                label="Clase",
                choices=["Business","Eco","Eco Plus"],
                value="Business")
            Wifi = gr.Slider(
                label="Servicio de Wifi",
                minimum=min_max_input_values["Wifi"]["Min"],
                maximum=min_max_input_values["Wifi"]["Max"],
                value=min_max_input_values["Wifi"]["Min"],
                step=1)
            Booking = gr.Slider(
                label="Facilidad de registro",
                minimum=min_max_input_values["Booking"]["Min"],
                maximum=min_max_input_values["Booking"]["Max"],
                value=min_max_input_values["Booking"]["Min"],
                step=1)
            Seat = gr.Dropdown(
                label="Comodidad del asiento",
                choices=range(min_max_input_values["Seat"]["Min"],min_max_input_values["Seat"]["Max"]+1),
                value=min_max_input_values["Seat"]["Min"],
                multiselect=False)
            Checkin = gr.Dropdown(
                label="Experiencia con el checkin",
                choices=range(min_max_input_values["Checkin"]["Min"],min_max_input_values["Checkin"]["Max"]+1),
                value=min_max_input_values["Checkin"]["Min"],
                multiselect=False)
            
        with gr.Column():
            gr.Markdown(
                """
                ### Predicción
                """
            )
            
            label = gr.Label(label="Score")
            prediction_btn = gr.Button(value="Evaluar")
            prediction_btn.click(
                predict,
                inputs=[Age,Class,Wifi,Booking,Seat,Checkin],
                outputs=label,
                api_name="predict"
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
            
demo.launch()