import dearpygui.dearpygui as dpg


def machine_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="machine_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"machine", tag='xxx')

    dpg.set_primary_window("machine_window", True)

    # dpg.set_viewport_resize_callback(update_gamepage_position)
    # update_gamepage_position()
