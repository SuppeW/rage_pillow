import pygame

sounds = ["chickencoop.mp3","where is my team.mp3","whaaat.mp3","goingtobed.mp3"]
soundslen = len(sounds)

pygame.mixer.init()
for i in range (0,soundslen):
    pygame.mixer.music.load(sounds[i])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
