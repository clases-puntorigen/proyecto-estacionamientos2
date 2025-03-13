from nicegui_router import ui   
from nicegui import app

@ui.refreshable
def usuarios_conectados():
    ui.label(f"{app.storage.general["usuarios_conectados"]} Usuarios Conectados")

def menu_superior():
    def cerrar_sesion():
        menu.close
        app.storage.user["logeado"] = False
        ui.navigate.to("/")
    
    ui.timer(2,lambda: usuarios_conectados.refresh())
    with ui.header().classes("bg-[#0077B6] text-white flex items-center"):
        with ui.row().classes("items-center"):
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
            ui.label("AparcaYa").classes("text-sm font-bold margin=0")
            
        usuarios_conectados()
        if app.storage.user["logeado"]:
            ui.space()
            ui.button(text="Principal").props("flat").classes("text-white text-xs")
            ui.button(text="Nosotros").props("flat").classes("text-white text-xs")
            with ui.row().classes("items-center"):
                #imagen = ui.avatar(icon="img:https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("rounded-full")
                imagen = ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
                with imagen:
                    with ui.menu() as menu:
                        ui.menu_item("Perfil", on_click=lambda: ui.notify("Perfil"))
                        ui.menu_item("Cerrar Sesion", on_click=lambda: menu.close)
        else:
            ui.space()
            ui.button(text="Iniciar Sesion").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/login"))
            ui.button(text="Registrarse").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/registro"))