from nicegui_router import Server
from pathlib import Path
from nicegui import app 
#import asyncio
from async_easy_model import init_db, db_config
from modelos.estacionamientos import Usuarios,Vehiculos,Horarios,Estacionamientos,Reserva,Pagos,TarifasEspeciales

async def startup_db_reservas_estacionamientos():
    try:
        await init_db()
        print("inicio bd")
    except:
        print("Error al iniciar la base de datos")
    
server = Server(
    title='Reserva estacionamientos', 
    routes_dir=Path(__file__).parent / "rutas",
    #on_startup=startup_db_reservas_estacionamientos,
    ui={
        "language": "es",
        "storage_secret": "reserva_estacionamientos",
    }

)
static_path = Path(__file__).parent / "assets"
app.add_static_files("/assets", static_path)

usuarios_conectados = 0
usuarios_x_hora = {}
#usuarios_x_hora[20] = 10
#usuarios_x_hora[21] = 3


def actualizar_usuarios_conectados():
    from datetime import datetime
    global usuarios_conectados
    usuarios_conectados += 1
    hora = datetime.now().hour
    if hora in usuarios_x_hora:
        usuarios_x_hora[hora] += 1
    else:
        usuarios_x_hora[hora] = 1
    app.storage.general["usuarios_conectados"] = usuarios_conectados
    # guardar dict usuarios_x_hora en BD o en archivo
    print(f"Usuarios conectados: {usuarios_conectados}")

def actualizar_usuarios_desconectados():
    global usuarios_conectados
    usuarios_conectados -= 1
    app.storage.general["usuarios_conectados"] = usuarios_conectados
    print(f"Usuarios conectados: {usuarios_conectados}")
    

app.on_connect(actualizar_usuarios_conectados)
app.on_disconnect(actualizar_usuarios_desconectados)
app.on_startup(startup_db_reservas_estacionamientos)
#asyncio.run(startup_db_reservas_estacionamientos())

if __name__ == '__main__':
    server.listen(port=8080)