import random
import time

ROULETTE_NUMBERS = [
    (0, "Green"),
    (32, "Red"), (15, "Black"), (19, "Red"), (4, "Black"),
    (21, "Red"), (2, "Black"), (25, "Red"), (17, "Black"),
    (34, "Red"), (6, "Black"), (27, "Red"), (13, "Black"),
    (36, "Red"), (11, "Black"), (30, "Red"), (8, "Black"),
    (23, "Red"), (10, "Black"), (5, "Red"), (24, "Black"),
    (16, "Red"), (33, "Black"), (1, "Red"), (20, "Black"),
    (14, "Red"), (31, "Black"), (9, "Red"), (22, "Black"),
    (18, "Red"), (29, "Black"), (7, "Red"), (28, "Black"),
    (12, "Red"), (35, "Black"), (3, "Red"), (26, "Black")
]


def roulette_spin(dpg, roulette_text_tag, roulette_button_tag):
    steps = random.randint(40, 60)
    delay = 0.01

    start_index = random.randint(0, len(ROULETTE_NUMBERS) - 1)
    current_index = start_index

    for i in range(steps):
        number, color = ROULETTE_NUMBERS[current_index]
        dpg.set_value(roulette_text_tag, f"Spinning... {number} {color}")
        time.sleep(delay)

        delay = delay * 1.05
        current_index = (current_index + 1) % len(ROULETTE_NUMBERS)

    final_number, final_color = ROULETTE_NUMBERS[current_index]
    dpg.set_value(roulette_text_tag, f"Result: {final_number} {final_color}")

    dpg.disable_item(roulette_button_tag)
