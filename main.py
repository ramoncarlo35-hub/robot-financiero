import os
import datetime

def generar_html():
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    
    herramientas = [
        {
            "nombre": "VEVOR España",
            "descripcion": "Maquinaria profesional, herramientas de taller y equipamiento industrial con envío rápido y grandes descuentos.",
            "categoria": "Herramientas & Bricolaje",
            "precio": "Ofertas exclusivas",
            "enlace": "https://vevores.sjv.io/c/7568707/3812783/22819"
        },
        {
            "nombre": "Shopify",
            "descripcion": "La plataforma líder mundial para crear tiendas online, vender productos y gestionar tu comercio digital fácilmente.",
            "categoria": "E-commerce & Tiendas Online",
            "precio": "Prueba gratis",
            "enlace": "https://shopify.pxf.io/c/7568707/2784851/13624"
        },
        {
            "nombre": "Hostinger",
            "descripcion": "Alojamiento web rápido, económico y fiable para lanzar tus proyectos en WordPress o páginas personalizadas.",
            "categoria": "Hosting & Dominios",
            "precio": "Desde 2,99€/mes",
            "enlace": "https://shopify.pxf.io/c/7568707/2784851/13624"
        },
        {
            "nombre": "Brevo",
            "descripcion": "Plataforma completa para automatización de correo electrónico, campañas de marketing y gestión de clientes (CRM).",
            "categoria": "Email Marketing",
            "precio": "Plan gratuito disponible",
            "enlace": "https://shopify.pxf.io/c/7568707/2784851/13624"
        },
        {
            "nombre": "DHgate",
            "descripcion": "Plataforma global de comercio online ideal para encontrar una gran variedad de productos al por mayor y minorista.",
            "categoria": "E-commerce & Compras",
            "precio": "Variedad de ofertas",
            "enlace": "https://dhgate.sjv.io/c/7568707/3997138/12108"
        },
        {
            "nombre": "Preply",
            "descripcion": "Plataforma líder para conectar con profesores particulares y aprender idiomas de forma online y flexible.",
            "categoria": "Educación & Idiomas",
            "precio": "Clases personalizadas",
            "enlace": "https://preply.sjv.io/c/7568707/2135760/24422"
        },
        {
            "nombre": "UPERFECT",
            "descripcion": "Especialistas en monitores portátiles de alta calidad para teletrabajo, gaming y movilidad profesional.",
            "categoria": "Hardware & Tecnología",
            "precio": "Pantallas portátiles",
            "enlace": "https://uperfect.sjv.io/c/7568707/1226538/15155"
        },
        {
            "nombre": "Clean Email",
            "descripcion": "Asistente inteligente para limpiar tu bandeja de entrada, organizar correos y cancelar suscripciones fácilmente.",
            "categoria": "Productividad & Email",
            "precio": "Prueba gratuita",
            "enlace": "https://cleanemailr.pxf.io/c/7568707/1114171/5448"
        },
        {
           "nombre": "Flashcloud",
           "descripcion": "Soluciones de infraestructura cloud y alojamiento web de alto rendimiento para proyectos digitales y profesionales.",
           "categoria": "Cloud & Hosting",
           "precio": "Alta rentabilidad",
           "enlace": "https://flashcloud.pxf.io/c/7568707/3920665/52759"
        }
    ]

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="google0ff72ddaea5d0b98" />
    <meta name="google-adsense-account" content="ca-pub-9167281162035819">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9167281162035819"
     crossorigin="anonymous"></script>
    <title>Robot Financiero - Directorio de Herramientas Digitales</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f6f9;
            color: #333;
        }}
        header {{
            background: linear-gradient(135deg, #0066ff, #00cc99);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        header h1 {{ margin: 0; font-size: 2.5em; }}
        header p {{ margin-top: 10px; font-size: 1.1em; opacity: 0.9; }}
        .container {{
            max-width: 1000px;
            margin: 30px auto;
            padding: 0 20px;
        }}
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }}
        .card {{
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: translateY(-5px);
        }}
        .tag {{
            background: #eef2ff;
            color: #4f46e5;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.85em;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 10px;
            width: fit-content;
        }}
        .card h3 {{ margin: 0 0 10px 0; color: #111; }}
        .card p {{ color: #666; font-size: 0.95em; line-height: 1.5; }}
        .price {{ font-weight: bold; color: #10b981; margin: 15px 0; }}
        .btn {{
            display: block;
            text-align: center;
            background: #0066ff;
            color: white;
            text-decoration: none;
            padding: 12px;
            border-radius: 6px;
            font-weight: bold;
            transition: background 0.2s;
        }}
        .btn:hover {{ background: #0052cc; }}
        footer {{
            text-align: center;
            padding: 30px;
            color: #888;
            font-size: 0.9em;
            margin-top: 40px;
        }}
    </style>
</head>
<body>

    <header>
        <h1>🤖 Robot Financiero</h1>
        <p>Herramientas y software recomendados para optimizar tu negocio digital</p>
    </header>

    <div class="container">
        <div class="card-grid">
"""

    for item in herramientas:
        html_content += f"""
            <div class="card">
                <div>
                    <span class="tag">{item['categoria']}</span>
                    <h3>{item['nombre']}</h3>
                    <p>{item['descripcion']}</p>
                </div>
                <div>
                    <div class="price">{item['precio']}</div>
                    <a href="{item['enlace']}" target="_blank" class="btn">Probar {item['nombre']}</a>
                </div>
            </div>
"""

    html_content += f"""
        </div>
    </div>

    <footer>
        <p>Última actualización automática: {fecha_actual}</p>
        <p>&copy; {datetime.datetime.now().year} Robot Financiero. Todos los derechos reservados.</p>
    </footer>

</body>
</html>
"""

    # Crear la carpeta public si no existe y guardar el HTML dentro
    os.makedirs("public", exist_ok=True)
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # También se guarda en la raíz por compatibilidad
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("¡Página web generada con éxito en public/index.html con todas las marcas!")

if __name__ == "__main__":
    generar_html()
