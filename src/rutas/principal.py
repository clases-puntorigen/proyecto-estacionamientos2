from nicegui_router import ui,page
from componentes.menu_superior import menu_superior
from componentes.carousel import carousel, item as slide

def item(imagen="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s", archivo="/estacionamiento"):
    with ui.column().classes("items-center"):
        ui.image(imagen).classes("w-[350px] h-[350px]")
        ui.label("Descripcion del estacionamiento")
        ui.button("Reservar", on_click=lambda: ui.navigate.to(archivo)).classes("bg-blue-500 text-white px-4 py-2 rounded-lg")

@page()
def principal():
    menu_superior()
    
    with ui.header(fixed=True).classes("h-12 bg-[#0077B6] text-white flex items-center px-7 justify-between"):
        with ui.row().classes("items-center"):
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
            ui.label("AparcaYa").classes("text-sm font-bold margin=0")
        ui.space()
        ui.button(text="Principal").props("flat").classes("text-white text-xs")
        ui.button(text="Nosotros").props("flat").classes("text-white text-xs")
        with ui.row().classes("items-center"):
            imagen =  ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
            with ui.menu() as menu:
                with ui.column().classes("bg-white shadow-lg p-2 rounded-md"):
                    ui.button("Perfil", on_click=lambda: ui.notify("Perfil")).classes("w-full")
                    ui.button("Cerrar Sesion", on_click=lambda: ui.notify(" Cerrar sesión")).classes("w-full")
        #con chatgpt, para poder saber como hacerlo visible y no...       
                def toggle_menu():
                    if menu.visible:
                        menu.classes("hidden")
                    else:
                        menu.classes(remove="hidden")
                imagen.on("click", toggle_menu)

    #ver mapa interactivo para agregar
    #----------------------------------------------------------------------------------------------#










    #---------------------------------------------------------------------------------------------#
#carrusel
    with carousel(tiempo=4):
        with slide():
            ui.image("/assets/slide1.jpg")
        with slide():
            ui.image("/assets/slide2.jpg")

    #estacionamientos por secciones
    with ui.column().classes("items-center justify-center w-full space-y-4"):  
        for titulo in ["Por Hora","Por Día","Semanal","Mensual"]:
            with ui.row().classes("bg-while-300 p-4 w-[80%] justify-center items-center"): 
                ui.label(titulo).classes("text-xl font-bold mb-4")
                with ui.row().classes("space-x-4 justify-center"):
                    for _ in range(3):
                        item()

    with ui.footer(bordered=False, fixed=False).classes("h-12 bg-[#0077B6] text-white items-center justify-center px-4 justify-between"):
        ui.label("Contacto").classes("text-sm text-center")
        ui.label("Correo: hola@gmail.com").classes("text-sm text-center")
        ui.label("wsp: +56912345678").classes("text-sm text-center")
        ui.space()
        ui.button(text="Iniciar Sesion").props("flat").classes("text-white text-xs")
        ui.button(text="Registrarse").props("flat").classes("text-white text-xs")