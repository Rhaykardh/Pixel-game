from heroi import *
class INIMIGO(HEROI):
    def __init__(self, x, y, name='sprite/inimigo.png'):
        super().__init__(x,y, name)
    def mover(self):
        self.rect.x -= 3
    



    