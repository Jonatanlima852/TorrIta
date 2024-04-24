from PIL import Image, ImageSequence
import pygame

def remove_background(frame, bg_color):
    """Remove o background de um frame PIL baseado na cor especificada."""
    data = frame.getdata()
    new_data = []
    for item in data:
        # Comparando a cor do pixel com a cor do background
        if item[:3] == bg_color[:3]:  # Ignora o canal alpha
            new_data.append((255, 255, 255, 0))  # Totalmente transparente
        else:
            new_data.append(item)
    frame.putdata(new_data)
    return frame

# def load_gif_frames(filepath, width, height):
#     frames = []
#     img = Image.open(filepath)
#     for frame in ImageSequence.Iterator(img):
#         frame = frame.convert('RGBA')  # Converte para um formato que o Pygame possa lidar
#         pygame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha()
#         pygame_image_scaled = pygame.transform.scale(pygame_image, (width, height))
#         frames.append(pygame_image_scaled)
#     return frames


def load_gif_frames(filepath, width, height, bg_color=(255, 255, 255)):
    frames = []
    img = Image.open(filepath)
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert('RGBA')  # Converte para um formato que o Pygame possa lidar
        # frame = remove_background(frame, bg_color)  # Remove o background antes de redimensionar

        # # Redimensiona a imagem mantendo a proporção
        # original_width, original_height = frame.size
        # ratio = min(target_width / original_width, target_height / original_height)
        # new_size = (int(original_width * ratio), int(original_height * ratio))
        # frame = frame.resize(new_size, Image.ANTIALIAS)
        
        pygame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha()

        # # Centraliza se necessário
        # if new_size[0] != target_width or new_size[1] != target_height:
        #     new_surface = pygame.Surface((target_width, target_height), pygame.SRCALPHA, 32).convert_alpha()
        #     new_surface.fill((0,0,0,0))  # Preenche com transparente
        #     x_offset = (target_width - new_size[0]) // 2
        #     y_offset = (target_height - new_size[1]) // 2
        #     new_surface.blit(pygame_image, (x_offset, y_offset))
        #     pygame_image = new_surface

        pygame_image_scaled = pygame.transform.scale(pygame_image, (width, height))
        frames.append(pygame_image_scaled)
    return frames