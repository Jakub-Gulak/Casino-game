import dearpygui.dearpygui as dpg
import time
from gui.player import player
from gui.roulette.roulette_logic import roulette_spin_number


def exact_numbers_update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("exact_numbers_text"))[0]
    dpg.configure_item("exact_numbers_text_money", pos=((width - text_width) // 2.12, height // 4))
    dpg.configure_item("exact_numbers_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("exact_numbers_bet_text", pos=((width - 450) // 2, (height // 2) - 200))
    dpg.configure_item("exact_numbers_bet_input", pos=((width - 300) // 2, (height // 2) - 200))

    dpg.configure_item("exact_numbers_number_input", pos=((width - 300) // 2, (height // 2) - 100))

    dpg.configure_item("exact_numbers_back_button", pos=((width - 300) // 2, (height // 2) + 300))
    dpg.configure_item("exact_numbers_spin_button", pos=((width - 300) // 2, (height // 2)))

    dpg.configure_item("numbers_result_text", pos=((width - 100) // 2, (height // 2) - 200))


def exact_numbers_bet_input(sender, app_data):
    try:
        value = int(app_data)
        if 0 < value <= player.get_money():
            dpg.show_item("exact_numbers_spin_button")
        else:
            dpg.hide_item("exact_numbers_spin_button")
    except ValueError:
        dpg.hide_item("exact_numbers_spin_button")


def exact_numbers_spin_button():
    bet_amount = int(dpg.get_value("exact_numbers_bet_input"))
    if bet_amount > player.get_money():
        return

    hide_buttons()
    number = int(dpg.get_value("exact_numbers_number_input"))
    dpg.set_value("numbers_result_text", "")

    result = roulette_spin_number(dpg, "exact_numbers_text", "exact_numbers_spin_button")
    if result != number:
        player.money -= bet_amount
        dpg.set_value("numbers_result_text", f"You lose.")
    else:
        player.money = (player.money - bet_amount) + bet_amount * 2
        dpg.set_value("numbers_result_text", f"You win.")

    dpg.set_value("exact_numbers_bet_input", 0)

    dpg.set_value("exact_numbers_text_money", f"You have {player.money}$ money.")
    from gui.games_page import update_money_text
    update_money_text()
    dpg.show_item("numbers_result_text")
    time.sleep(2.5)
    dpg.hide_item("numbers_result_text")
    if player.get_money() == 0:
        dpg.hide_item("exact_numbers_spin_button")
        dpg.show_item("exact_numbers_back_button")
    else:
        dpg.enable_item("exact_numbers_spin_button")
        show_buttons()
        update_bet_buttons()


def hide_buttons():
    dpg.hide_item("exact_numbers_text_money")
    dpg.hide_item("exact_numbers_bet_text")
    dpg.hide_item("exact_numbers_bet_input")
    dpg.hide_item("exact_numbers_number_input")
    dpg.hide_item("exact_numbers_back_button")
    dpg.hide_item("exact_numbers_spin_button")
    dpg.hide_item("numbers_result_text")
    dpg.hide_item("numbers_result_text")


def show_buttons():
    dpg.show_item("exact_numbers_text_money")
    dpg.show_item("exact_numbers_text")
    dpg.show_item("exact_numbers_bet_text")
    dpg.show_item("exact_numbers_bet_input")
    dpg.show_item("exact_numbers_number_input")
    dpg.show_item("exact_numbers_back_button")
    dpg.show_item("exact_numbers_spin_button")


def exact_numbers_number_input(sender, app_data):
    try:
        value = int(app_data)
        if value < 1:
            dpg.set_value(sender, 1)
        elif value > 37:
            dpg.set_value(sender, 37)
    except ValueError:
        dpg.set_value(sender, 1)


def update_bet_buttons():
    current_bet = dpg.get_value("exact_numbers_bet_input")
    exact_numbers_bet_input(None, current_bet)


def back_button_click():
    dpg.hide_item("exact_numbers_window")
    dpg.show_item("roulette_window")

    from gui.roulette.roulette import roulette_update_gamepage_position
    roulette_update_gamepage_position()


def exact_numbers_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()
    money_text = f"You have {player.get_money()}$ money."

    with dpg.window(tag="exact_numbers_window", pos=(0, 0), width=width, height=height, no_title_bar=True,
                    no_move=True, no_bring_to_front_on_focus=True):
        dpg.add_text(f"Exact numbers", tag='exact_numbers_text')

        dpg.add_input_text(width=300, tag="exact_numbers_bet_input", default_value="0", show=True,
                           callback=exact_numbers_bet_input)

        dpg.add_input_int(width=300, tag="exact_numbers_number_input", show=True, default_value=1, min_value=1,
                          max_value=37,
                          callback=exact_numbers_number_input)

        dpg.add_text(f"{money_text}", tag='exact_numbers_text_money')
        dpg.add_text("", tag='numbers_result_text')
        dpg.add_text("Bet:", tag='exact_numbers_bet_text')

        dpg.add_button(label="Spin", width=300, tag="exact_numbers_spin_button", show=False,
                       callback=exact_numbers_spin_button)
        dpg.add_button(label="Back", width=300, tag="exact_numbers_back_button", callback=back_button_click)

    dpg.set_primary_window("exact_numbers_window", True)

    dpg.set_viewport_resize_callback(exact_numbers_update_gamepage_position)
    exact_numbers_update_gamepage_position()
