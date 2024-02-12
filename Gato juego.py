import pygame

# Inicializamos el motor de juegos

pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((450,450)) 

# Le ponemos un título a la ventana
pygame.display.set_caption("Gato Asahi")

# Definimos las imágenes
tablero = pygame.image.load('imagenes/tablero.png')
circulo = pygame.image.load('imagenes/circulo.png')
equis= pygame.image.load('imagenes/equis.png')

# Definimos escalas
tablero = pygame.transform.scale( tablero, (450,450))
circulo = pygame.transform.scale( circulo, (125,125))
equis = pygame.transform.scale( equis, (125,125))

# coordenadas elementos

coor = [[(0,0), (0,0), (0,0)],
        [(0,0), (0,0), (0,0)],
        [(0,0), (0,0), (0,0)]]

tablero =  [['','',''],
            ['','',''],
            ['','','']]

# Definimos logica del juego
turno = 'X'
game_over = False
clock = pygame.time.Clock()

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

    screen.blit(tablero, (0, 0))
    screen.blit(circulo, (40,50))
    screen.blit(equis, (160,165))

pygame.display.update()
pygame.quit()

