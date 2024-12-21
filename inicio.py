from config import *
class INICIO:
    def __init__(self, tela, font, texto, color):
        self.tela= tela
        self.font = pygame.font.Font(None, font)
        self.texto = self.font.render(texto, True, color)
    def start(self, x, y): 
        self.tela.blit(self.texto, (x//2-self.texto.get_width()//2, y//3))
        
    
    

   

        