# sound.py
import pygame

# Initialize the mixer
pygame.mixer.init()

def load_and_play_city_sound():
    """
    Loads and plays the city ambient sound in a loop.
    """
    # Load the city/ambient sound (replace with your own sound file)
    city_sound = pygame.mixer.Sound("./src/sound/citysound.wav")
    
    # Play the city sound in a loop
    city_sound.play(loops=-1, maxtime=0)  # Loop indefinitely
    
    return city_sound

def stop_sound(city_sound):
    """
    Stops the sound that is currently playing.
    """
    city_sound.stop()
