from nicegui_router import ui,page


@ui.page("/estacionamiento")

def estacionamiento():
    with ui.header().classes("h-12 bg-[#0077B6] text-white flex items-center px-7 justify-between"):
        with ui.row().classes("items-center"):
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
            ui.label("AparcaYa").classes("text-sm font-bold margin=0")
        ui.space()
        ui.button(text="Principal").props("flat").classes("text-white text-xs")
        ui.button(text="Nosotros").props("flat").classes("text-white text-xs")
        with ui.row().classes("items-center"):
            imagen =  ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full items-center")
            with ui.menu():
                with ui.column().classes("bg-white shadow-lg p-2 rounded-md"):
                    ui.button("Perfil", on_click=lambda: ui.notify("Opción 1 seleccionada")).classes("w-full")
                    ui.button("Cerrar Sesion", on_click=lambda: ui.notify("Opción 2 seleccionada")).classes("w-full")
        #con chatgpt, para poder saber como hacerlo visible y no...       
                def toggle_menu():
                    if menu.visible:
                        menu.classes("hidden")
                    else:
                        menu.classes(remove="hidden")
                imagen.on("click", toggle_menu)

    #cuerpo
    with ui.row():
        with ui.column():
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[400px]")
            ui.label("Detalle del estacionamiento").classes("text-lg font-bold")
            
        with ui.column():
            ui.label("Ubicación").classes("text-lg font-bold")
            ui.button("Reservar Estacionamiento", on_click=lambda: ui.notify("¡Envio a reserva!"))







