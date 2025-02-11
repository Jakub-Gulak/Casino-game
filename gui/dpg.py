import dearpygui.dearpygui as dpg


def update_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()
    dpg.configure_item("card_1", pos=(width * 0.1, height * 0.1))
    dpg.configure_item("card_2", pos=(width * 0.8, height * 0.1))


def create_gui():
    dpg.create_context()

    width, height, channels, data = dpg.load_image("images/cards.png")

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="cards_tag")

    with dpg.window(label="Casino", tag="casino_window"):
        dpg.add_image("cards_tag", width=200, height=200, tag="card_1")
        dpg.add_image("cards_tag", width=200, height=200, tag="card_2")

    dpg.set_viewport_resize_callback(update_position)

    dpg.set_primary_window("casino_window", True)
    dpg.create_viewport(title='Custom Title', width=800, height=700, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    update_position()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
