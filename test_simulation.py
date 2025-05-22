import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, VelocityBodyYawspeed)
import pygame



class Button():
    """
    
    """
    def __init__(self, place, x, y, bWidth, bHeight, text):
        self.place = place     # élément dans lequel apparait le bouton
        self.x = x             # position d'apparition en x (coin superieur gauche)
        self.y = y             # position d'apparition en y (coin superieur gauche)
        self.bWidth = bWidth   # largeur du bouton
        self.bHeight = bHeight # hauteur du bouton
        self.text = text       # texte écrit sur le bouton

        # Initialisation pygame
        pygame.init()

        # BUTTON  
        self.color_light = (170,170,170) # gris clair
        self.color_dark = (100,100,100)  # gris foncé

        # FONT
        self.smallfont = pygame.font.SysFont('Corbel', 35) # paramètres de la police
        self.font_color = (255,255,255)                    # couleur du texte : blanc

    def button_drawing(self):
        """ Fonction qui dessine le bouton """
        pygame.draw.rect(self.place, self.color_dark, [self.x, self.y, self.bWidth, self.bHeight])

    def change_color(self):
        """ Version gris clair du bouton (quuand la touche correspondante est appuyée) """
        pygame.draw.rect(self.place, self.color_light, [self.x, self.y, self.bWidth, self.bHeight])


pygame.init()

pas=300
# WINDOW
width, height = 1300, 720                         # taille de la fenêtre
screen = pygame.display.set_mode((width, height)) # affichage de la fenêtre
screen.fill((0,0,0))                              # couleur du background : noir

# FONTS
smallfont = pygame.font.SysFont('Calibri', 18)         # police 1 : calibri taille 18
smallfont2 = pygame.font.SysFont('Corbel', 20, 'bold') # police 2 : corbel taille 20 gras
font_color = (235,235,235) 
font_color2 = (96,96,96) 
font_red = (255,0,0)
font_green = (0,255,0)
font_blue = (0,0,255)
font_purple = (155,38,182)

# TEXTS
# Creation des textes pour les boutons 
## battery
text_battery = smallfont2.render('BATTERY', True , font_color2)
text_temperature = smallfont2.render('Temperature : ', True , font_color)
text_voltage = smallfont2.render('Voltage            : ', True , font_color)
text_percentage = smallfont2.render('Percentage    : ', True , font_color)
text_percentage_dynamic = smallfont.render('0', True , font_color)
text_temperature_dynamic = smallfont.render('0', True , font_color)
text_voltage_dynamic = smallfont.render('0', True , font_color)
## speed
text_speed = smallfont2.render('SPEED', True , font_color2)
text_speed_north = smallfont2.render('North  : ', True , font_red)
text_speed_east = smallfont2.render('East     : ', True , font_green)
text_speed_down = smallfont2.render('Down  : ', True , font_blue)
text_speed_north_dynamic = smallfont.render('-10.25', True , font_color)
text_speed_east_dynamic = smallfont.render('0', True , font_color)
text_speed_down_dynamic = smallfont.render('0', True , font_color)

#cam
text_cam = smallfont2.render('CAM FLUIDE',True, font_color)
text_cam_traitement= smallfont2.render('CAM TRAITEMENT' , True , font_color)
screen.blit(text_cam, (800, 300))
screen.blit(text_cam_traitement, (200, 600))


## buttons
text_c = smallfont2.render('C', True , font_color)
text_b = smallfont2.render('B', True , font_color)
text_n = smallfont2.render('N', True , font_color)
text_p = smallfont2.render('P', True , font_color)
image_fleche_up = pygame.image.load('arrows/fleche_up.png') 
image_fleche_left = pygame.image.load('arrows/fleche_left.png') 
image_fleche_down = pygame.image.load('arrows/fleche_down.png') 
image_fleche_right = pygame.image.load('arrows/fleche_right.png') 
image_logo = pygame.image.load('arrows/Logo_Scrypt_Carre_Blanc.png')

colorBarres = (255,255,255) # couleur des lignes : blanc
colorFrames = (192,192,192) # couleur des cases de titre : gris clair

