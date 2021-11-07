input.onButtonPressed(Button.A, function () {
    radio.sendString(Lozinka)
})
input.onButtonPressed(Button.B, function () {
    if (Lozinka == ":)") {
        Lozinka = ":p"
        basic.showIcon(IconNames.Silly)
    } else if (Lozinka == ":p") {
        Lozinka = ":("
        basic.showIcon(IconNames.Sad)
    } else if (Lozinka == ":(") {
        Lozinka = ":|"
        basic.showIcon(IconNames.Asleep)
    } else if (Lozinka == ":|") {
        Lozinka = ":/"
        basic.showIcon(IconNames.Meh)
    } else if (Lozinka == ":/") {
        Lozinka = ":0"
        basic.showIcon(IconNames.Surprised)
    } else if (Lozinka == ":0") {
        Lozinka = ":)"
        basic.showIcon(IconNames.Happy)
    } else {
    	
    }
})
let Lozinka = ""
Lozinka = ":)"
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
