from nicegui_router import ui,page
from componentes.menu_superior import menu_superior,footer
@page()
def nosotros():
    menu_superior()
    with ui.row():
        with ui.column():
            ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpSelqig2f7PiM4oxIzBrLNzo0eI9P-YLCg&s").classes("w-[350px] h-[400px]")
                       
        with ui.column():
            ui.markdown(f"""
# Sobre Nosotros

Bienvenido/a a **{{nombre_empresa}}**, una empresa dedicada a {{descripcion_empresa}}.  
Nuestro compromiso es ofrecer soluciones eficientes e innovadoras para {{sector_o_servicio}}.

## ¿Quiénes Somos?

En **{{nombre_empresa}}**, nos especializamos en {{especialidad_empresa}}.  
Nuestra misión es proporcionar {{objetivo_principal}}, asegurando calidad, seguridad y confianza en cada servicio que ofrecemos.

## Nuestros Valores

En nuestra empresa, nos guiamos por los siguientes valores fundamentales:

- 🤝 **Compromiso** – Trabajamos con responsabilidad y dedicación para cumplir con las expectativas de nuestros clientes.
- 💡 **Innovación** – Buscamos constantemente nuevas soluciones para mejorar nuestros servicios y adaptarnos a las necesidades del mercado.
- 🔒 **Seguridad** – Garantizamos un entorno seguro en cada interacción con nuestros usuarios.
- 🌱 **Sostenibilidad** – Nos preocupamos por el impacto ambiental y promovemos prácticas responsables.
- 📞 **Atención al Cliente** – Nos enfocamos en brindar un soporte excepcional y una experiencia de usuario óptima.

## Nuestra Propuesta de Valor

En **{{nombre_empresa}}**, nos diferenciamos por:

✅ **{{diferenciador_1}}** – {{descripcion_diferenciador_1}}  
✅ **{{diferenciador_2}}** – {{descripcion_diferenciador_2}}  
✅ **{{diferenciador_3}}** – {{descripcion_diferenciador_3}}  

Nos esforzamos cada día para mejorar y ofrecer un servicio que realmente marque la diferencia.

## Contáctanos

Si deseas más información sobre nuestra empresa o nuestros servicios, puedes comunicarte con nosotros a través de:

- 📧 **Correo electrónico**: {{correo_contacto}}
- 📞 **Teléfono**: {{telefono_contacto}}
- 📍 **Dirección**: {{direccion_empresa}}

---

**Fecha de última actualización**: _{{fecha_actualizacion}}_
""")
    footer()
