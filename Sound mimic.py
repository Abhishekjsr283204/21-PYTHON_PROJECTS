import random
import sys
import time
import os
import pygame

# Initialize pygame
pygame.init()

print('''Sound Mimic, by Abhishek kumar
Try to memorize a pattern of A S D F letters (each with its own sound)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)  # Clear the screen by printing several newlines.

    # Add a random letter to the pattern:
    pattern = pattern + random.choice('ASDF')

    # Display the pattern (and play their sounds):
    print('Pattern: ', end='', flush=True)
    for letter in pattern:
        print(letter, end=' ', flush=True)

        sound_file = os.path.join('.', 'sound' + letter + '.wav')
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        # Wait until the sound finishes playing.
        while pygame.mixer.music.get_busy():
            pass

        # Add a slight pause between sounds.
        time.sleep(0.5)

    time.sleep(1)  # Add a slight pause at the end.
    print('\n' * 60)  # Clear the screen by printing several newlines.

    # Let the player enter the pattern:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        sound_file = os.path.join('.', 'sound' + letter + '.wav')
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        # Wait until the sound finishes playing.
        while pygame.mixer.music.get_busy():
            pass

        # Add a slight pause between sounds.
        time.sleep(0.5)

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)

