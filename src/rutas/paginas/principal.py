from nicegui_router import ui,page

@ui.page("/principal")

def principal():
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

    #ver mapa interactivo para agregar
    #----------------------------------------------------------------------------------------------#











    #---------------------------------------------------------------------------------------------#
#estacionamientos por secciones

    with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')
    