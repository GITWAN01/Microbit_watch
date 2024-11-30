def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_screen_up():
    basic.show_string("12:00")
    music.play(music.string_playable("G F G A - F E D ", 500),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    basic.clear_screen()
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    basic.show_string("" + str((input.compass_heading())))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global steps
    steps += 1
    basic.show_number(steps)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
steps = 0