# BARRES
## horizontales
pygame.draw.rect(screen, colorBarres, [0, 100, 1300, 2])
pygame.draw.rect(screen, colorBarres, [300+pas, 570, 700, 2])
pygame.draw.rect(screen, colorBarres, [0, 244, 300+pas, 2])
pygame.draw.rect(screen, colorBarres, [0, 388, 300+pas, 2])
## verticale
pygame.draw.rect(screen, colorBarres, [300+pas, 100, 2, 620])
pygame.draw.rect(screen, colorBarres, [300, 100, 2, 290])

# Frames infos
## battery
pygame.draw.rect(screen, colorFrames, [0, 102, 300, 33])
## speed
pygame.draw.rect(screen, colorFrames, [0, 246, 300, 33])


# BUTTONS
## space
space_button = Button(screen, 325+pas, 645, 355, 50, "")
## C, B, N
c_button = Button(screen, 325+pas, 590, 85, 50, "")
b_button = Button(screen, 415+pas, 590, 85, 50, "")
n_button = Button(screen, 505+pas, 590, 85, 50, "")
p_button = Button(screen, 595+pas, 590, 85, 50, "")
## ↑, ←, ↓, →
up_button = Button(screen, 805+pas, 590, 85, 50, "")
left_button = Button(screen, 715+pas, 645, 85, 50, "")
down_button = Button(screen, 805+pas, 645, 85, 50, "")
right_button = Button(screen, 895+pas, 645, 85, 50, "")
## drawing
space_button.button_drawing()
c_button.button_drawing()
b_button.button_drawing()
n_button.button_drawing()
p_button.button_drawing()
up_button.button_drawing()
down_button.button_drawing()
left_button.button_drawing()
right_button.button_drawing()

# TEXTS PLOTS
## logo
screen.blit(image_logo, (1190, 10))
## battery
screen.blit(text_battery, (109, 109))
screen.blit(text_temperature, (20, 147))
screen.blit(text_voltage, (20, 177))
screen.blit(text_percentage, (20, 207))
screen.blit(text_temperature_dynamic, (150, 147))
screen.blit(text_voltage_dynamic, (150, 177))
screen.blit(text_percentage_dynamic, (150, 207))
## speed
screen.blit(text_speed, (112, 253))
screen.blit(text_speed_north, (20, 291))
screen.blit(text_speed_east, (20, 321))
screen.blit(text_speed_down, (20, 351))
screen.blit(text_speed_north_dynamic, (100, 291))
screen.blit(text_speed_east_dynamic, (100, 321))
screen.blit(text_speed_down_dynamic, (100, 351))

## buttons
screen.blit(text_c, (360+pas, 605))
screen.blit(text_b, (450+pas, 605))
screen.blit(text_n, (540+pas, 605))
screen.blit(text_p, (630+pas, 605))
screen.blit(image_fleche_up, (827+pas, 598))
screen.blit(image_fleche_down, (828+pas, 650))    
screen.blit(image_fleche_left, (737+pas, 650))
screen.blit(image_fleche_right, (917+pas, 650))

# BARRES 
## battery
pygame.draw.rect(screen, (192,192,192), [185, 207, 100, 15]) # percentage
## speed
pygame.draw.rect(screen, (192,192,192), [160, 291, 125, 15]) # north
pygame.draw.rect(screen, (192,192,192), [160, 321, 125, 15]) # east
pygame.draw.rect(screen, (192,192,192), [160, 351, 125, 15]) # down

pygame.display.set_caption("Drone Control")
pygame.display.update()

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Connexion au drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Drone connecté !")
            break
        elif state.is_connected is False:
            print("-- Échec de la connexion au drone.")
            return

    print("Attente du GPS...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Position GPS OK")
            break
        elif not health.is_global_position_ok or not health.is_home_position_ok:
            print("-- Position GPS non disponible.")
            return

    # Passer en mode GUIDED avant d'armer
    await asyncio.sleep(2)  # Petite pause pour assurer le changement de mode

    print("Armement...")
    try:
        await drone.action.arm()
    except Exception as e:
        print(f"Erreur d'armement : {e}")
        return

    await asyncio.sleep(2)  # Petite pause pour éviter un refus de décollage

    print("Décollage...")
    await drone.action.takeoff()
    await asyncio.sleep(5)  # Laisse le temps au drone de monter

    # Vérifier si le drone a bien décollé
    async for position in drone.telemetry.position():
        if position.relative_altitude_m > 1.0:  # Vérifie si le drone est bien en l'air
            print("-- Drone en vol")
            break

    
    print("Démarrage du mode offboard...")
    try:
        await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
        await drone.offboard.start()
        print("-- Mode Offboard démarré")
    except OffboardError as error:
        print(f"Erreur lors du démarrage du mode Offboard : {error._result.result}")
        await drone.action.land()
        return
    print("Démarrage du mode offboard...")
    try:
        await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
        await drone.offboard.start()
        print("-- Mode Offboard démarré")
    except OffboardError as error:
        print(f"Erreur lors du démarrage du mode Offboard : {error._result.result}")
        await drone.action.land()
        return

