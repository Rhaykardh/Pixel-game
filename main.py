from config import *
from heroi import *
from bala import *
from inimigo import *
from carga import *
from musica import *
from inicio import *
from vida import *
from recorde import *
from ambiente import *
from desenhar import *
from boss import *
import sys
def main():
    pygame.init()
    largura= 800
    altura= 600
    tela= pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Aventura')
    kill_counter= 0
    rodando= True
    esperando = True
    ambiente= AMBIENTE()
    background= AMBIENTE('sprite/background.png')
    bosses= pygame.sprite.Group()
    boss= None
    Hp= 3
    vidas=pygame.sprite.Group()
    titulo= DESENHAR(250, 90, name= 'sprite/titulo.png')
    pontos= 0
    cargas= pygame.sprite.Group()
    heroi= HEROI(100, altura//2)
    inimigos= pygame.sprite.Group()
    all_sprites= pygame.sprite.LayeredUpdates()
    all_sprites.add(heroi)
    tocar_som('ambiente.mp3', loop= -1, volume= 0.5)
    background.desenhar(tela) 
    inicio= INICIO(tela= tela, font= 65, texto= 'CLICK EM ESPAÇO', color= ROXO)
    inicio.start(altura* 1.3, 450* 3) 
    titulo.desenhar(tela)
    pygame.display.flip()
    coldown= 0
    coldown1= 0
    record= RECORDE()
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_SPACE:
                    esperando= False
    tocar_som('inicio.mp3', volume= 7.0)                
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                rodando= False
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_q:
                    if heroi.blast():
                        tocar_som('especial.mp3')
                    

                if evento.key== pygame.K_z:
                    heroi.disparo()
                    tocar_som('bala.mp3')
                    
        coldown += 1
        if coldown > random.randint(30, 100):
            if random.randint(1, 100) <= 2:
                carga= CARGA(largura, random.randint(0, altura - 50))
                cargas.add(carga)
                all_sprites.add(carga)
            
        coldown1 += 1
        if coldown1 > random.randint(30, 100):
            if random.randint(1, 780) <= 2:
                vida= VIDA(largura, random.randint(0, altura - 50))
                vidas.add(vida)
                all_sprites.add(vida)


        if kill_counter >= 50:
            if len(bosses) == 0:
               if random.randint(1, 100) <= 5:
                boss= BOSS(50, 50, largura  -250, random.randint(100, altura - 100), tamanhox = 275, tamanhoy= 275)
                bosses.add(boss)
                all_sprites.add(boss)
                for inimigo in inimigos:
                    inimigo.kill() 
        else: 
            if random.randint(1, 100) <= 5:
                inimigo= INIMIGO(largura, random.randint(0, altura - 50))
                inimigos.add(inimigo)
                all_sprites.add(inimigo)
        
        
       
        
        
        for bala in heroi.balas:  
            bateu = pygame.sprite.spritecollide(bala, inimigos, True)
            if bateu:
                tocar_som('inimigo.mp3', volume= 0.5)
                heroi.balas.remove(bala)
                pontos += 1
                bala.kill()  
                kill_counter += 1
            bateu_boss= pygame.sprite.spritecollide(bala, bosses, False)
            if bateu_boss:
                heroi.balas.remove(bala)
                bala.kill()
                for chefe in bosses:
                    chefe.vida -= 1
                    if chefe.vida <= 0:
                        kill_counter = 0
                        pontos += chefe.pontos
                        bosses.remove(chefe)
                        chefe.kill()
                        


            


        
        for blast in heroi.blasts:  
            bateu = pygame.sprite.spritecollide(blast, inimigos, True)
            if bateu:  
                pontos += 1
                kill_counter += 1
            bateu_boss= pygame.sprite.spritecollide(blast, bosses, False)
            if bateu_boss:
                heroi.blasts.remove(blast)
                blast.kill()
                for chefe in bosses:
                    chefe.vida -= 5
                    if chefe.vida <= 0:
                        pontos += chefe.pontos
                        bosses.remove(chefe)
                        chefe.kill()
                        kill_counter = 0
               
                
           
        if pygame.sprite.spritecollide(heroi, inimigos, True): 
            tocar_som('inimigo.mp3', volume= 0.5)
            Hp -= 1
            pontos += 1  
            kill_counter += 1
         
            if Hp <=0:
                rodando= False

        
        if pygame.sprite.spritecollide(heroi, cargas, True):
            tocar_som('pick-up.mp3')
            if heroi.carga != 100:
                heroi.carga += 25

        if pygame.sprite.spritecollide(heroi, vidas, True):
            if Hp < 5:
                Hp += 1 

        if pygame.sprite.spritecollide(heroi, bosses, False): 
            tocar_som('inimigo.mp3', volume= 0.5)
            boss.vida -= 1
            if boss.vida <= 0:
                kill_counter = 0
                pontos += boss.pontos
                boss.kill()
                boss= None
                
        for chefe in bosses:
            for bala in chefe.balas:  
                bateu = pygame.sprite.spritecollide(heroi, chefe.balas, False)
                if bateu:
                    chefe.balas.remove(bala)
                    Hp -= 1
                    bala.kill()  
                    if Hp <= 0:
                        rodando= False

        ambiente.mover()

        for inimigo in inimigos:
            inimigo.mover()
            
        for carga in cargas:
            carga.mover()

        for blast in heroi.blasts:
            blast.mover()


        for tiro in heroi.balas:
            tiro.mover()

        for vida in vidas:
            vida.mover()
        
        for chefao in bosses:
            chefao.mover()
            for bala in chefao.balas:
                bala.mover()




        ambiente.desenhar(tela)


        all_sprites.draw(tela)

        teclas= pygame.key.get_pressed()

        recorde= INICIO(tela, font= 34, texto= f'recorde= {record.mostrar()}', color= VERMELHO)
        heroi.mover(teclas)
        score = INICIO(tela, font= 34, texto= f'pontuação= {pontos}', color= ROXO)
        score.start(150, 10)
        heroi.desenhar(tela)
        life= INICIO(tela, font= 34, texto= f'life= {Hp}', color= ROXO)
        life.start(70,80)
        energia= INICIO(tela, font= 34, texto= f'energia= {heroi.carga}', color= ROXO)
        energia.start(150, 150)
        recorde.start(150, 200)
        
       

        for chefao in bosses:
            chefao.desenhar(tela)
            for bala in chefao.balas:
                bala.desenhar(tela)
        
        for vida in vidas:
            vida.desenhar(tela)

        for carga in cargas:
            carga.desenhar(tela)

        for bala in heroi.balas:
            bala.desenhar(tela)
           
        for inimigo in inimigos:
            inimigo.desenhar(tela)

        for blast in heroi.blasts:
            blast.desenhar(tela)


        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    record.save(pontos)
    tela.fill(PRETO)
    morte= AMBIENTE('sprite/gameover.jpg')
    morte.desenhar(tela)
    gameover=INICIO(tela= tela, font= 65, texto= 'VOCÊ PERDEU', color= VERMELHO)
    gameover.start(altura* 1.3, 450* 3)
    resultado=INICIO(tela= tela, font= 65, texto= 'voce conseguiu: {}'.format(pontos), color= VERMELHO)
    resultado.start(altura* 1.3, 450)
    pygame.mixer.stop()
    tocar_som('morte.mp3')
    pygame.display.flip()
    pygame.time.wait(1000*5)
    pygame.mixer.stop()    
if __name__== "__main__":
   while True:
       main()
