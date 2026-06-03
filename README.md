# Trip Planner AI

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-191919?style=for-the-badge&logo=anthropic&logoColor=white)
![Serper](https://img.shields.io/badge/Serper-Google%20Search-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-white?style=for-the-badge&logo=ollama&logoColor=black)

Sistema multi-agente de planificación de viajes construido con **CrewAI** que genera itinerarios personalizados basados en tus intereses, fechas y ciudades de preferencia.

---

## Agentes

El sistema cuenta con tres agentes especializados que trabajan en secuencia:

| Agente | Rol | Herramientas |
|--------|-----|--------------|
| **City Selection Expert** | Analiza y selecciona la mejor ciudad según clima, costos y eventos | Serper Search |
| **Local Tour Guide** | Compila una guía detallada de la ciudad seleccionada | Serper Search, Web Scraping |
| **Expert Travel Agent** | Genera el itinerario completo de 7 días | Serper Search |

---

## Flujo de trabajo

```
Usuario ingresa datos
        ↓
City Selection Expert → Selecciona la mejor ciudad
        ↓
Local Tour Guide → Investiga atracciones y cultura local
        ↓
Expert Travel Agent → Genera itinerario completo
        ↓
Reportes generados en /reportes/
```

---

## Requisitos previos

- Python 3.11+
- Conda o entorno virtual
- Cuenta en [Anthropic](https://console.anthropic.com) (Claude API)
- Cuenta en [Serper](https://serper.dev) (Google Search API)

---

## Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/trip_planner.git
cd trip_planner
```

**2. Crea y activa el entorno:**
```bash
conda create -n trip_planner python=3.11
conda activate trip_planner
```

**3. Instala CrewAI:**
```bash
pip install crewai crewai-tools
```

**4. Configura las variables de entorno:**
```bash
cp .env.example .env
```

Edita el `.env` con tus keys:
```dotenv
MODEL=anthropic/claude-haiku-4-5-20251001
ANTHROPIC_API_KEY=tu-api-key-aqui
SERPER_API_KEY=tu-serper-key-aqui
```

**5. Crea la carpeta de reportes:**
```bash
mkdir reportes
```

---

## Uso

```bash
crewai run
```

El sistema te pedirá:

```
Where are you located?
> CDMX

What are the cities options you are interested in visiting?
> Puerto Vallarta, Cancún

What are some of your high level interests and hobbies?
> hiking, live music, swimming

What is the starting date? (YYYY-MM-DD)
> 2026-07-01

How long is the trip in days?
> 7
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
│       └── main.py               # Punto de entrada
├── reportes/
│   ├── local_guide_report.md     # Guía de la ciudad
│   └── itinerary.md              # Itinerario completo
├── .env                          # Variables de entorno (no compartir)
├── .env.example                  # Plantilla de variables
├── pyproject.toml                # Configuración del proyecto
└── README.md
```

---

## Reportes generados

Después de cada ejecución se generan dos archivos en `/reportes/`:

- **`local_guide_report.md`** — Guía detallada de la ciudad seleccionada
- **`itinerary.md`** — Itinerario completo día a día con hoteles, restaurantes y actividades

---

## Variables de entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `MODEL` | Modelo LLM a usar | Si |
| `ANTHROPIC_API_KEY` | API Key de Anthropic (Claude) | Si |
| `SERPER_API_KEY` | API Key de Serper (Google Search) | Si |

---

## Modelos compatibles

El sistema es compatible con cualquier LLM. Cambia el `MODEL` en tu `.env`:

```dotenv
# Anthropic (recomendado)
MODEL=anthropic/claude-haiku-4-5-20251001

# Groq (gratuito)
MODEL=groq/llama-3.1-8b-instant

# Local con Ollama (necesitas una consulta muy sencilla)
MODEL=ollama/llama3.1:8b
```

