import markdown2
from weasyprint import HTML

def md_a_pdf(texto):
    '''
    Convertir la salida de MD a un PDF
    '''
    html_content = markdown2.markdown(texto)
    
    # Agregar estilos CSS
    html_con_estilos = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; }}
            h2 {{ color: #34495e; }}
            h3 {{ color: #7f8c8d; }}
            ul {{ padding-left: 20px; }}
            li {{ margin: 5px 0; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    pdf = HTML(string=html_con_estilos).write_pdf()
    return pdf