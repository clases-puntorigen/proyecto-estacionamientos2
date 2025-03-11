from nicegui_router import ui,page

@page()
def perfil():
    with ui.row().classes():
        with ui.column().classes():
            ui.label("Perfil")





ui.run()
