import pygame
pygame.init()

class Janela:
    def __init__(self):
        largura = 500
        altura = 480
        self.Tela = pygame.display.set_mode((500,480))
        nomeJanela = "Primeiro jogo"
        pygame.display.set_caption(nomeJanela)

class Renderizavel:
    def __init__(self,x,y,largura,altura,cor):
        self.x = x; self.y = y; self.largura = largura; self.altura = 20
        self.retangulo = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = cor

    def renderizar(self, tela):
        pygame.draw.rect(tela, self.cor, self.retangulo)

class Jogador(Renderizavel):
    def __init__(self):
        x = 0; y = 0; largura = 20; altura = 20; cor = (255,0,0)
        Renderizavel.__init__(self,x,y,largura,altura, cor)
        self.velocidade = 10

    def atualizaRetangulo(self):
        self.retangulo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, cima, baixo, esq, dir):
        if cima:
            self.y -= self.velocidade
        if baixo:
            self.y += self.velocidade
        if esq:
            self.x -= self.velocidade
        if dir:
            self.x += self.velocidade
        self.atualizaRetangulo()

    def pehX(self):
        return self.x + self.largura/2

    def pehY(self):
        return self.y + self.altura

class Plataforma(Renderizavel):
    def __init__(self, x, y, largura, altura, cor, tela):
        Renderizavel.__init__(self,x,y,largura,altura, cor)
        self.tela = tela
    def renderizar(self):
        Renderizavel.renderizar(self, self.tela)



class Teclado:
    def __init__(self):
        self.keys = pygame.key.get_pressed()

    def escaneiaTeclas(self):
        self.keys = pygame.key.get_pressed()

    def baixo(self):
        return self.keys[pygame.K_DOWN]
    def cima(self):
        return self.keys[pygame.K_UP]
    def esq(self):
        return self.keys[pygame.K_LEFT]
    def dir(self):
        return self.keys[pygame.K_RIGHT]



jogador = Jogador()
janela = Janela()
teclado = Teclado()
plat1 = Plataforma(200,200,100,20,(0,255,0),janela.Tela)

#game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30) #faz o game ficar em 30 FPS

    #pinta a tela toda de preto
    janela.Tela.fill( (0,0,0) )

    teclado.escaneiaTeclas()

    jogador.mover(teclado.cima(), teclado.baixo(), teclado.esq(), teclado.dir())
    jogador.renderizar(janela.Tela)
    plat1.renderizar()
    #atualiza a tela com o que foi desenhado
    pygame.display.update()

    #fecha o jogo caso tenham clicado no X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
