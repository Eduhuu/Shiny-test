from shiny import render, ui
from shiny.express import input

ui.panel_title("Hola Maru esto es una prueba!")
ui.input_slider("n", "N", 0, 100, 20)


@render.text
def txt():
    return f"n*2 is {input.n() * 2}"
