import asyncio
from async_easy_model import init_db, db_config
import os
from datetime import date

async def main():
    
    if os.path.exists('reservas_estacionamientos.db'):
        os.remove('reservas_estacionamientos.db')


db_config.configure_sqlite("reservas_estacionamientos.db")


await init_db()
print("Database initialized")



if __name__ == "__main__":
    asyncio.run(main())

