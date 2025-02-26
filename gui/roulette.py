import dearpygui.dearpygui as dpg


def roulette_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="roulette_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"roulette", tag='xxx')

    dpg.set_primary_window("roulette_window", True)

    # dpg.set_viewport_resize_callback(update_gamepage_position)
    # update_gamepage_position()
