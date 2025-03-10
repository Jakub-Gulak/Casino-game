import dearpygui.dearpygui as dpg


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("end_text"))[0]
    dpg.configure_item("end_text", pos=((width - text_width) // 2, height // 6))
    dpg.configure_item("end_button", pos=((width - 300) // 2, (height // 2) - 50))


def end_button_click():
    dpg.stop_dearpygui()


def end_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="end_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text("You won X money", tag='end_text')
        dpg.add_button(label="End", width=300, tag="end_button", callback=end_button_click)

    dpg.set_primary_window("end_window", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
