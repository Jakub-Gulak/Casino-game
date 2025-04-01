import dearpygui.dearpygui as dpg


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("secventions_text"))[0]
    dpg.configure_item("secventions_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("secventions_back_button", pos=((width - 300) // 2, (height // 2) + 300))


def back_button_click():
    dpg.hide_item("secventions_window")
    dpg.show_item("roulette_window")


def secventions_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="secventions_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Secventions", tag='secventions_text')

        dpg.add_button(label="Back", width=300, tag="secventions_back_button", callback=back_button_click)

    dpg.set_primary_window("secventions_window", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
