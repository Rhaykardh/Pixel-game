from config import *
class RECORDE:
    def __init__(self, name= 'data/recorde.txt'):
        try:
            with open (name, 'r') as arquivo:
                self.pontuação= int(arquivo.read())
        except:
            self.pontuação= 0
    def save(self, score):
        if score > self.pontuação:
            with open ('data/recorde.txt', 'w') as arquivo:
                arquivo.write(str(score))
    def mostrar(self):
        return self.pontuação


    