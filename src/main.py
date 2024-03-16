import pygame
from datetime import datetime
from datetime import date

# Initialize pygame
pygame.init()

# Window
window_width = 1000
window_height = 600
white_background = (255, 255, 255)
screen = pygame.display.set_mode((window_width, window_height))
screen.fill(white_background)
pygame.display.set_caption("Planner")

# Button
class SideButton:
    def __init__(self, position_x, position_y, width_x, height_y, text):
        self.x = position_x
        self.y = position_y
        self.height = height_y
        self.width = width_x
        self.colour = (255, 0, 0)
        self.text = text
        self.surface = pygame.Surface((width_x, height_y))
        self.isClicked = False
        self.isHovered = False

    def draw(self, screen):
        if self.isHovered:
            button_color = (160, 0, 0)  # Change color if hovered over
        else:
            button_color = self.colour
        pygame.draw.rect(self.surface, button_color, pygame.Rect(0, 0, self.width, self.height))
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))
        self.surface.blit(text_surface, text_rect)
        screen.blit(self.surface, (self.x, self.y))  # Blit the button surface onto the screen

    def is_clicked(self, mouse_pos):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return button_rect.collidepoint(mouse_pos)

    def is_hovered_over(self, mouse_pos):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return button_rect.collidepoint(mouse_pos)

# Create a font object
font = pygame.font.Font(None, 24)
datefont = pygame.font.Font(None, 40)

#dateTime
def draw_monthYear():
    # Get the current date
    now = datetime.now()
    month = now.strftime("%B")
    year = now.strftime("%Y")
    day = now.strftime("%A")
    current_time = now.strftime("%H:%M:%S")

    month_string = now.strftime("%B %Y")
    # Render the text
    text_surface = datefont.render(month_string, True, (0, 0, 0))
    # Blit the text surface onto the screen
    screen.blit(text_surface, (0, 20))  # Adjust the position as needed

# Initialize Variables
sideBar = pygame.Rect(0,0,150,600)
dayBar = pygame.Rect(150,0,850,50)

# To add buttons just add here and chagne the array
# Buttons
inputButton = SideButton(25, 50, 100, 40, "INPUT")
sortButton = SideButton(25, 90, 100, 40, "SORT")
deleteButton = SideButton(25,130,100,40,"DELETE")
editButton = SideButton(25,170,100,40,"EDIT")

PlannerButtons = [sortButton, inputButton,deleteButton,editButton]

# Input handling
def handle_input():
    global running, window_height, window_width, screen,PlannerButtons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # If the window is resized, update the window dimensions
            window_width = event.w
            window_height = event.h
            screen = pygame.display.set_mode((window_width, window_height))
            screen.fill(white_background)  # Fill the screen with white background again
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                for button in PlannerButtons:
                    if button.is_clicked(mouse_pos):
                        button.isClicked = True;
        elif event.type == pygame.MOUSEMOTION:
            # Check if mouse is hovering over any button
            for button in PlannerButtons:
                button.isHovered = button.is_hovered_over(pygame.mouse.get_pos())


def update():
    #get datetime
    global now,month,current_time,PlannerButtons

    pygame.display.update()
    for button in PlannerButtons:
        if(inputButton.isClicked):
            print("CLICK INPUT")
            inputButton.isClicked = False;
        if (sortButton.isClicked):
            print("CLICK SORT")
            sortButton.isClicked = False;
        if (deleteButton.isClicked):
            print("CLICK DELETE")
            deleteButton.isClicked = False;
        if (editButton.isClicked):
            print("CLICK EDIT")
            editButton.isClicked = False;


def draw():
    global PlannerButtons, screen
    #draw Bars
    pygame.draw.rect(screen,(169,169,169),sideBar)
    pygame.draw.rect(screen,(169,169,169),dayBar)

    draw_monthYear()

    for button in PlannerButtons:
        button.draw(screen)




# Program Loop
running = True
while running:
    handle_input()
    draw()
    update()

# Quit
pygame.quit()