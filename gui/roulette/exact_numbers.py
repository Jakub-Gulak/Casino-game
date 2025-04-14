import dearpygui.dearpygui as dpg
from gui.player import player
from gui.roulette.roulette_logic import roulette_spin


def exact_numbers_update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("exact_numbers_text"))[0]
    dpg.configure_item("text_money", pos=((width - text_width) // 2.12, height // 4))
    dpg.configure_item("exact_numbers_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("exact_numbers_bet_input", pos=((width - 300) // 2, (height // 2) - 200))

    dpg.configure_item("bet_text", pos=((width - 450) // 2, (height // 2) - 200))

    dpg.configure_item("exact_numbers_back_button", pos=((width - 300) // 2, (height // 2) + 300))
    dpg.configure_item("exact_numbers_spin_button", pos=((width - 300) // 2, (height // 2)))


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
    pass


def update_bet_buttons():
    current_bet = dpg.get_value("exact_numbers_bet_input")
    exact_numbers_bet_input(None, current_bet)


def back_button_click():
    dpg.hide_item("exact_numbers_window")
    dpg.show_item("roulette_window")


def exact_numbers_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()
    money_text = f"You have {player.get_money()}$ money."

    with dpg.window(tag="exact_numbers_window", pos=(0, 0), width=width, height=height, no_title_bar=True,
                    no_move=True):
        dpg.add_text(f"Exact numbers", tag='exact_numbers_text')

        dpg.add_input_text(width=300, tag="exact_numbers_bet_input", default_value="0", show=True,
                           callback=exact_numbers_bet_input)

        dpg.add_text(f"{money_text}", tag='text_money')
        dpg.add_text("Bet:", tag='bet_text')

        dpg.add_button(label="Spin", width=300, tag="exact_numbers_spin_button", show=False,
                       callback=exact_numbers_spin_button)
        dpg.add_button(label="Back", width=300, tag="exact_numbers_back_button", callback=back_button_click)

    dpg.set_primary_window("exact_numbers_window", True)

    dpg.set_viewport_resize_callback(exact_numbers_update_gamepage_position)
    exact_numbers_update_gamepage_position()
