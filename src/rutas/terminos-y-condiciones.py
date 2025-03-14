from nicegui_router import ui, page
from componentes.menu_superior import menu_superior,footer
@page()
def terminos_condiciones():
    menu_superior()
    with ui.card_section():

        ui.markdown(f"""
# Términos y Condiciones de Uso

Bienvenido/a a **{{nombre_aplicacion}}**, una plataforma para la reserva de estacionamientos.  
Al utilizar nuestros servicios, aceptas los siguientes términos y condiciones. Por favor, léelos detenidamente.

## 1. Aceptación de los Términos

Al acceder y utilizar nuestra aplicación, aceptas cumplir con estos términos y condiciones,  
así como con nuestra **Política de Privacidad**.  
Si no estás de acuerdo con alguno de estos términos, te recomendamos que no utilices nuestros servicios.

## 2. Servicios Ofrecidos

**{{nombre_aplicacion}}** permite a los usuarios reservar espacios de estacionamiento en lugares específicos.  
Nuestros servicios incluyen:

- 🔍 Búsqueda de estacionamientos disponibles.
- 📅 Reserva de espacios en tiempo real.
- 💳 Pago en línea (si aplica).
- ℹ️ Información sobre tarifas y disponibilidad.

## 3. Registro de Usuario

Para utilizar nuestros servicios, es necesario **registrarse y crear una cuenta**.  
Al registrarte, aceptas:

- Proporcionar información **veraz, exacta y completa**.
- Mantener tu información de cuenta **actualizada**.
- Ser **responsable de todas las actividades** que ocurran bajo tu cuenta.

## 4. Reservas y Pagos

- Las **reservas** están sujetas a disponibilidad.
- El **pago** de la reserva se realizará a través de los métodos de pago disponibles en la plataforma.
- En caso de **cancelación**, consulta nuestra política de reembolsos (si aplica).

## 5. Uso Adecuado

El usuario se compromete a utilizar la aplicación de manera adecuada y conforme a la **ley**.  
Queda **prohibido**:

- ❌ Utilizar la aplicación para fines **ilegales o no autorizados**.
- ❌ Dañar, deshabilitar o sobrecargar la plataforma.
- ❌ Acceder a cuentas de otros usuarios sin autorización.

## 6. Responsabilidades del Usuario

- 📌 **Proporcionar información precisa** sobre tu vehículo al realizar una reserva.
- 📌 **Respetar las normas** del estacionamiento donde reserves (horarios, tarifas, etc.).
- 📌 En caso de **daños o incidentes**, deberás informar al proveedor del estacionamiento y a **{{nombre_aplicacion}}**.

## 7. Limitación de Responsabilidad

**{{nombre_aplicacion}}** no se hace responsable por:

- ⚠️ Daños o pérdidas derivadas del **uso incorrecto** de la plataforma.
- ⚠️ Problemas técnicos **fuera de nuestro control** (fallos de internet, dispositivos, etc.).
- ⚠️ Conflictos entre **usuarios y proveedores de estacionamiento**.

## 8. Modificaciones de los Términos

Nos reservamos el derecho de **modificar** estos términos y condiciones en cualquier momento.  
Te notificaremos sobre cambios significativos a través de la plataforma o por correo electrónico.

## 9. Privacidad

Tu privacidad es **importante** para nosotros.  
Consulta nuestra **[Política de Privacidad](#)** para conocer cómo recopilamos, usamos y protegemos tu información.

## 10. Contacto

Si tienes preguntas o inquietudes sobre estos términos y condiciones, puedes contactarnos a través de:

- 📧 **Correo electrónico**: soporte@tuaplicacion.com  
- 📞 **Teléfono**: +56 9 1234 5678  
- 📍 **Dirección**: {{direccion_empresa}}  

---

**Fecha de última actualización**: _{{fecha_actualizacion}}_
""")
    footer()
