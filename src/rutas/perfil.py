from nicegui_router import ui,page
from nicegui import app
from componentes.menu_superior import menu_superior


@page()
async def perfil():
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
            ## Datos Personales

            - **Nombre**: {perfil["nombre"]}
            - **Apellido**: {perfil["apellido"]}
            - **Rut**: {perfil["rut"]}
            - **Correo Electrónico**: {perfil["email"]}
            - **Teléfono**: {perfil["telefono"]}
        """)
        with ui.card_actions():
            ui.button("Editar perfil").on_click(lambda: ui.navigate.to("/editar_perfil"))
            ui.button("Volver").on_click(lambda: ui.navigate.to("/principal"))