# Variables pour accumuler les vitesses
    forward_speed = 0.0
    right_speed = 0.0
    down_speed = 0.0
    yawspeed = 0.0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("-- Atterrissage")
                    p_button.change_color()
                    screen.blit(text_p, (630+pas, 605))
                    await drone.action.land()
                    run = False
                
                elif event.key == pygame.K_UP:                    
                    print("-- Avancer")
                    up_button.change_color()
                    forward_speed = 1.0
                    screen.blit(image_fleche_up, (827+pas, 598)
                    )
                elif event.key == pygame.K_DOWN:
                    print("-- Reculer")
                    down_button.change_color()
                    forward_speed = -1.0
                    screen.blit(image_fleche_down, (828+pas, 650)
                    )
                elif event.key == pygame.K_s:
                    print("-- Stop")

                elif event.key == pygame.K_LEFT:
                    print("-- Gauche")
                    left_button.change_color()
                    right_speed = -1.0
                    screen.blit(image_fleche_left, (737+pas, 650)
                    )
                elif event.key == pygame.K_RIGHT:
                    print("-- Droite")
                    right_button.change_color()
                    right_speed = 1.0
                    screen.blit(image_fleche_right, (917+pas, 650)
                    )
                elif event.key == pygame.K_SPACE:
                    print("-- Monter")
                    down_speed = -1.0
                    space_button.change_color()

                elif event.key == pygame.K_c:
                    print("-- Descendre")
                    c_button.change_color()
                    down_speed = 1.0
                    screen.blit(text_c, (360+pas, 605)
                    )
                elif event.key == pygame.K_n:
                    print("-- Rotation droite")
                    n_button.change_color()
                    yawspeed = 100.0
                    screen.blit(text_n, (540+pas, 605)
                    )
                elif event.key == pygame.K_b:
                    print("-- Rotation gauche")
                    b_button.change_color()
                    yawspeed = -100.0
                    screen.blit(text_b, (450+pas, 605)
                    )

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up_button.button_drawing()
                    forward_speed = 0.0
                    screen.blit(image_fleche_up, (827+pas, 598)
                    )
                elif event.key == pygame.K_DOWN:
                    down_button.button_drawing()
                    forward_speed = 0.0
                    screen.blit(image_fleche_down, (828+pas, 650)
                    )
                elif event.key == pygame.K_LEFT:
                    left_button.button_drawing()
                    right_speed = 0.0
                    screen.blit(image_fleche_left, (737+pas, 650)
                    )
                elif event.key == pygame.K_RIGHT:
                    right_button.button_drawing()
                    right_speed = 0.0
                    screen.blit(image_fleche_right, (917+pas, 650)
                    )
                elif event.key == pygame.K_SPACE:
                    down_speed = 0.0
                    space_button.button_drawing()

                elif event.key == pygame.K_c:
                    c_button.button_drawing()
                    down_speed = 0.0
                    screen.blit(text_c, (360+pas, 605)
                    )
                elif event.key == pygame.K_n:
                    n_button.button_drawing()
                    yawspeed = 0.0
                    screen.blit(text_n, (540+pas, 605)
                    )
                elif event.key == pygame.K_b:
                    b_button.button_drawing()
                    yawspeed = 0.0
                    screen.blit(text_b, (450+pas, 605)
                    )

# Envoi de la commande de vitesse combinée
            await drone.offboard.set_velocity_body(
                VelocityBodyYawspeed(forward_speed, right_speed, down_speed, yawspeed)
            )
        pygame.display.update()
    print("-- Drone posé.")

async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return

if __name__ == "__main__":
    asyncio.run(run())