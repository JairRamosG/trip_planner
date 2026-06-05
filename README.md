# Trip Planner AI

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-191919?style=for-the-badge&logo=anthropic&logoColor=white)
![Serper](https://img.shields.io/badge/Serper-Google%20Search-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-white?style=for-the-badge&logo=ollama&logoColor=black)

Sistema multi-agente de planificación de viajes construido con **CrewAI** que genera itinerarios personalizados basados en tus intereses, fechas y ciudades de preferencia. Incluye interfaz web con Streamlit y exportación a PDF.

---

## Agentes

El sistema cuenta con tres agentes especializados que trabajan en secuencia:

| Agente | Rol | Herramientas |
|--------|-----|--------------|
| **City Selection Expert** | Analiza y selecciona la mejor ciudad según clima, costos y eventos | Serper Search |
| **Local Tour Guide** | Compila una guía detallada de la ciudad seleccionada | Serper Search |
| **Expert Travel Agent** | Genera el itinerario completo de 7 días | Serper Search |

---

## Flujo de trabajo

```
Usuario ingresa datos en la interfaz web
        ↓
City Selection Expert → Selecciona la mejor ciudad
        ↓
Local Tour Guide → Investiga atracciones y cultura local
        ↓
Expert Travel Agent → Genera itinerario completo
        ↓
Resultado mostrado en pantalla + descarga en PDF
```

---

## Requisitos previos

- Python 3.11+
- Cuenta en [Anthropic](https://console.anthropic.com) (Claude API)
- Cuenta en [Serper](https://serper.dev) (Google Search API)

---

## Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/trip_planner.git
cd trip_planner
```

**2. Instala las dependencias con uv:**
```bash
pip install crewai
uv sync
```

**3. Configura las variables de entorno:**
```bash
cp .env.example .env
```

Edita el `.env` con tus keys:
```dotenv
MODEL=anthropic/claude-haiku-4-5-20251001
ANTHROPIC_API_KEY=tu-api-key-aqui
SERPER_API_KEY=tu-serper-key-aqui
```

**4. Crea la carpeta de reportes:**
```bash
mkdir reportes
```

---

## Uso

**Interfaz web (recomendado):**
```bash
.venv/bin/streamlit run app.py
```

**Terminal:**
```bash
crewai run
```

El sistema te pedirá:

```
¿Dónde estás?
> CDMX

¿Qué ciudades te interesan?
> Puerto Vallarta, Cancún

¿Cuáles son tus intereses?
> hiking, música en vivo, gastronomía

Fecha de inicio
> 2026-07-01

Duración del viaje (días)
> 3
```

---

## Estructura del proyecto

```
trip_planner/
├── src/
│   └── trip_planner/
│       ├── config/
│       │   ├── agents.yaml       # Definición de agentes
│       │   └── tasks.yaml        # Definición de tareas
│       ├── crew.py               # Orquestación del crew
│       └── main.py               # Punto de entrada CLI
├── utils/
│   └── pdf.py                    # Generación de PDF
├── reportes/
│   ├── local_guide_report.md     # Guía de la ciudad
│   └── itinerary.md              # Itinerario completo
├── app.py                        # Interfaz web Streamlit
├── .env                          # Variables de entorno (no compartir)
├── .env.example                  # Plantilla de variables
├── pyproject.toml                # Configuración del proyecto
└── README.md
```

---

## Salidas del sistema

- **Interfaz web** — Itinerario mostrado en pantalla con formato
- **Descarga PDF** — Reporte descargable con diseño profesional
- **`reportes/local_guide_report.md`** — Guía detallada de la ciudad
- **`reportes/itinerary.md`** — Itinerario completo en markdown

---

## Variables de entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `MODEL` | Modelo LLM a usar | SI |
| `ANTHROPIC_API_KEY` | API Key de Anthropic (Claude) | SI |
| `SERPER_API_KEY` | API Key de Serper (Google Search) | SI |
| `CREWAI_TRACING_ENABLED` | Habilitar trazabilidad en CrewAI | NO |

---

## Modelos compatibles

El sistema es compatible con cualquier LLM. Cambia el `MODEL` en tu `.env`:

```dotenv
# Anthropic (recomendado)
MODEL=anthropic/claude-haiku-4-5-20251001

# Groq (gratuito)
MODEL=groq/llama-3.1-8b-instant

# Local con Ollama (requiere GPU para buena velocidad)
MODEL=ollama/llama3.1:8b
```

---

## Despliegue en Streamlit Cloud

1. Sube el proyecto a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Apunta al archivo `app.py`
5. En **Settings → Secrets** agrega:

```toml
MODEL = "anthropic/claude-haiku-4-5-20251001"
ANTHROPIC_API_KEY = "tu-api-key"
SERPER_API_KEY = "tu-serper-key"
```