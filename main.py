radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
my_serial = control.device_serial_number()

name="vote"
vote = 1
def on_received_value(name, number):
    if name == "send" and number == 1:
        def on_button_pressed_a():
            global vote
            vote = (vote+1)%4
            basic.show_number(vote+1)
        input.on_button_pressed(Button.A, on_button_pressed_a)

        def sending():
            radio.send_value("vote", vote+1)
            music.play_tone(Note.C, music.beat(1000))
            radio.send_value("learn", 1)
        input.on_button_pressed(Button.B, sending)
    else:
        pass
radio.on_received_value(on_received_value)

#def on_button_pressed_a():
#    global vote
#    vote = (vote+1)%4
#    basic.show_number(vote+1)
#input.on_button_pressed(Button.A, on_button_pressed_a)

#def sending():
#    radio.send_value("vote", vote+1)
#    music.play_tone(Note.C, music.beat(1000))
#input.on_button_pressed(Button.B, sending)