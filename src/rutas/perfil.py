from nicegui_router import ui,page
from nicegui import app
from componentes.menu_superior import menu_superior,footer


@page()
async def perfil():
    menu_superior()
    if not app.storage.user["logeado"]:
        ui.navigate.to("/")

    perfil = app.storage.user["logeado_perfil"]

    @ui.refreshable
    def mostrar_perfil():
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
                ui.button("Volver").on_click(lambda: ui.navigate.to("/principal"))
                

    mostrar_perfil()

    def actualizar_datos(nuevos_datos):
        app.storage.user["logeado_perfil"] = nuevos_datos
        mostrar_perfil.refresh()

    with ui.dialog() as dialog, ui.card():
        ui.label("Actualizar datos del perfil")
        nombre = ui.input("Nombre", value=perfil["nombre"])
        apellido = ui.input("Apellido", value=perfil["apellido"])
        rut = ui.input("Rut", value=perfil["rut"])
        email = ui.input("Correo", value=perfil["email"])
        telefono = ui.input("Telefono", value=perfil["telefono"])
        #ver para cambiar la contraseña

        def guardar_datos_actualizados():
            nuevos_datos = {
                "nombre": nombre.value,
                "apellido": apellido.value,
                "rut": rut.value,
                "email": email.value,
                "telefono": telefono.value,
            }
            actualizar_datos(nuevos_datos)
            dialog.close()

        ui.button("Guardar", on_click=guardar_datos_actualizados)
    ui.button("Editar Perfil", on_click=dialog.open)
    footer()
