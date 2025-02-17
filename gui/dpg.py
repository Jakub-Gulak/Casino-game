import dearpygui.dearpygui as dpg


def update_position():
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()

    margin = 50
    img_size = 190

    x = (width // 2) - 150
    y = (height // 2) - 25

    dpg.configure_item("card_1", pos=(margin, 100))
    dpg.configure_item("chip_1", pos=(margin, 400))
    dpg.configure_item("machine_1", pos=(margin, 700))

    dpg.configure_item("card_2", pos=(width - img_size - margin, 100))
    dpg.configure_item("chip_2", pos=(width - img_size - margin, 400))
    dpg.configure_item("machine_2", pos=(width - img_size - margin, 700))

    dpg.configure_item("enter-name_text", pos=(x + 70, y - 60))
    dpg.configure_item("input_name", pos=(x, y))
    dpg.configure_item("casino_button", pos=(x, y + 60))


def casino_button_click():
    print("siema")


def create_gui():
    dpg.create_context()

    cards_width, cards_height, cards_channels, cards_data = dpg.load_image("images/cards.png")
    chips_width, chips_height, chips_channels, chips_data = dpg.load_image("images/casino_chips.png")
    machines_width, machines_height, machines_channels, machines_data = dpg.load_image("images/slot_machine.png")

    with dpg.font_registry():
        font = dpg.add_font("fonts/Atkinson_Hyperlegible_Next/AtkinsonHyperlegibleNext-VariableFont_wght.ttf", 40)
        dpg.bind_font(font)

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=cards_width, height=cards_height, default_value=cards_data, tag="cards_tag")
        dpg.add_static_texture(width=chips_width, height=chips_height, default_value=chips_data, tag="chips_tag")
        dpg.add_static_texture(width=machines_width, height=machines_height, default_value=machines_data,
                               tag="machines_tag")

    with dpg.window(label="Casino", tag="casino_window"):
        dpg.add_text("Your name:", tag="enter-name_text")
        dpg.add_input_text(width=300, height=50, tag="input_name")
        dpg.add_button(label="Go to Casino!", width=300, height=50, tag="casino_button", callback=casino_button_click)

        dpg.add_image("cards_tag", width=190, height=190, tag="card_1")
        dpg.add_image("cards_tag", width=190, height=190, tag="card_2")
        dpg.add_image("chips_tag", width=190, height=190, tag="chip_1")
        dpg.add_image("chips_tag", width=190, height=190, tag="chip_2")
        dpg.add_image("machines_tag", width=190, height=190, tag="machine_1")
        dpg.add_image("machines_tag", width=190, height=190, tag="machine_2")

    dpg.set_viewport_resize_callback(update_position)

    dpg.set_primary_window("casino_window", True)
    dpg.create_viewport(title='Custom Title', width=1400, height=900, resizable=True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    update_position()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
