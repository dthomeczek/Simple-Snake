import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors for different themes
theme1 = {'background': (255, 255, 255), 'snake': (0, 255, 0), 'food': (255, 0, 0), 'text': (0, 0, 0)}
theme2 = {'background': (0, 0, 0), 'snake': (0, 255, 0), 'food': (255, 0, 0), 'text': (255, 255, 255)}
current_theme = theme1  # Default theme

# Set up the snake
snake = [(100, 50), (90, 50), (80, 50)]
snake_dir = (1, 0)  # Initial direction (right)
last_dir = snake_dir

# Set up the food
food = (random.randint(0, (width-10)//10) * 10, random.randint(0, (height-10)//10) * 10)

# Set up the score
score = 0

# Set up the high score
high_score = 0
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

# Set up the game settings
difficulty_settings = {
    'easy': {'speed': 10},
    'medium': {'speed': 15},
    'hard': {'speed': 20}
}
wrap_around = True


# Set up the font
font = pygame.font.Font(None, 24)

# Set up the clock
clock = pygame.time.Clock()

# Set up the start menu
def start_menu(current_difficulty='easy'):
    menu_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(current_theme['background'])

        title_text = menu_font.render("Snake Game", True, current_theme['text'])
        title_rect = title_text.get_rect(center=(width // 2, height // 6))
        screen.blit(title_text, title_rect)

        start_button = pygame.Rect((width // 2 - 75, height // 4, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], start_button)
        start_text = font.render("Start Game", True, current_theme['background'])
        start_text_rect = start_text.get_rect(center=start_button.center)

        options_button = pygame.Rect((width // 2 - 75, height // 4 + 60, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], options_button)
        options_text = font.render("Options", True, current_theme['background'])
        options_text_rect = options_text.get_rect(center=options_button.center)

        quit_button = pygame.Rect((width // 2 - 75, height // 4 + 120, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], quit_button)
        quit_text = font.render("Quit Game", True, current_theme['background'])
        quit_text_rect = quit_text.get_rect(center=quit_button.center)

        # Display current difficulty in the top right corner
        if current_difficulty is not None:
            difficulty_text = menu_font.render(f"Difficulty: {current_difficulty.capitalize()}", True, current_theme['text'])
        else:
            difficulty_text = menu_font.render("Difficulty: None", True, current_theme['text'])
        difficulty_rect = difficulty_text.get_rect(topright=(width - 20, 20))
        screen.blit(difficulty_text, difficulty_rect)

        # Highlight buttons when mouse hovers over them
        mouse_pos = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), start_button, border_radius=5)
        if options_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), options_button, border_radius=5)
        if quit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), quit_button, border_radius=5)

        screen.blit(start_text, start_text_rect)
        screen.blit(options_text, options_text_rect)
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return current_difficulty  # Return the selected difficulty
                elif options_button.collidepoint(event.pos):
                    current_difficulty = options_menu(current_difficulty)  # Update current_difficulty based on options menu
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        clock.tick(5)

# Set up the options menu
def options_menu(current_difficulty):
    global wrap_around  # Declare global variable

    menu_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(current_theme['background'])

        title_text = menu_font.render("Options", True, current_theme['text'])
        title_rect = title_text.get_rect(center=(width // 2, height // 6))
        screen.blit(title_text, title_rect)

        themes_button = pygame.Rect((width // 2 - 75, height // 4, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], themes_button)
        themes_text = font.render("Themes", True, current_theme['background'])
        themes_text_rect = themes_text.get_rect(center=themes_button.center)

        difficulty_button = pygame.Rect((width // 2 - 75, height // 4 + 60, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], difficulty_button)
        difficulty_text = font.render("Difficulty", True, current_theme['background'])
        difficulty_text_rect = difficulty_text.get_rect(center=difficulty_button.center)

        wrap_around_button = pygame.Rect((width // 2 - 75, height // 4 + 120, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], wrap_around_button)
        wrap_around_text = font.render(f"Wrap Around: {'On' if wrap_around else 'Off'}", True, current_theme['background'])
        wrap_around_text_rect = wrap_around_text.get_rect(center=wrap_around_button.center)

        back_button = pygame.Rect((width // 2 - 75, height // 4 + 180, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], back_button)
        back_text = font.render("Back", True, current_theme['background'])
        back_text_rect = back_text.get_rect(center=back_button.center)

        # Highlight buttons when mouse hovers over them
        mouse_pos = pygame.mouse.get_pos()
        if themes_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), themes_button, border_radius=5)
        if difficulty_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), difficulty_button, border_radius=5)
        if wrap_around_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), wrap_around_button, border_radius=5)
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), back_button, border_radius=5)

        screen.blit(themes_text, themes_text_rect)
        screen.blit(difficulty_text, difficulty_text_rect)
        screen.blit(wrap_around_text, wrap_around_text_rect)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if themes_button.collidepoint(event.pos):
                    themes_menu()
                elif difficulty_button.collidepoint(event.pos):
                    current_difficulty = difficulty_menu(current_difficulty)  # Get the selected difficulty
                elif wrap_around_button.collidepoint(event.pos):
                    wrap_around = not wrap_around
                elif back_button.collidepoint(event.pos):
                    return current_difficulty  # Return the selected difficulty

        clock.tick(5)

# Set up the difficulty menu
def difficulty_menu(current_difficulty):
    menu_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(current_theme['background'])

        title_text = menu_font.render("Difficulty", True, current_theme['text'])
        title_rect = title_text.get_rect(center=(width // 2, height // 6))
        screen.blit(title_text, title_rect)

        easy_button = pygame.Rect((width // 2 - 75, height // 4, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], easy_button)
        easy_text = font.render("Easy", True, current_theme['background'])
        easy_text_rect = easy_text.get_rect(center=easy_button.center)

        medium_button = pygame.Rect((width // 2 - 75, height // 4 + 60, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], medium_button)
        medium_text = font.render("Medium", True, current_theme['background'])
        medium_text_rect = medium_text.get_rect(center=medium_button.center)

        hard_button = pygame.Rect((width // 2 - 75, height // 4 + 120, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], hard_button)
        hard_text = font.render("Hard", True, current_theme['background'])
        hard_text_rect = hard_text.get_rect(center=hard_button.center)

        back_button = pygame.Rect((width // 2 - 75, height // 4 + 180, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], back_button)
        back_text = font.render("Back", True, current_theme['background'])
        back_text_rect = back_text.get_rect(center=back_button.center)

        # Highlight buttons when mouse hovers over them
        mouse_pos = pygame.mouse.get_pos()
        if easy_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), easy_button, border_radius=5)
        if medium_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), medium_button, border_radius=5)
        if hard_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), hard_button, border_radius=5)
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), back_button, border_radius=5)

        screen.blit(easy_text, easy_text_rect)
        screen.blit(medium_text, medium_text_rect)
        screen.blit(hard_text, hard_text_rect)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return 'easy'
                elif medium_button.collidepoint(event.pos):
                    return 'medium'
                elif hard_button.collidepoint(event.pos):
                    return 'hard'
                elif back_button.collidepoint(event.pos):
                    return current_difficulty

        clock.tick(5)

# Set up the themes menu
def themes_menu():
    global current_theme

    menu_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(current_theme['background'])

        title_text = menu_font.render("Themes", True, current_theme['text'])
        title_rect = title_text.get_rect(center=(width // 2, height // 6))
        screen.blit(title_text, title_rect)

        theme1_button = pygame.Rect((width // 2 - 75, height // 4, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], theme1_button)
        theme1_text = font.render("Theme 1", True, current_theme['background'])
        theme1_text_rect = theme1_text.get_rect(center=theme1_button.center)

        theme2_button = pygame.Rect((width // 2 - 75, height // 4 + 60, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], theme2_button)
        theme2_text = font.render("Theme 2", True, current_theme['background'])
        theme2_text_rect = theme2_text.get_rect(center=theme2_button.center)

        back_button = pygame.Rect((width // 2 - 75, height // 4 + 120, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], back_button)
        back_text = font.render("Back", True, current_theme['background'])
        back_text_rect = back_text.get_rect(center=back_button.center)

        # Highlight buttons when mouse hovers over them
        mouse_pos = pygame.mouse.get_pos()
        if theme1_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), theme1_button, border_radius=5)
        if theme2_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), theme2_button, border_radius=5)
        if back_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), back_button, border_radius=5)

        screen.blit(theme1_text, theme1_text_rect)
        screen.blit(theme2_text, theme2_text_rect)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if theme1_button.collidepoint(event.pos):
                    current_theme = theme1
                elif theme2_button.collidepoint(event.pos):
                    current_theme = theme2
                elif back_button.collidepoint(event.pos):
                    return

        clock.tick(5)

# Set up the end screen
def end_screen(score):
    menu_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(current_theme['background'])

        end_text = menu_font.render("Game Over!", True, current_theme['text'])
        end_rect = end_text.get_rect(center=(width // 2, height // 6))
        screen.blit(end_text, end_rect)

        score_text = menu_font.render(f"Score: {score}", True, current_theme['text'])
        score_rect = score_text.get_rect(center=(width // 2, height // 3))
        screen.blit(score_text, score_rect)

        restart_button = pygame.Rect((width // 2 - 75, height // 2, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], restart_button)
        restart_text = font.render("Restart?", True, current_theme['background'])
        restart_text_rect = restart_text.get_rect(center=restart_button.center)

        main_menu_button = pygame.Rect((width // 2 - 75, height // 2 + 60, 150, 40))
        pygame.draw.rect(screen, current_theme['text'], main_menu_button)
        main_menu_text = font.render("Main Menu", True, current_theme['background'])
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button.center)

        # Highlight buttons when mouse hovers over them
        mouse_pos = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), restart_button, border_radius=5)
        if main_menu_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (200, 200, 200), main_menu_button, border_radius=5)

        screen.blit(restart_text, restart_text_rect)
        screen.blit(main_menu_text, main_menu_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                elif main_menu_button.collidepoint(event.pos):
                    return "main_menu"

        clock.tick(5)

current_difficulty = 'easy'  # Define current_difficulty before the loop begins

# Main game loop
while True:
    current_difficulty = start_menu(current_difficulty)  # Get the selected difficulty from the start menu

    # Reset snake and other game variables after theme and difficulty selection
    snake = [(100, 50), (90, 50), (80, 50)]
    snake_dir = (1, 0)
    last_dir = snake_dir
    food = (random.randint(0, (width - 10) // 10) * 10, random.randint(0, (height - 10) // 10) * 10)
    score = 0

    # Set the snake speed based on difficulty
    snake_speed = difficulty_settings[current_difficulty]['speed']

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and last_dir != (0, 1):
                    snake_dir = (0, -1)
                elif event.key == pygame.K_DOWN and last_dir != (0, -1):
                    snake_dir = (0, 1)
                elif event.key == pygame.K_LEFT and last_dir != (1, 0):
                    snake_dir = (-1, 0)
                elif event.key == pygame.K_RIGHT and last_dir != (-1, 0):
                    snake_dir = (1, 0)

        # Check if the new direction is opposite to the current direction
        if (snake_dir[0] == -1 * snake[1][0] + snake[0][0]) and (snake_dir[1] == -1 * snake[1][1] + snake[0][1]):
            snake_dir = last_dir  # If opposite, continue in the current direction

        last_dir = snake_dir

        # Move the snake
        head = (snake[0][0] + snake_dir[0] * 10, snake[0][1] + snake_dir[1] * 10)

        # Wrap around the edges if enabled
        if wrap_around:
            head = (head[0] % width, head[1] % height)
        else:
            # Check for collision with walls
            if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
                if end_screen(score) == "restart":
                    break  # Restart the game
                else:
                    break  # Return to main menu

        snake.insert(0, head)

        # Check for collision with food
        if head == food:
            food = (random.randint(0, (width-10)//10) * 10, random.randint(0, (height-10)//10) * 10)
            score += 10
            if score > high_score:
                high_score = score
                with open("highscore.txt", "w") as file:
                    file.write(str(high_score))
        else:
            snake.pop()

        # Check for collision with self
        if head in snake[1:]:
            if end_screen(score) == "restart":
                break  # Restart the game
            else:
                break  # Return to main menu

        # Draw the screen
        screen.fill(current_theme['background'])
        pygame.draw.rect(screen, current_theme['food'], (*food, 10, 10))
        for segment in snake:
            pygame.draw.rect(screen, current_theme['snake'], (*segment, 10, 10))

        # Draw the score and high score
        score_text = font.render(f"Score: {score}", True, current_theme['text'])
        screen.blit(score_text, (10, 10))

        high_score_text = font.render(f"High Score: {high_score}", True, current_theme['text'])
        screen.blit(high_score_text, (width - 140, 10))

        pygame.display.flip()

        # Set the frame rate based on snake speed
        clock.tick(snake_speed)
