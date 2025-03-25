from nicegui_router import ui, page
from componentes.menu_superior import menu_superior,footer
from componentes.carousel import carousel, item as slide


def item(imagen="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s"):
    with ui.column().classes("items-center"):
        ui.image(imagen).classes("w-[350px] h-[350px]")
        ui.label("Descripcion del estacionamiento")
        ui.button("Reservar", on_click=lambda: ui.navigate.to(archivo)).classes("bg-blue-500 text-white px-4 py-2 rounded-lg")

@page()
def principal():
    menu_superior()
#carrusel

    with carousel(tiempo=5):
        with slide():
            ui.image("/assets/slide1.jpg")
        with slide():
            ui.image("/assets/slide2.jpg")
    
#estacionamientos por secciones
    with ui.column().classes("items-center justify-center w-full space-y-4"):  
        for titulo in ["Por Hora","Por Día","Semanal","Mensual"]:
            with ui.row().classes("bg-white-300 p-4 w-[80%] justify-center items-center"): 
                ui.label(titulo).classes("text-xl font-bold mb-4")
                with ui.row().classes("space-x-4 justify-center"):
                    for _ in range(3):
                        item()

#footer
    footer()

            