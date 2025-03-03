import dearpygui.dearpygui as dpg


def update_gamepage_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    text_width = dpg.get_text_size(dpg.get_value("roulette_text"))[0]
    dpg.configure_item("roulette_text", pos=((width - text_width) // 2, height // 6))

    dpg.configure_item("colors_button", pos=((width - 300) // 2, (height // 2) - 50))
    dpg.configure_item("exact_numbers_button", pos=((width - 300) // 2, (height // 2)))
    dpg.configure_item("secventions_button", pos=((width - 300) // 2, (height // 2) + 50))


def colors_button_click():
    pass


def exact_numbers_button_click():
    pass


def secventions_button_click():
    pass


def roulette_page():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    roulette_text = f"Roulette"

    with dpg.window(tag="roulette_window", pos=(0, 0), width=width, height=height, no_title_bar=True, no_move=True):
        dpg.add_text(roulette_text, tag='roulette_text')
        dpg.add_button(label="Colors", width=300, tag="colors_button", callback=colors_button_click)
        dpg.add_button(label="Exact Numbers", width=300, tag="exact_numbers_button",
                       callback=exact_numbers_button_click)
        dpg.add_button(label="Secventions", width=300, tag="secventions_button", callback=secventions_button_click)

    dpg.set_primary_window("roulette_window", True)

    dpg.set_viewport_resize_callback(update_gamepage_position)
    update_gamepage_position()
