from gamepadshift import GamePadShift

class BetterPad():
    def __init__(self, clk, out, latch, buttons = {0: "b", 1: "a", 2: "start", 3: "select"}, *args, **kwargs):
        self._pad = GamePadShift(clk, out, latch, *args, **kwargs)
        self._buttons = buttons
    def getPressed(self):
        pressed = self._pad.get_pressed()
        output = {}
        for x in range(0, len(self._buttons)):
            output[self._buttons[x]] = pressed & 1 << x != 0
        none = True
        for x in output:
            if output[x]:
                none = False
        output["none"] = none
        return output
