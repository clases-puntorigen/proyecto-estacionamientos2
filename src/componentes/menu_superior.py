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
            ui.button(text="Principal").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/principal"))
            ui.button(text="Nosotros").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/nosotros"))
            with ui.row().classes("items-center"):
                #imagen = ui.avatar(icon="img:https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("rounded-full")
                imagen = ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
                with imagen:
                    with ui.menu() as menu:
                        ui.menu_item("Perfil", on_click=lambda: ui.notify("Perfil")).on_click(lambda: ui.navigate.to("/perfil"))
                        ui.menu_item("Cerrar Sesion", on_click=lambda: menu.close).on_click(lambda: ui.navigate.to("/"))
        else:
            ui.space()
            ui.button(text="Iniciar Sesion").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/login"))
            ui.button(text="Registrarse").props("flat").classes("text-white text-xs").on_click(lambda: ui.navigate.to("/registro"))


def footer():
        with ui.footer(bordered=False, fixed=False).classes("h-24 bg-[#0077B6] text-white flex items-center justify-center px-4"):
            with ui.row().classes("w-full max-w-4xl justify-between items-start"):
                # Parte izquierda: Información de contacto
                with ui.column().classes("items-start gap-1"):
                    ui.label("Contacto").classes("text-sm font-medium")
                    ui.label("Correo: hola@gmail.com").classes("text-sm")
                    ui.label("WhatsApp: +56912345678").classes("text-sm")
                
                # Parte central: Términos y condiciones (como un enlace)
                with ui.column().classes("items-center gap-1"):
                    ui.link("Términos y condiciones", "/terminos-y-condiciones").classes("text-sm hover:underline")
                
                # Parte derecha: Un elemento adicional (por ejemplo, un ícono o logo)
                with ui.column().classes("items-end gap-1"):
                    ui.icon("thumb_up", size="sm").classes("text-white")
                    ui.label("¡Síguenos!").classes("text-sm")