import dearpygui.dearpygui as dpg

from gui.roulette import roulette_page
from gui.machine import machine_page
from gui.blackjack import blackjack_page


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    greeting_text = dpg.get_value("name_text")
    greeting_width = dpg.get_text_size(greeting_text)[0]

    dpg.configure_item("name_text", pos=((width - greeting_width) // 2, height // 6))
    dpg.configure_item("roulette_button", pos=((width - 300) // 2, (height // 2) - 50))
    dpg.configure_item("slot_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("blackjack_button", pos=((width - 300) // 2, (height // 2) + 50))


def roulette_button_click():
    if dpg.does_item_exist("roulette_window"):
        dpg.show_item("roulette_window")
    else:
        roulette_page()
    dpg.hide_item("casino_window2")


def machine_button_click():
    dpg.hide_item("casino_window2")
    machine_page()


def blackjack_button_click():
    dpg.hide_item("casino_window2")
    blackjack_page()


def show_games_page():
    name = dpg.get_value("input_name")
    greeting_text = f"Hello, {name}."

    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="casino_window2", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(greeting_text, tag="name_text")
        dpg.add_button(label="Roulette", width=300, tag="roulette_button", callback=roulette_button_click)
        dpg.add_button(label="Slot Machine", width=300, tag="slot_button", callback=machine_button_click)
        dpg.add_button(label="BlackJack", width=300, tag="blackjack_button", callback=blackjack_button_click)

    dpg.set_primary_window("casino_window2", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
