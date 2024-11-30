input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onGesture(Gesture.ScreenUp, function () {
    basic.showString("12:00")
    music.play(music.stringPlayable("G F G A - F E D ", 500), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.ScreenDown, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + (input.compassHeading()))
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
})
input.onGesture(Gesture.Shake, function () {
    steps += 1
    basic.showNumber(steps)
})
let steps = 0
steps = 0
