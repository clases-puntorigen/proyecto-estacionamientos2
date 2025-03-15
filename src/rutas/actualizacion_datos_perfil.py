from nicegui_router import ui,page
from componentes.menu_superior import menu_superior,footer
from nicegui import app
page()
def actualizar_perfil():
    menu_superior()
    if not app.storage.user["logeado"]:
        ui.navigate.to("/")
    
        perfil = app.storage.user["logeado_perfil"]
    with ui.card(align_items="center").classes(
        "absolute-center w-[500px] ma-0"
    ).style(
        "background-color: #FFF; padding:0 0 0 0;"
    ):
        with ui.card_section():
            ui.label("Perfil").classes("text-h6 q-mb-xs text-center")
        with ui.card_section():

            ui.markdown(f"""
            ## Datos personales

            **Nombre**: {perfil["nombre"]}<br/>
            **Apellido**: {perfil["apellido"]}<br/>  
            **Rut**: {perfil["rut"]}<br/>
            **Correo electrónico**: {perfil["email"]}<br/>
            **Teléfono**: {perfil["telefono"]}<br/>
        """)
        

