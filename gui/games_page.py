import dearpygui.dearpygui as dpg


def show_games_page():
    name = dpg.get_value("input_name")

    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="casino_window2", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Hello, {name}.")
        dpg.add_button(label="Roulette", width=300, tag="roulette_button",)
        dpg.add_button(label="Slot Machine", width=300, tag="slot_button",)
        dpg.add_button(label="BlackJack", width=300, tag="blackjack_button",)

    dpg.set_primary_window("casino_window2", True)
