from nicegui import ui
@ui.page("/registro")

def formulario_registro():
    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"
    ):
        with ui.row().style('height: 100vh; justify-content: center; align-items: center;'):
            with ui.column().style('max-width: 400px; width: 100%; padding: 20px; border-radius: 8px; border: 1px solid #ccc; background-color: #f9f9f9;'):
                ui.label("Registro de datos").style('font-size: 24px; font-weight: bold; color:black; text-align: center; margin-bottom: 20px;')

                
                usuario = ui.input(label="Nombre").style('width: auto;  padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')    
                apellido = ui.input(label="Apellido").style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                rut = ui.input(label="Rut").style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                email = ui.input(label="Correo electrónico").style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                telefono = ui.input(label="Teléfono").style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
                contraseña = ui.input(label="Contraseña", password=True).style('width: auto; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;')

                def on_submit():
                    print("")
                ui.button("Registrar", on_click=on_submit).style('background-color: black; color: white; padding: 12px; width: 95%; border-radius: 5px; font-size: 16px;')
