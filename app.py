import streamlit as st
from src.trip_planner.crew import TripPlanner
from datetime import datetime, timedelta
from utils.pdf import md_a_pdf

# Configuración de la página
st.set_page_config(
    page_title="Trip Planner AI",
    layout="centered"
)

# Estilos personalizados
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        
        .hero-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 60px 70px;
            text-align: center;
            margin: -1rem -1rem 2rem -1rem;
        }
        
        .hero-banner h1 {
            color: white;
            font-size: 3em;
            font-weight: 800;
            margin-bottom: 10px;
            letter-spacing: -1px;
        }
        
        .hero-banner p {
            color: rgba(255,255,255,0.85);
            font-size: 1.1em;
            font-weight: 300;
        }

        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: 600;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown("""
    <div class='hero-banner'>
        <h1>Trip Planner Agents</h1>
        <p><b>Dinos a dónde quieres ir y nuestros agentes planean todo por ti</b></p>
    </div>
""", unsafe_allow_html=True)

# Formulario
col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("¿Dónde estás?", placeholder="Ciudad de México")
    interest = st.text_input("¿Cuáles son tus intereses?")

with col2:
    cities = st.text_input("¿Qué ciudades te interesan?")
    start_date = st.date_input("Fecha de inicio")

days = st.slider("Duración del viaje (días)", min_value=1, max_value=30, value=7)

st.divider()

if st.button("Planear mi viaje"):
    if not origin or not cities or not interest:
        st.warning("Por favor completa todos los campos antes de continuar.")
    else:
        with st.spinner("Los agentes están planificando tu viaje..."):
            end = start_date + timedelta(days=int(days))
            inputs = {
                'origin': origin,
                'cities': cities,
                'interest': interest,
                'dates': f"{start_date} a {end}"
            }
            try:
                result = TripPlanner().crew().kickoff(inputs=inputs)

                st.success("¡Tu itinerario está listo!")
                st.markdown("## Tu Itinerario")
                st.markdown(str(result))
                st.divider()

                pdf_bytes = md_a_pdf(str(result))
                st.download_button(
                    label="Descargar itinerario en PDF",
                    data=pdf_bytes,
                    file_name="itinerario.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Ocurrió un error: {str(e)}")
                st.info("Intenta de nuevo en unos segundos.")