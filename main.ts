radio.setGroup(69)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
let my_serial = control.deviceSerialNumber()
let name = "vote"
let vote = 1
radio.onReceivedValue(function on_received_value(name: string, number: number) {
    if (name == "send" && number == 1) {
        input.onButtonPressed(Button.A, function on_button_pressed_a() {
            
            vote = (vote + 1) % 4
            basic.showNumber(vote + 1)
        })
        input.onButtonPressed(Button.B, function sending() {
            radio.sendValue("vote", vote + 1)
            music.playTone(Note.C, music.beat(1000))
            radio.sendValue("learn", 1)
        })
    } else {
        
    }
    
})
