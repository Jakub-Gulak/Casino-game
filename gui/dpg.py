import dearpygui.dearpygui as dpg

with dpg.window(label="Casino Game"):
    dpg.add_text("Hello!")

dpg.create_viewport(title="Casino Game", width=400, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
