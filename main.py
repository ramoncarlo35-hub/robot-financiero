Python
import os

# Crear la carpeta donde se guardará la web
os.makedirs("public", exist_ok=True)

def obtener_ofertas():
    """
    Lista de ejemplo. Más adelante puedes conectar esto a una API 
    o lista real de productos/servicios monetizables.
    """
    return [
        {
            "titulo": "Auriculares Inalámbricos Canc. Ruido",
            "precio_original": "59.99€",
            "precio_oferta": "29.99€",
            "enlace": "https://www.amazon.es"
        },
        {
            "titulo": "Teclado Mecánico RGB Gaming",
            "precio_original": "79.99€",
            "precio_oferta": "45.50€",
            "enlace": "https://www.amazon.es"
        },
        {
            "titulo": "Monitor 24 pulgadas Full HD 144Hz",
            "precio_original": "189.00€",
            "precio_oferta": "129.00€",
            "enlace": "https://www.amazon.es"
        }
    ]

def generar_web(ofertas):
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robot Financiero - Oportunidades Automáticas</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; color: #333; }
        .header { text-align: center; padding: 20px 0; background: #fff; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .container { max-width: 800px; margin: 0 auto; }
        .card { background: white; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.08); display: flex; justify-content: space-between; align-items: center; }
        .card-info h3 { margin: 0 0 10px 0; color: #1a73e8; }
        .price { font-size: 1.2em; font-weight: bold; color: #2e7d32; }
        .old-price { text-decoration: line-through; color: #888; font-size: 0.9em; margin-right: 8px; }
        .btn { background: #ff9900; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; }
        .btn:hover { background: #e68a00; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Robot Financiero</h1>
            <p>Oportunidades y chollos actualizados en tiempo real de forma autómata</p>
        </div>
    """
    
    for item in ofertas:
        html += f"""
        <div class="card">
            <div class="card-info">
                <h3>{item['titulo']}</h3>
                <p><span class="old-price">{item['precio_original']}</span><span class="price">{item['precio_oferta']}</span></p>
            </div>
            <a href="{item['enlace']}" class="btn" target="_blank">Ver Oportunidad</a>
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
    print("Robot Financiero trabajando...")
    datos = obtener_ofertas()
    generar_web(datos)
    print("¡Web actualizada y lista!")
