from nicegui_router import ui,page

@page()
def registro_vehiculo():
    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"
    ):
        with ui.row().classes("items-center justify-center w-full space-y-4"):
            with ui.column().style('max-width: 400px; width: 100%; padding: 20px; border-radius: 8px; border: 1px solid #ccc; background-color: #f9f9f9;'):
                ui.label("Registro Vehiculo").style('font-size: 24px; font-weight: bold; color:black; text-align: center; margin-bottom: 20px;')

                marca = ui.input(label="Marca").style('width: 100%;  padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')    
                modelo = ui.input(label="Modelo").style('width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                patente = ui.input(label="Patente").style('width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                color = ui.input(label="Color").style('width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                
                ui.button("Registrar Vehiculo", on_click=lambda: ui.notify("Vehiculo Registrado Con Exito")).classes("w-full")
