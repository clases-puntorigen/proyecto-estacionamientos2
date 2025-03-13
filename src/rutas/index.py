from nicegui_router import ui,page
from nicegui import app
from componentes.menu_superior import menu_superior
@page()
def visitante():
    #menu
    if not "logeado" in app.storage.user:
        app.storage.user["logeado"] = False
    menu_superior()
   #cuerpo
    with ui.column().classes("items-center justify-center w-full space-y-4"):  
        with ui.row().classes("bg-while-300 p-4 w-[80%] justify-center items-center"): 
            ui.label("Por Hora").classes("text-xl font-bold mb-4")
            with ui.row().classes("space-x-4 justify-center"):
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]") 
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")

        with ui.row().classes("bg-while-300 p-4 w-[80%] justify-center items-center"): 
            ui.label("Por Día").classes("text-xl font-bold mb-4")
            with ui.row().classes("space-x-4 justify-center"):
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]") 
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")

        with ui.row().classes("bg-while-300 p-4 w-[80%] justify-center items-center"):  
            ui.label("Semanal").classes("text-xl font-bold mb-4")
            with ui.row().classes("space-x-4 justify-center"):
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]") 
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")

        with ui.row().classes("bg-while-300 p-4 w-[80%] justify-center items-center"):  
            ui.label("Mensual").classes("text-xl font-bold mb-4")
            with ui.row().classes("space-x-4 justify-center"):
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]") 
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")
                with ui.column().classes("items-center"):
                    ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[350px]")
                    ui.label("Descripcion del estacionamiento")
    #pie
    with ui.footer().classes("h-12 bg-[#0077B6] text-white items-center justify-center px-4 justify-between"):
        ui.label("Contacto").classes("text-sm text-center")
        ui.label("Correo: hola@gmail.com").classes("text-sm text-center")
        ui.label("wsp: +56912345678").classes("text-sm text-center")
        ui.space()
        ui.button(text="Iniciar Sesion").props("flat").classes("text-white text-xs")
        ui.button(text="Registrarse").props("flat").classes("text-white text-xs")


