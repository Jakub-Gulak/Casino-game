import dearpygui.dearpygui as dpg


def blackjack_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="blackjack_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"blackjack", tag='xxx')

    dpg.set_primary_window("blackjack_window", True)

    # dpg.set_viewport_resize_callback(update_gamepage_position)
    # update_gamepage_position()
