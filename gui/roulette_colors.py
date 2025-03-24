import dearpygui.dearpygui as dpg


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("roulette_colors_text"))[0]
    dpg.configure_item("roulette_colors_text", pos=((width - text_width) // 2, height // 6))
    dpg.configure_item("roulette_colors_back_button", pos=((width - 300) // 2, (height // 2) + 300))

    dpg.configure_item("roulette_red_button", pos=((width - 300) // 2, (height // 2) - 50))
    dpg.configure_item("roulette_black_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("roulette_green_button", pos=((width - 300) // 2, (height // 2) + 50))


def back_button_click():
    dpg.hide_item("roulette_colors_window")
    dpg.show_item("roulette_window")


def red_button_click():
    pass


def black_button_click():
    pass


def green_button_click():
    pass


def roulette_colors_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    with dpg.window(tag="roulette_colors_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(f"Roulette Colors", tag='roulette_colors_text')

        dpg.add_button(label="Red", width=300, tag="roulette_red_button", callback=red_button_click)

        dpg.add_button(label="Black", width=300, tag="roulette_black_button", callback=black_button_click)
        dpg.add_button(label="Green", width=300, tag="roulette_green_button", callback=green_button_click)

        dpg.add_button(label="Back", width=300, tag="roulette_colors_back_button", callback=back_button_click)

    dpg.set_primary_window("roulette_colors_window", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
