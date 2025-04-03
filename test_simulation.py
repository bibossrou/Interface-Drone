import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, VelocityBodyYawspeed)
import pygame

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drone Control")

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

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("-- Atterrissage")
                    await drone.action.land()
                    run = False

    print("-- Drone posé.")

async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return

if __name__ == "__main__":
    asyncio.run(run())
