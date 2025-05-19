import dearpygui.dearpygui as dpg
import time

from gui.roulette.roulette_logic import roulette_spin_number
from gui.player import player

selection_buttons = ["even_button", "odd_button", "under_button", "above_button"]
currently_selected = None

def secventions_update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("secventions_text"))[0]
    dpg.configure_item("secventions_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("even_button", pos=((width - 1300) // 2, height // 2))
    dpg.configure_item("odd_button", pos=((width - 600) // 2, height // 2))
    dpg.configure_item("under_button", pos=((width + 100) // 2, height // 2))
    dpg.configure_item("above_button", pos=((width + 800) // 2, height // 2))

    dpg.configure_item("secventions_text_money", pos=(((width - text_width) - 150) // 2, height // 4))

    dpg.configure_item("secventions_back_button", pos=((width - 300) // 2, (height // 2) + 300))

    dpg.configure_item("result_text", pos=((width - 100) // 2, (height // 2) - 200))

    dpg.configure_item("secventions_bet_input", pos=((width - 300) // 2, (height // 2) - 200))


def update_bet_buttons():
    current_bet = dpg.get_value("secventions_bet_input")
    secventions_bet_input(None, current_bet)


def back_button_click():
    dpg.hide_item("secventions_window")
    dpg.show_item("roulette_window")

    from gui.roulette.roulette import roulette_update_gamepage_position
    roulette_update_gamepage_position()


def even_button_click():
    bet_amount = int(dpg.get_value("secventions_bet_input"))
    if bet_amount > player.get_money():
        return

    number = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    hide_buttons()

    result = roulette_spin_number(dpg, "secventions_text", "even_button")
    print(result)
    if result not in number:
        player.money -= bet_amount
        dpg.set_value("result_text", f"You lose.")
    else:
        player.money = (player.money - bet_amount) + bet_amount * 2
        dpg.set_value("result_text", f"You win.")

    dpg.set_value("secventions_bet_input", "0")

    dpg.set_value("secventions_text_money", f"You have {player.money}$ money.")
    from gui.games_page import update_money_text
    update_money_text()
    dpg.show_item("result_text")
    time.sleep(2.5)
    if player.get_money() == 0:
        dpg.hide_item("even_button")
        dpg.hide_item("odd_button")
        dpg.hide_item("under_button")
        dpg.hide_item("above_button")
        dpg.show_item("secventions_back_button")
    else:
        dpg.enable_item("even_button")
        show_buttons()
        update_bet_buttons()


def odd_button_click():
    bet_amount = int(dpg.get_value("secventions_bet_input"))
    if bet_amount > player.get_money():
        return

    number = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    hide_buttons()


def under_button_click():
    bet_amount = int(dpg.get_value("secventions_bet_input"))
    if bet_amount > player.get_money():
        return

    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    hide_buttons()
    dpg.set_value("result_text", "")


def above_button_click():
    bet_amount = int(dpg.get_value("secventions_bet_input"))
    if bet_amount > player.get_money():
        return

    number = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    hide_buttons()


def hide_buttons():
    dpg.hide_item("even_button")
    dpg.hide_item("odd_button")
    dpg.hide_item("under_button")
    dpg.hide_item("above_button")
    dpg.hide_item("secventions_bet_input")
    dpg.hide_item("secventions_back_button")
    dpg.hide_item("secventions_text_money")


def show_buttons():
    dpg.show_item("even_button")
    dpg.show_item("odd_button")
    dpg.show_item("under_button")
    dpg.show_item("above_button")
    dpg.show_item("secventions_bet_input")
    dpg.show_item("secventions_back_button")
    dpg.show_item("secventions_text_money")


def secventions_bet_input(sender, app_data):
    try:
        value = int(app_data)
        if 0 < value <= player.get_money():
            dpg.show_item("even_button")
            dpg.show_item("odd_button")
            dpg.show_item("under_button")
            dpg.show_item("above_button")
        else:
            dpg.hide_item("even_button")
            dpg.hide_item("odd_button")
            dpg.hide_item("under_button")
            dpg.hide_item("above_button")
    except ValueError:
        dpg.hide_item("even_button")
        dpg.hide_item("odd_button")
        dpg.hide_item("under_button")
        dpg.hide_item("above_button")


def secventions_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    money_text = f"You have {player.get_money()}$ money."

    with dpg.window(tag="secventions_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Secventions", tag='secventions_text')
        dpg.add_text(f"{money_text}", tag='secventions_text_money')

        dpg.add_button(label="Even numbers", width=300, tag="even_button", callback=even_button_click, show=False)

        dpg.add_button(label="Odd numbers", width=300, tag="odd_button", callback=odd_button_click, show=False)

        dpg.add_button(label="Under 18", width=300, tag="under_button", callback=under_button_click, show=False)

        dpg.add_button(label="Above 18", width=300, tag="above_button", callback=above_button_click, show=False)

        dpg.add_text("", tag='result_text')

        dpg.add_input_text(width=300, tag="secventions_bet_input", default_value="0", show=True,
                           callback=secventions_bet_input)

        dpg.add_button(label="Back", width=300, tag="secventions_back_button", callback=back_button_click)

    dpg.set_primary_window("secventions_window", True)

    dpg.set_viewport_resize_callback(secventions_update_gamepage_position)
    secventions_update_gamepage_position()
