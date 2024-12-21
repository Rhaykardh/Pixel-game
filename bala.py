from config import *
class BALA(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao= 1, name = 'sprite/shoot.png', tamanhox= 65, tamanhoy= 65):
        super().__init__()
        self.imagem_entrada= pygame.image.load(name)
        self.image= pygame.transform.scale(self.imagem_entrada, (tamanhox, tamanhoy))
        self.velocidade= 18
        self.x= x
        self.y= y
        self.rect= self.image.get_rect()
        self.rect.topleft= (x,y)
        self.direcao= direcao
    def mover(self):
        self.rect.x += self.velocidade * self.direcao
        if self.rect.left > 800 or self.rect.right < 0:
            self.kill()
        
            

    def desenhar(self, tela):
        tela.blit(self.image, self.rect.topleft)
        
    
    


    