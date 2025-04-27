import dearpygui.dearpygui as dpg

from gui.roulette.roulette_logic import roulette_spin
from gui.player import player

selection_buttons = ["even_back_button", "odd_back_button", "under_back_button", "above_back_button"]
currently_selected = None


def create_themes():
    with dpg.theme(tag="selected_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 200, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 180, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 160, 0, 255))

    with dpg.theme(tag="unselected_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 70, 70, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (90, 90, 90, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (50, 50, 50, 255))


def secventions_update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("secventions_text"))[0]
    dpg.configure_item("secventions_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("even_back_button", pos=((width - 1300) // 2, height // 2))
    dpg.configure_item("odd_back_button", pos=((width - 600) // 2, height // 2))
    dpg.configure_item("under_back_button", pos=((width + 100) // 2, height // 2))
    dpg.configure_item("above_back_button", pos=((width + 800) // 2, height // 2))

    dpg.configure_item("secventions_text_money", pos=(((width - text_width) - 150) // 2, height // 4))

    dpg.configure_item("secventions_back_button", pos=((width - 300) // 2, (height // 2) + 300))


def select_button(selected_tag):
    global currently_selected
    currently_selected = selected_tag

    for tag in selection_buttons:
        if tag == selected_tag:
            dpg.bind_item_theme(tag, "selected_theme")
        else:
            dpg.bind_item_theme(tag, "unselected_theme")


def back_button_click():
    global currently_selected
    for tag in selection_buttons:
        dpg.bind_item_theme(tag, "unselected_theme")

    currently_selected = None
    dpg.hide_item("secventions_window")
    dpg.show_item("roulette_window")

    from gui.roulette.roulette import roulette_update_gamepage_position
    roulette_update_gamepage_position()


def even_button_click():
    select_button("even_back_button")


def odd_button_click():
    select_button("odd_back_button")


def under_button_click():
    select_button("under_back_button")


def above_button_click():
    select_button("above_back_button")


def secventions_bet_input(sender, app_data):
    try:
        value = int(app_data)
        if 0 < value <= player.get_money():
            dpg.show_item("secventions_back_button")
        else:
            dpg.hide_item("secventions_back_button")
    except ValueError:
        dpg.hide_item("secventions_back_button")


def secventions_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    money_text = f"You have {player.get_money()}$ money."

    create_themes()

    with dpg.window(tag="secventions_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Secventions", tag='secventions_text')
        dpg.add_text(f"{money_text}", tag='secventions_text_money')

        dpg.add_button(label="Even numbers", width=300, tag="even_back_button", callback=even_button_click)
        dpg.bind_item_theme("even_back_button", "unselected_theme")

        dpg.add_button(label="Odd numbers", width=300, tag="odd_back_button", callback=odd_button_click)
        dpg.bind_item_theme("odd_back_button", "unselected_theme")

        dpg.add_button(label="Under 18", width=300, tag="under_back_button", callback=under_button_click)
        dpg.bind_item_theme("under_back_button", "unselected_theme")

        dpg.add_button(label="Above 18", width=300, tag="above_back_button", callback=above_button_click)
        dpg.bind_item_theme("above_back_button", "unselected_theme")

        dpg.add_input_text(width=300, tag="roulette_colors_bet_input", default_value="0", show=True,
                           callback=secventions_bet_input)

        dpg.add_button(label="Back", width=300, tag="secventions_back_button", callback=back_button_click)

    dpg.set_primary_window("secventions_window", True)

    dpg.set_viewport_resize_callback(secventions_update_gamepage_position)
    secventions_update_gamepage_position()
