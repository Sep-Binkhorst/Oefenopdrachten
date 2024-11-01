class Particle:
    def __init__(self, name, spin):
        self.name = name
        self.spin = spin

    def is_up_or_down(self):
            if self.spin >= 0:
                print('up')
            else:
                print('down')

    def flip(self):
            self.spin = -self.spin

proton = Particle('mooi proton', 0.5)
proton.is_up_or_down()
proton.flip()
proton.is_up_or_down()
print(proton.spin)
print(proton.name)
