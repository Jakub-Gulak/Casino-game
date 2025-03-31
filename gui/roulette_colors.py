import time

import dearpygui.dearpygui as dpg
from .roulette_logic import roulette_spin


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("roulette_colors_text"))[0]
    dpg.configure_item("roulette_colors_text", pos=((width - text_width) // 2, height // 6))
    dpg.configure_item("roulette_colors_back_button", pos=((width - 300) // 2, (height // 2) + 300))

    dpg.configure_item("roulette_red_button", pos=((width - 1000) // 2, (height // 2)))
    dpg.configure_item("roulette_black_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("roulette_green_button", pos=((width + 400) // 2, (height // 2)))


def red_button_click():
    color = "red"
    hide_buttons()
    roulette_spin(dpg, "roulette_colors_text", "roulette_red_button")
    time.sleep(2)
    show_buttons()


def black_button_click():
    color = "black"
    hide_buttons()
    roulette_spin(dpg, "roulette_colors_text", "roulette_black_button")
    time.sleep(2)
    show_buttons()


def green_button_click():
    color = "green"
    hide_buttons()
    roulette_spin(dpg, "roulette_colors_text", "roulette_green_button")
    time.sleep(2)
    show_buttons()


def back_button_click():
    dpg.hide_item("roulette_colors_window")
    dpg.show_item("roulette_window")


def hide_buttons():
    dpg.hide_item("roulette_red_button")
    dpg.hide_item("roulette_black_button")
    dpg.hide_item("roulette_green_button")
    dpg.hide_item("roulette_colors_back_button")


def show_buttons():
    dpg.show_item("roulette_red_button")
    dpg.show_item("roulette_black_button")
    dpg.show_item("roulette_green_button")
    dpg.show_item("roulette_colors_back_button")


def create_themes():
    with dpg.theme(tag="red_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [250, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [250, 0, 0])

    with dpg.theme(tag="black_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [5, 5, 5])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [5, 5, 5])

    with dpg.theme(tag="green_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 200, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 200, 0])


def roulette_colors_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    create_themes()

    with dpg.window(tag="roulette_colors_window", pos=(0, 0), width=width, height=height, no_title_bar=True,
                    no_move=True):
        dpg.add_text(f"Roulette Colors", tag='roulette_colors_text')

        red_button = dpg.add_button(label="Red", width=300, tag="roulette_red_button", callback=red_button_click)
        black_button = dpg.add_button(label="Black", width=300, tag="roulette_black_button",
                                      callback=black_button_click)
        green_button = dpg.add_button(label="Green", width=300, tag="roulette_green_button",
                                      callback=green_button_click)

        dpg.add_button(label="Back", width=300, tag="roulette_colors_back_button", callback=back_button_click)

        dpg.bind_item_theme(red_button, "red_button_theme")
        dpg.bind_item_theme(black_button, "black_button_theme")
        dpg.bind_item_theme(green_button, "green_button_theme")

    dpg.set_primary_window("roulette_colors_window", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
