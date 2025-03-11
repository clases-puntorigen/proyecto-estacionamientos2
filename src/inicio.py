from nicegui_router import Server
from nicegui import app as app_nicegui
from pathlib import Path
import asyncio
from async_easy_model import init_db, db_config
from modelos.estacionamientos import Usuarios,Vehiculos,Horarios,Estacionamientos,Reserva,Pagos,TarifasEspeciales

async def startup_db_reservas_estacionamientos():
    await init_db()
    print("inicio bd")

server = Server(
    title='Reserva estacionamientos', 
    routes_dir=Path(__file__).parent / "rutas",
    on_startup=startup_db_reservas_estacionamientos,
    ui={
        "language": "es"
    }

)

app = server.app
static_path = Path(__file__).parent / "assets"
app_nicegui.add_static_files("/assets", static_path)


if __name__ == '__main__':
    server.listen(port=8080)