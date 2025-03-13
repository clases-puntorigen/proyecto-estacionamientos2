from nicegui import app
from nicegui_router import page, ui, component, use_state
from componentes.login import formulario_login
from componentes.menu_superior import menu_superior
from modelos.estacionamientos import Usuarios

@page()
async def login():
    with ui.image("https://elcomercio.pe/resizer/JF4zBvpLD2JjnpJs5fKhFAwFNis=/1280x720/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/XVO6I5CHD5CUZGB5G57G5LVMFU.webp").classes(
        "absolute-full object-cover"
    ):
        async def form_enviado(datos):
            existe_usuario = await Usuarios.get_by_attribute(
                email = datos["username"],
                contrasena = datos["password"]
            )
            if not existe_usuario:
                ui.notify("Email o contraseña incorrectos", type="negative")
            else:
                ui.notify(f"Bienvenido {existe_usuario.nombre}", type="positive")
                app.storage.user["logeado"] = True
                app.storage.user["logeado_perfil"] = existe_usuario.to_dict()
                ui.timer(2, lambda: ui.navigate.to("/"), once=True)

        await formulario_login(form_enviado)