import streamlit as st
from src.trip_planner.crew import TripPlanner
from datetime import datetime, timedelta
from fpdf import FPDF

def md_a_pdf(texto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    # Reemplazar caracteres especiales
    texto_limpio = texto.replace('–', '-').replace('—', '-').replace('"', '"').replace('"', '"').replace(''', "'").replace(''', "'")
    pdf.multi_cell(0, 10, texto_limpio)
    return bytes(pdf.output())

st.title('Trip planner')

origin = st.text_input("¿Dónde estás?")
cities = st.text_input("¿Qué ciudades te interesan?")
interest = st.text_input("¿Cuáles son tus intereses?")
start_date = st.date_input("Fecha de inicio")
days = st.number_input("Días de viaje", min_value=1, max_value=30, value=7)

if st.button("Planear viaje"):
    with st.spinner('Agentes trabajando...'):
        end = start_date + timedelta(days=int(days))
        inputs = {
            'origin' : origin,
            'cities' : cities,
            'interest' : interest,
            'dates' : f"{start_date} a {end}"
        }
        result = TripPlanner().crew().kickoff(inputs = inputs)
    
    if result:
        st.markdown('Itinerario')

        pdf_bytes = md_a_pdf(str(result))
        st.download_button(
            label = 'Descargar itinerario',
            data = pdf_bytes,
            file_name= 'itinerario.pdf',
            mime = 'application/pdf'
        )
