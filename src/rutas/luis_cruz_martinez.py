from nicegui_router import ui,page
from componentes.menu_superior import menu_superior, footer

@page()
async def estacionamiento():
    menu_superior()

    with ui.row():
        with ui.column():
            ui.label("Estacionamiento Luis Cruz Martinez")
            ui.label("Dirección: Calle Falsa 123, La Ligua")
            ui.label("Servicios:")
            # ver los iconos
            ui.label("Precio: $1,500 por hora")
        with ui.column():
            m = ui.leaflet(center=(-32.450, -71.232), zoom=15).style('width: 500px; height: 500px;')

            cuadrado = m.generic_layer(name='polygon', args=[[  
                (-32.451111, -71.231000),  # Arriba izquierda
                (-32.451111, -71.230500),  # Arriba derecha
                (-32.451611, -71.230500),  # Abajo derecha
                (-32.451611, -71.231000),  # Abajo izquierda
                        ]])
            await m.initialized()
            bounds = await central_park.run_method('getBounds')
            m.run_map_method('fitBounds', [[bounds['_southWest'], bounds['_northEast']]])












    footer()




