from PIL import Image, ImageSequence
import pygame




def load_gif_frames(filepath, width, height, bg_color=(255, 255, 255)):
    frames = []
    img = Image.open(filepath)
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert('RGBA')  # Converte para um formato que o Pygame possa lidar
        pygame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha()
        pygame_image_scaled = pygame.transform.scale(pygame_image, (width, height))
        frames.append(pygame_image_scaled)
    return frames