from nicegui_router import Server
from pathlib import Path
import asyncio
from async_easy_model import init_db, db_config
from modelos.estacionamientos import Usuarios,Vehiculos,Horarios,Estacionamientos,Reserva,Pagos,TarifasEspeciales

async def startup_db_reservas_estacionamientos():
    await init_db()
    print("inicio bd")

server = Server(
    title='Reserva estacionamientos', 
    routes_dir=Path(__file__).parent / "rutas"/"paginas",
    on_startup=startup_db_reservas_estacionamientos,
    ui={
        "language": "es"
    }

)

app = server.app

if __name__ == '__main__':
    server.listen(port=8080)