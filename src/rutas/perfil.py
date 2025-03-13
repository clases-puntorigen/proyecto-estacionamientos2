from nicegui_router import ui,page
from nicegui import app
from componentes import menu_superior

@page()
async def perfil():
    menu_superior()
    if not app.storage.user["loegado"]:
        ui.navigate.to("/")
