import gradio as gr
import json
import pandas as pd
import pickle

PARAM_NAMES = {
    "Age",
    "Class",
    "Wifi",
    "Booking",
    "Seat",
    "Checkin"   
}

with open("08-hugging-face-y-gradio/model/rf.pkl", "rb") as handle:
    model = pickle.load(handle)

with open("08-hugging-face-y-gradio/model/categories_ohe.pkl", "rb") as handle:
    columns_ohe = pickle.load(handle)

with open("08-hugging-face-y-gradio/model/min_max_input_values.json", "r") as handle:
    min_max_input_values = json.load(handle)
    
def predict(*args):
    keys = ["Age", "Class", "Wifi", "Booking", "Seat", "Checkin"]
    data_dict = dict(zip(keys, args))

    single_instance = pd.DataFrame([data_dict])
    single_instance_ohe = pd.get_dummies(single_instance,dtype="int64").reindex(columns=columns_ohe,fill_value=0)

    prediction = model.predict(single_instance_ohe)

    return ("Satisfecho" if prediction == 1 else "No Satisfecho")

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