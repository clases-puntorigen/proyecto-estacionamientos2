from nicegui_router import ui,page
from modelos.estacionamientos import Vehiculos
from componentes.menu_superior import menu_superior,footer
@page()
def registro_vehiculo():
    menu_superior()
    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"
    ):
         with ui.column().classes("absolute-center").style('max-width: 400px; width: 100%; padding: 20px; border-radius: 8px; border: 1px solid #ccc; background-color: #f9f9f9;'):
            ui.label("Registro Vehiculo").style('font-size: 24px; font-weight: bold; color:black; text-align: center; margin-bottom: 20px;')

            marca = ui.input(label="Marca").classes("full-width")
            modelo = ui.input(label="Modelo").classes("full-width")
            patente = ui.input(label="Patente").classes("full-width")
            color = ui.input(label="Color").classes("full-width")
            #ver como conecto el id del usuario al vehiculo(fk)

            async def on_submit():
                existe_vehiculo = await Vehiculo.get_by_attribute(
                    patente = patente.Value
                )
                if vehiculo_existente:
                    ui.notify("El Vehiculo ya existe", type="negative")
                else:
                    await Vehiculos.insert({
                        "marca" : marca.Value,
                        "modelo" : modelo.Value,
                        "patente" : patente.Value,
                        "color" : color.Value
                    })
                    ui.notify("Vehiculo registrado", type="positive")
                    ui.timer(2, lambda: ui.navigate.to("/"), once=True)

            ui.button("Registrar Vehiculo", on_click=on_submit).style('background-color: black; color: white; padding: 12px; width: 95%; border-radius: 5px; font-size: 16px;')

    footer()


         