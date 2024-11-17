import streamlit as st
from moodle_generator.xml_generator import MoodleXMLFile, MoodleXMLMultipleChoiceQuestion
from moodle_generator.models import calculate_half_wave, calculate_full_wave
import random

def sanitize_cdata_content(content):
    return content.replace("]]>", "]] >")

def generate_datos(V_EF_SEC, RL, FR):
    f = 50
    datos = f"V(EF_SEC)={V_EF_SEC}Vef<br>f={f}Hz<br>RL={RL}Ω<br>FR={FR}%"
    return sanitize_cdata_content(datos)

def main():
    st.title("Generador de preguntas Moodle")
    st.sidebar.header("Parámetros")

    category_name = st.sidebar.text_input("Nombre de la categoría", value="Preguntas personalizadas")
    num_questions = st.sidebar.number_input("Número de preguntas", min_value=1, max_value=50, value=5)

    st.sidebar.subheader("Valores base de DATOS")
    V_EF_SEC = st.sidebar.number_input("V(EF_SEC) (Voltaje base)", min_value=1, max_value=100, value=50)
    RL = st.sidebar.number_input("RL (Resistencia base)", min_value=1, max_value=1000000, value=1000, step=100)
    FR = st.sidebar.selectbox("FR (Base FR %)", [5, 10, 15], index=1)

    model = st.sidebar.selectbox("Selecciona el modelo matemático", ["Rectificador de media onda", "Rectificador de onda completa"])

    if st.sidebar.button("Generar preguntas"):
        questions = []
        for i in range(num_questions):
            datos = generate_datos(V_EF_SEC, RL, FR)

            if model == "Rectificador de media onda":
                correct_answer, distractors = calculate_half_wave(V_EF_SEC, RL, FR)
            elif model == "Rectificador de onda completa":
                correct_answer, distractors = calculate_full_wave(V_EF_SEC, RL)

            answers = [
                (f"{correct_answer} V", 100),
                (f"{distractors[0]} V", 0),
                (f"{distractors[1]} V", 0),
            ]

            question_text = f"""
                CALCULAR LA SIGUIENTE FUENTE DE ½ ONDA:<br>
                {datos}
            """
            questions.append(MoodleXMLMultipleChoiceQuestion(f"Pregunta {i+1}", question_text, answers))

        xml_file = MoodleXMLFile()
        xml_file.addCategory(category_name, questions)
        xml_content = xml_file.toXMLDocument().toprettyxml(indent="    ", encoding="utf-8")

        st.text_area("XML generado", xml_content, height=300)
        st.download_button("Descargar archivo XML", xml_content, file_name="preguntas_moodle.xml", mime="application/xml")
