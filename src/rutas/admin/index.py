from nicegui_router import page, ui, component, use_state
from componentes.login import formulario_login

@page()
async def login():
    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"
    ):
        def form_enviado(datos):
            ui.notify(f"Username: {datos["username"]}, Password: {datos["password"]}")
            ui.navigate.to("/admin/logged")

        formulario_login(form_enviado)