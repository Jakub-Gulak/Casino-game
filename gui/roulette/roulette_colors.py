import time
import dearpygui.dearpygui as dpg

from gui.roulette.roulette_logic import roulette_spin_color
from gui.player import player


def roulette_colors_update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("roulette_colors_text"))[0]
    dpg.configure_item("roulette_colors_text_money", pos=((width - text_width) // 2.12, height // 4))
    dpg.configure_item("roulette_colors_text", pos=((width - text_width) // 2, height // 6))
    dpg.configure_item("roulette_colors_back_button", pos=((width - 300) // 2, (height // 2) + 300))

    dpg.configure_item("roulette_red_button", pos=((width - 1000) // 2, (height // 2)))
    dpg.configure_item("roulette_black_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("roulette_green_button", pos=((width + 400) // 2, (height // 2)))

    dpg.configure_item("roulette_colors_bet_text", pos=((width - 450) // 2, (height // 2) - 200))
    dpg.configure_item("result_text", pos=((width - 100) // 2, (height // 2) - 200))
    dpg.configure_item("roulette_colors_bet_input", pos=((width - 300) // 2, (height // 2) - 200))


def roulette_colors_bet_input(sender, app_data):
    try:
        value = int(app_data)
        if 0 < value <= player.get_money():
            dpg.show_item("roulette_red_button")
            dpg.show_item("roulette_black_button")
            dpg.show_item("roulette_green_button")
        else:
            dpg.hide_item("roulette_red_button")
            dpg.hide_item("roulette_black_button")
            dpg.hide_item("roulette_green_button")
    except ValueError:
        dpg.hide_item("roulette_red_button")
        dpg.hide_item("roulette_black_button")
        dpg.hide_item("roulette_green_button")


def update_bet_buttons():
    current_bet = dpg.get_value("roulette_colors_bet_input")
    roulette_colors_bet_input(None, current_bet)


def red_button_click():
    bet_amount = int(dpg.get_value("roulette_colors_bet_input"))
    if bet_amount > player.get_money():
        return

    color = "Red"
    hide_buttons()
    dpg.set_value("result_text", "")
    result = roulette__color(dpg, "roulette_colors_text", "roulette_red_button")
    if result != color:
        player.money -= bet_amount
        dpg.set_value("result_text", f"You lose.")
    else:
        player.money = (player.money - bet_amount) + bet_amount * 2
        dpg.set_value("result_text", f"You win.")

    dpg.set_value("roulette_colors_bet_input", "0")

    dpg.set_value("roulette_colors_text_money", f"You have {player.money}$ money.")
    from gui.games_page import update_money_text
    update_money_text()
    dpg.show_item("result_text")
    time.sleep(2.5)
    if player.get_money() == 0:
        dpg.hide_item("roulette_red_button")
        dpg.hide_item("roulette_black_button")
        dpg.hide_item("roulette_green_button")
        dpg.show_item("roulette_colors_back_button")
    else:
        dpg.enable_item("roulette_red_button")
        show_buttons()
        update_bet_buttons()


def black_button_click():
    bet_amount = int(dpg.get_value("roulette_colors_bet_input"))
    if bet_amount > player.get_money():
        return

    color = "Black"
    hide_buttons()
    dpg.set_value("result_text", "")
    result = roulette_color(dpg, "roulette_colors_text", "roulette_black_button")
    if result != color:
        player.money -= bet_amount
        dpg.set_value("result_text", f"You lose.")
    else:
        player.money = (player.money - bet_amount) + bet_amount * 2
        dpg.set_value("result_text", f"You win.")

    dpg.set_value("roulette_colors_bet_input", "0")

    dpg.set_value("roulette_colors_text_money", f"You have {player.money}$ money.")
    from gui.games_page import update_money_text
    update_money_text()
    dpg.show_item("result_text")
    time.sleep(2.5)
    if player.get_money() == 0:
        dpg.hide_item("roulette_red_button")
        dpg.hide_item("roulette_black_button")
        dpg.hide_item("roulette_green_button")
        dpg.show_item("roulette_colors_back_button")
    else:
        dpg.enable_item("roulette_black_button")
        show_buttons()
        update_bet_buttons()


def green_button_click():
    bet_amount = int(dpg.get_value("roulette_colors_bet_input"))
    if bet_amount > player.get_money():
        return

    color = "Green"
    hide_buttons()
    dpg.set_value("result_text", "")
    result = roulette_spin_color(dpg, "roulette_colors_text", "roulette_green_button")
    if result != color:
        player.money -= bet_amount
        dpg.set_value("result_text", f"You lose.")
    else:
        player.money = (player.money - bet_amount) + bet_amount * 2
        dpg.set_value("result_text", f"You win.")

    dpg.set_value("roulette_colors_bet_input", "0")

    dpg.set_value("roulette_colors_text_money", f"You have {player.money}$ money.")
    from gui.games_page import update_money_text
    update_money_text()
    dpg.show_item("result_text")
    time.sleep(2.5)
    if player.get_money() == 0:
        dpg.hide_item("roulette_red_button")
        dpg.hide_item("roulette_black_button")
        dpg.hide_item("roulette_green_button")
        dpg.show_item("roulette_colors_back_button")
    else:
        dpg.enable_item("roulette_green_button")
        show_buttons()
        update_bet_buttons()


def back_button_click():
    dpg.hide_item("roulette_colors_window")
    dpg.show_item("roulette_window")

    from gui.roulette.roulette import roulette_update_gamepage_position
    roulette_update_gamepage_position()


def hide_buttons():
    dpg.hide_item("roulette_red_button")
    dpg.hide_item("roulette_black_button")
    dpg.hide_item("roulette_green_button")
    dpg.hide_item("roulette_colors_back_button")
    dpg.hide_item("roulette_colors_bet_input")
    dpg.hide_item("roulette_colors_bet_text")
    dpg.hide_item("roulette_colors_text_money")


def show_buttons():
    dpg.show_item("roulette_red_button")
    dpg.show_item("roulette_black_button")
    dpg.show_item("roulette_green_button")
    dpg.show_item("roulette_colors_back_button")
    dpg.show_item("roulette_colors_bet_input")
    dpg.show_item("roulette_colors_bet_text")
    dpg.show_item("roulette_colors_text_money")


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
    money_text = f"You have {player.get_money()}$ money."

    create_themes()

    with dpg.window(tag="roulette_colors_window", pos=(0, 0), width=width, height=height, no_title_bar=True,
                    no_move=True, no_bring_to_front_on_focus=True):
        dpg.add_text(f"Roulette Colors", tag='roulette_colors_text')

        red_button = dpg.add_button(label="Red", width=300, tag="roulette_red_button", callback=red_button_click,
                                    show=False)
        black_button = dpg.add_button(label="Black", width=300, tag="roulette_black_button",
                                      callback=black_button_click, show=False)
        green_button = dpg.add_button(label="Green", width=300, tag="roulette_green_button",
                                      callback=green_button_click, show=False)

        dpg.add_text(f"{money_text}", tag='roulette_colors_text_money')
        dpg.add_text("", tag='result_text')
        dpg.add_text("Bet:", tag='roulette_colors_bet_text')
        dpg.add_input_text(width=300, tag="roulette_colors_bet_input", default_value="0", show=True,
                           callback=roulette_colors_bet_input)

        dpg.add_button(label="Back", width=300, tag="roulette_colors_back_button", callback=back_button_click)

        dpg.bind_item_theme(red_button, "red_button_theme")
        dpg.bind_item_theme(black_button, "black_button_theme")
        dpg.bind_item_theme(green_button, "green_button_theme")

    dpg.set_primary_window("roulette_colors_window", True)

    dpg.set_viewport_resize_callback(roulette_colors_update_gamepage_position)
    roulette_colors_update_gamepage_position()
