from nicegui_router import ui, page

@page()
def formulario_registro():
    def on_submit():
        print("")

    def input_jose(label, **kwargs):
        return ui.input(label=label, **kwargs).style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')

    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"):
        with ui.column().classes("absolute-center").style('max-width: 400px; width: 100%; padding: 20px; border-radius: 8px; border: 1px solid #ccc; background-color: #f9f9f9;'):
            ui.label("Registro de datos").style('font-size: 24px; font-weight: bold; color:black; text-align: center; margin-bottom: 20px;')

            usuario = ui.input(label="Nombre").classes("full-width") #.style('width: auto;  padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')    
            apellido = ui.input(label="Apellido").classes("full-width") #.style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
            rut = ui.input(label="Rut").classes("full-width") #.style('width: auto; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;')
            email = ui.input(label="Correo electrónico").classes("full-width") 
            telefono = ui.input(label="Teléfono").classes("full-width")
            contraseña = ui.input(label="Contraseña", password=True).classes("full-width")

            ui.button("Registrar", on_click=on_submit).style('background-color: black; color: white; padding: 12px; width: 95%; border-radius: 5px; font-size: 16px;')
