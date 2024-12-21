from config import *
def tocar_som(nome, loop = 0, volume= 1.0):
    nome = f'musicas/{nome}'
    som = pygame.mixer.Sound(nome)
    som.set_volume(volume)
    canal_live = None
    for canal in range (pygame.mixer.get_num_channels()):
        if not pygame.mixer.Channel(canal).get_busy():
            canal_live = canal
            break
    if canal_live is None:
        canal_live = pygame.mixer.find_channel()
    if canal_live is not None:
        pygame.mixer.Channel(canal_live).play(som, loops= loop)
        canais_usados[nome] = canal_live
