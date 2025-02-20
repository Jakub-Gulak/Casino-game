import dearpygui.dearpygui as dpg


def show_games_page():
    name = dpg.get_value("input_name")

    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="casino_window2", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Hello, {name} .Welcome to Page 2!")

    dpg.set_primary_window("casino_window2", True)
