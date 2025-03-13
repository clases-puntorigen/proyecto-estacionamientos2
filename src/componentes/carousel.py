from contextlib import contextmanager
from nicegui_router import ui

@contextmanager
def item():
    with ui.carousel_slide().classes('p-0') as slide:
        yield slide

@contextmanager
def carousel(tiempo=3):
    with ui.carousel(animated=False, arrows=False, navigation=False).classes("w-full") as carousel:
        yield carousel

    # Start the carousel timer
    indice = 0
    total_slides = len(carousel.slots["default"].children)
    
    def rotate_slide():
        nonlocal indice
        #print(f"posicion = indice % total_slides = {indice} % {total_slides} = {indice % total_slides}")
        posicion = (indice % total_slides) + 1
        carousel.set_value(f"slide_{posicion}")
        #print(f"indice actual: {posicion}")
        indice += 1
        #print(f"(indice:{indice}) slide_{indice % total_slides}")

    ui.timer(tiempo, rotate_slide)