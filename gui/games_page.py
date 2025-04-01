import dearpygui.dearpygui as dpg

from gui.player import player
from gui.roulette.roulette import roulette_page
from gui.machine import machine_page
from gui.blackjack import blackjack_page
from gui.end import end_page


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    name = dpg.get_value("name_text")
    player.set_name(name)
    greeting_width = dpg.get_text_size(name)[0]

    money_width = dpg.get_text_size(dpg.get_value("money_text"))[0]

    dpg.configure_item("name_text", pos=((width - greeting_width) // 2, height // 6))
    dpg.configure_item("money_text", pos=((width - money_width) // 2, height // 5))
    dpg.configure_item("roulette_button", pos=((width - 300) // 2, (height // 2) - 50))
    dpg.configure_item("slot_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("blackjack_button", pos=((width - 300) // 2, (height // 2) + 50))
    dpg.configure_item("leave_casino_button", pos=((width - 300) // 2, (height // 2) + 300))


def roulette_button_click():
    if dpg.does_item_exist("roulette_window"):
        dpg.show_item("roulette_window")
    else:
        roulette_page()
    dpg.hide_item("casino_window2")


def machine_button_click():
    if dpg.does_item_exist("slot_machine_window"):
        dpg.show_item("slot_machine_window")
    else:
        machine_page()
    dpg.hide_item("casino_window2")


def blackjack_button_click():
    if dpg.does_item_exist("blackjack_window"):
        dpg.show_item("blackjack_window")
    else:
        blackjack_page()
    dpg.hide_item("casino_window2")


def leave_casino_button_click():
    dpg.hide_item("casino_window2")
    end_page()


def show_games_page():
    name = dpg.get_value("input_name")
    player.set_name(name)
    greeting_text = f"Hello, {name}."
    money_text = f"You have {player.get_money()}$ money."

    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="casino_window2", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(greeting_text, tag="name_text")
        dpg.add_text(money_text, tag="money_text")
        dpg.add_button(label="Roulette", width=300, tag="roulette_button", callback=roulette_button_click)
        dpg.add_button(label="Slot Machine", width=300, tag="slot_button", callback=machine_button_click)
        dpg.add_button(label="BlackJack", width=300, tag="blackjack_button", callback=blackjack_button_click)
        dpg.add_button(label="Leave The Casino", width=300, tag="leave_casino_button",
                       callback=leave_casino_button_click)

    dpg.set_primary_window("casino_window2", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
