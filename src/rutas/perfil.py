from nicegui_router import ui,page
from nicegui import app
from componentes.menu_superior import menu_superior,footer

@page()
async def perfil():
    menu_superior()
    if not app.storage.user["logeado"]:
        ui.navigate.to("/")

    perfil = app.storage.user["logeado_perfil"]

    def actualizar_datos(nuevos_datos): #funcion para poder, actualizar los datos, verifica los datos
        app.storage.user["logeado_perfil"] = nuevos_datos
        dialogo.refresh(nuevos_datos)
        mostrar_perfil.refresh(nuevos_datos) # actualiza la funcion 
   
    @ui.refreshable
    def dialogo(datos):
        with ui.dialog(value=True) as dialog:
            with ui.card():
                ui.label("Actualizar datos del perfil")
                nombre = ui.input("Nombre", value=datos["nombre"])
                apellido = ui.input("Apellido", value=datos["apellido"])
                rut = ui.input("Rut", value=datos["rut"])
                email = ui.input("Correo", value=datos["email"])
                telefono = ui.input("Telefono", value=datos["telefono"])
                with ui.card_actions():
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
                    ui.button("cancelar", on_click= dialog.close)

    @ui.refreshable #para refrescar la pagina sola
    def mostrar_perfil(datos):    #se agrego funcion para poder llamarla despues
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

                - **Nombre**: {datos["nombre"]}
                - **Apellido**: {datos["apellido"]}
                - **Rut**: {datos["rut"]}
                - **Correo Electrónico**: {datos["email"]}
                - **Teléfono**: {datos["telefono"]}
            """)
            with ui.card_actions():
                ui.button("Editar Perfil", on_click=lambda: dialogo(datos))
                ui.button("Volver").on_click(lambda: ui.navigate.to("/principal"))
                

    mostrar_perfil(app.storage.user["logeado_perfil"]) # aca se llama
    footer()
