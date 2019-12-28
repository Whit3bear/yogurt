class Lamp():
    def __init__(self, color):
        self.color = color
        self.on = False
    def toggle_switch(self):
        self.on = not self.on
    def state(self):
        return "The lamp is on." if self.on else "The lamp is off."

my_lamp = Lamp("Blue")
print(my_lamp.color)
#"Blue"
print(my_lamp.on)
#False
print(my_lamp.state())
#"The lamp is off."
# now switch it on
my_lamp.toggle_switch()
print(my_lamp.state())
#"The lamp is on.")