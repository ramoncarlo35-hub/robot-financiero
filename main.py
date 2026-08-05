import os

# Crear la carpeta donde se guardará la web
os.makedirs("public", exist_ok=True)

def obtener_herramientas():
    """
    Catálogo de Herramientas Digitales y Hosting.
    Aquí irás cambiando las URL de 'enlace' por tus enlaces de afiliado a medida que te des de alta.
    """
    return [
        {
            "categoria": "🌐 Hosting & Web",
            "titulo": "Hostinger - Plan Web Premium",
            "descripcion": "Ideal para crear webs rápidas con dominio gratis y soporte 24/7.",
            "descuento": "75% DTO",
            "precio_desde": "2.99€ / mes",
            "enlace": "https://www.hostinger.es"
        },
        {
            "categoria": "🔒 Seguridad & Privacidad",
            "titulo": "NordVPN - Protección Total",
            "descripcion": "Navegación segura, ultra rápida y acceso a contenido global sin límites.",
            "descuento": "68% DTO + 3 Meses Gratis",
            "precio_desde": "3.09€ / mes",
            "enlace": "https://nordvpn.com"
        },
        {
            "categoria": "🤖 Inteligencia Artificial & Contenidos",
            "titulo": "Notion AI - Productividad con IA",
            "descripcion": "Organiza tus tareas, redacta contenido y gestiona proyectos en un solo lugar.",
            "descuento": "Prueba Gratuita",
            "precio_desde": "0.00€",
            "enlace": "https://www.notion.so"
        },
        {
            "categoria": "📈 Email Marketing & Automatización",
            "titulo": "Brevo (Sendinblue) - Envíos Masivos",
            "descripcion": "Plataforma líder para automatizar correos y newsletters para tus clientes.",
            "descuento": "Plan Gratis 300 emails/día",
            "precio_desde": "0.00€",
            "enlace": "https://www.brevo.com"
        }
    ]

def generar_web(herramientas):
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robot Financiero - Herramientas Digitales & Software</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; color: #2c3e50; }
        .container { max-width: 900px; margin: 0 auto; }
        .header { text-align: center; padding: 30px 20px; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; border-radius: 12px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .header h1 { margin: 0 0 10px 0; font-size: 2.2em; }
        .header p { margin: 0; opacity: 0.9; font-size: 1.1em; }
        .card { background: white; border-radius: 12px; padding: 22px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; justify-content: space-between; align-items: center; gap: 20px; transition: transform 0.2s; }
        .card:hover { transform: translateY(-3px); }
        .badge { background-color: #e8f5e9; color: #2e7d32; font-size: 0.85em; font-weight: bold; padding: 4px 10px; border-radius: 20px; display: inline-block; margin-bottom: 8px; }
        .card-info h3 { margin: 5px 0 8px 0; color: #1a2a3a; font-size: 1.3em; }
        .card-info p { margin: 0 0 12px 0; color: #666; font-size: 0.95em; line-height: 1.4; }
        .price-box { font-size: 1.1em; font-weight: bold; color: #d32f2f; }
        .discount { background: #ffebee; color: #c62828; padding: 3px 8px; border-radius: 5px; font-size: 0.85em; margin-right: 8px; }
        .btn { background: #0066ff; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; text-align: center; whitespace: nowrap; transition: background 0.2s; }
        .btn:hover { background: #0052cc; }
        @media (max-width: 600px) {
            .card { flex-direction: column; align-items: flex-start; }
            .btn { width: 100%; box-sizing: border-box; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Robot Financiero: Software & SaaS</h1>
            <p>Selección autómata de las mejores herramientas digitales y licencias en oferta</p>
        </div>
    """
    
    for item in herramientas:
        html += f"""
        <div class="card">
            <div class="card-info">
                <span class="badge">{item['categoria']}</span>
                <h3>{item['titulo']}</h3>
                <p>{item['descripcion']}</p>
                <div class="price-box">
                    <span class="discount">{item['descuento']}</span>
                    <span>Desde {item['precio_desde']}</span>
                </div>
            </div>
            <a href="{item['enlace']}" class="btn" target="_blank" rel="noopener">Obtener Oferta ➔</a>
        </div>
        """
        
    html += """
    </div>
</body>
</html>
    """
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    print("Robot Financiero: Actualizando portal de Software...")
    datos = obtener_herramientas()
    generar_web(datos)
    print("¡Portal de herramientas publicado con éxito!")
