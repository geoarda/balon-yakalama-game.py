import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balon Yakalama")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font settings
font = pygame.font.SysFont(None, 40)

# Game variables
score = 0
time_limit = 500  # Increased time limit
start_ticks = pygame.time.get_ticks()

# Balloon properties
balloon_radius = 30
balloon_x = random.randint(balloon_radius, WIDTH - balloon_radius)
balloon_y = random.randint(balloon_radius, HEIGHT - balloon_radius)
balloon_speed = 2

# Difficulty level (speed increase)
speed_increment = 0.5

# Game status
game_over = False

def draw_text(text, x, y, color=BLACK, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(img, rect)

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Time control
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, time_limit - seconds_passed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # Balloon click control
            dist = ((mx - balloon_x) ** 2 + (my - balloon_y) ** 2) ** 0.5
            if dist <= balloon_radius:
                score += 1
                balloon_x = random.randint(balloon_radius, WIDTH - balloon_radius)
                balloon_y = random.randint(balloon_radius, HEIGHT - balloon_radius)
                balloon_speed += speed_increment  # speed increases

    # Move the balloon (choose a random direction and move)
    direction = random.choice(['left', 'right', 'up', 'down'])
    if direction == 'left':
        balloon_x -= balloon_speed
    elif direction == 'right':
        balloon_x += balloon_speed
    elif direction == 'up':
        balloon_y -= balloon_speed
    elif direction == 'down':
        balloon_y += balloon_speed

    # Limit the balloon so it doesn't go off the screen
    if balloon_x < balloon_radius:
        balloon_x = balloon_radius
    elif balloon_x > WIDTH - balloon_radius:
        balloon_x = WIDTH - balloon_radius
    if balloon_y < balloon_radius:
        balloon_y = balloon_radius
    elif balloon_y > HEIGHT - balloon_radius:
        balloon_y = HEIGHT - balloon_radius

    # If time runs out, the game ends
    if time_left <= 0:
        print(f"Oyun Bitti! Toplam Skor: {score}")
        pygame.quit()
        sys.exit()

    # Draw the balloon
    pygame.draw.circle(screen, RED, (int(balloon_x), int(balloon_y)), balloon_radius)

    # Print score and time
    draw_text(f"Skor: {score}", 10, 10)
    draw_text(f"Süre: {int(time_left)}", 10, 50)

    pygame.display.flip()
    clock.tick(60)
