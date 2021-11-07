def on_button_pressed_a():
    radio.send_string(Lozinka)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Lozinka
    if Lozinka == ":)":
        Lozinka = ":p"
        basic.show_icon(IconNames.SILLY)
    elif Lozinka == ":p":
        Lozinka = ":("
        basic.show_icon(IconNames.SAD)
    elif Lozinka == ":(":
        Lozinka = ":|"
        basic.show_icon(IconNames.ASLEEP)
    elif Lozinka == ":|":
        Lozinka = ":/"
        basic.show_icon(IconNames.MEH)
    elif Lozinka == ":/":
        Lozinka = ":0"
        basic.show_icon(IconNames.SURPRISED)
    elif Lozinka == ":0":
        Lozinka = ":)"
        basic.show_icon(IconNames.HAPPY)
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

Lozinka = ""
radio.set_group(234)
Lozinka = ":)"
basic.show_icon(IconNames.HAPPY)