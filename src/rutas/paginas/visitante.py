from nicegui_router import ui,page

@ui.page("/principal")

def principal():
    #menu
    with ui.header().classes("h-12 bg-[#0077B6] text-white flex items-center px-4 justify-between"):
        with ui.row():
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-8 h-8 rounded-full")
            ui.label("AparcaYa").classes("text-sm font-bold margin=0")
        ui.space()
        ui.button(text="Iniciar Sesion").props("flat").classes("text-white text-xs")
        ui.button(text="Registrarse").props("flat").classes("text-white text-xs")

    
    with ui.row().classes("space-x-4"):  # Contenedor que organiza las columnas en una fila
        with ui.column().classes("bg-gray-300 p-4 "):  # Primera columna
            ui.label("Columna 1")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]") 
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")
        with ui.column().classes("bg-gray-300 p-4 "):  # Segunda columna
            ui.label("Columna 2")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]") 
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")
        with ui.column().classes("bg-gray-300 p-4 "):  # Tercera columna
            ui.label("Columna 3")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]") 
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[200px] h-[200px]")


   

ui.run()