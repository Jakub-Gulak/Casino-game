import dearpygui.dearpygui as dpg


def create_gui():
    dpg.create_context()

    width, height, channels, data = dpg.load_image("images/cards.png")

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="cards_tag")

    with dpg.window(label="Casino", tag="casino_window"):
        dpg.add_image("cards_tag", width=100, height=100)

    dpg.set_primary_window("casino_window", True)
    dpg.create_viewport(title='Custom Title', width=800, height=700, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
