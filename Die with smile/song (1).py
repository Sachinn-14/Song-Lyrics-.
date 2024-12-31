import time
import sys
import pygame
import os
import platform


# Clear the terminal screen
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear screen for Windows
    else:
        os.system("clear")  # Clear screen for Unix/Linux/Mac

clear_terminal()  # Call the function to clear the terminal

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

pygame.mixer.init()

# Specify the music file path
music_file = 'die with you(1).MP3'

# Load the music file
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play()

# Full lyrics of the song
lyrics = """
If the world was ending I'd wanna be next to you...
If the party was over And our time on Earth was through...
I'd wanna hold you just for a while And die with a smile
If the world was ending I'd wanna be next to you❤️
"""

phrases = [
    "If the world was ending",  
    "I'd wanna be next to you...",  
    "If the party was over",  
    "And our time on Earth was through...",  
    "I'd wanna hold you just for a while",  
    "And die with a smile",  
    "If the world was ending",  
    "I'd wanna be next to you❤️"
]

default_speed = 0.067
default_word_delay = 0.3

def print_word(word, speed):
    if word.lower() == "wanna":
        speed = max(0, speed - 0.2)
    if word in ["our", "time", "on", "Earth"]:
        speed = max(0, speed - 0.2)
    if word.endswith("..."):   
        main_word = word[:-3]
        for char in main_word:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        for dot in "...":
            sys.stdout.write(dot)
            sys.stdout.flush()
            time.sleep(3.0 / 3)
        return
    for char in word:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if word.lower() == "die":
        time.sleep(0.87)

for i, phrase in enumerate(phrases):
    words = phrase.split()
    for word in words:
        print_word(word, default_speed)
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(default_word_delay)
    print()
    if phrase == "I'd wanna hold you just for a while":
        time.sleep(0.7)
    if phrase == "And die with a smile":
        time.sleep(1)
    if phrase in ["I'd wanna be next to you...", "And our time on Earth was through..."]:
        time.sleep(0.4)
    if i == 2:
        time.sleep(0.5)

while pygame.mixer.music.get_busy():
    time.sleep(0.1)

print()
