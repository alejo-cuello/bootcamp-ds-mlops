import gradio as gr
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

#TODO: Descomentar cuando estén desarrollados
# with open("./model/rf.pkl", "wb") as handle:
#     model = pickle.load(handle)

# with open("./model/columns.pkl", "wb") as handle:
#     columns_ohe = pickle.load(handle)

# Tienen que adaptar los datos de input respecto a los datos que recibe el modelo. Entonces tienen que agregarle / reformatear el nombre de las columnas.
#     single_instance = pd.DataFrame.from_dict(answer_dict)
#     # Reformat columns
#     single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
#     prediction = model.predict(single_instance_ohe)

    
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
            
            #TODO: Revisar mínimos y máximos
            Age = gr.Slider(label="Edad",minimum = 0,maximum=100,value=50,step=1)
            Class = gr.Radio(label="Clase",choices=["Business","Eco","Eco Plus"],value="Business")
            Wifi = gr.Slider(label="Servicio de Wifi",minimum = 0,maximum=5,value=3,step=1)
            Booking = gr.Slider(label="Facilidad de registro",minimum = 0,maximum=5,value=3,step=1)
            Seat = gr.Dropdown(label="Comodidad del asiento",choices=[1,2,3,4,5],value=3,multiselect=False)
            Checkin = gr.Dropdown(label="Experiencia con el checkin",choices=[1,2,3,4,5],value=3,multiselect=False)
            
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