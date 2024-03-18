import pygame
from datetime import datetime,date,timedelta

# Initialize pygame
pygame.init()

# Window
window_width = 1000
window_height = 600
white_background = (255, 255, 255)
screen = pygame.display.set_mode((window_width, window_height))
screen.fill(white_background)
pygame.display.set_caption("Planner")

# Colours
Dark_Gray = (64, 64, 64)
Light_Gray=  (192, 192, 192)
Slate_Gray= (112, 128, 144)
Charcoal= (54, 69, 79)
Steel_Blue= (70, 130, 180)
Navy_Blue= (0, 0, 128)
Royal_Blue= (65, 105, 225)
Deep_Green= (0, 100, 0)
Olive_Green= (128, 128, 0)
Burgundy= (128, 0, 32)

#Testing
Recty = 100
Rect = (400,Recty,100,100)

# Button
class SideButton:
    def __init__(self, position_x, position_y, width_x, height_y, text):
        self.x = position_x
        self.y = position_y
        self.height = height_y
        self.width = width_x
        self.colour = (200,0,0)
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

#scroll bar
class scrollBar:
    def __init__(self, position_x, position_y, width_x, height_y):
        self.x = position_x
        self.y = position_y
        self.width = width_x
        self.height = height_y
        #self.icon = icon
        self.isHovered = False
        self.isClicked = False
        self.colour = (220,220,220)
        self.bar_colour = (169,169,169)
        self.bar_pos_x = position_x
        self.bar_pos_y = position_y
        self.bar_height = 75
        self.barisDragged = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self,screen):
        if(self.isHovered):
            self.bar_colour = (64,64,64)
        else:
            self.bar_colour = (169,169,169)
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen,self.bar_colour,pygame.Rect(self.bar_pos_x,self.bar_pos_y,self.width,self.bar_height))

    def is_hovered_over(self,mouse_pos):
        scroll_bar_rect = pygame.Rect(self.bar_pos_x,self.bar_pos_y,self.width,self.bar_height)
        return scroll_bar_rect.collidepoint(mouse_pos)

    def is_dragged(self,mouse_pos):
        scroll_bar_rect = pygame.Rect(self.bar_pos_x, self.bar_pos_y, self.width, self.bar_height)
        return scroll_bar_rect.collidepoint(mouse_pos)

    def detect_scroll(self,mouse_pos):
        if self.is_dragged(mouse_pos):
            self.barisDragged = True
            self.offset_y = self.bar_pos_y - mouse_pos[1]

    def scrolling(self,mouse_pos):
        self.bar_pos_y = mouse_pos[1] + self.offset_y
        if(self.bar_pos_y <= 50):
            self.bar_pos_y = 50
            return
        if(self.bar_pos_y >= 525):
            self.bar_pos_y = 525
            return
        #testing
        # Update the position of the test rectangle based on the scroll bar position
        global Recty
        Recty = 50 + (self.bar_pos_y - 50) * (1000 - window_height) / (600 - 50 - self.bar_height)

    def stop_scrolling(self,mouse_pos):
        self.barisDragged = False

rightScrollBar = scrollBar(975,50,25,600)
scrollBars = [rightScrollBar]

# Create a font object
font = pygame.font.Font(None, 24)
datefont = pygame.font.Font(None, 30)

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

def get_monday_date():
    # Get today's date
    today = datetime.now()
    # Calculate the difference between today's weekday and Monday (0: Monday, 1: Tuesday, ..., 6: Sunday)
    days_to_monday = today.weekday()
    # Subtract the difference to get the date of Monday of the current week
    monday_date = today - timedelta(days=days_to_monday)
    return monday_date

def draw_dayDate(x, y):
    # Get the date of Monday of the current week
    monday_date = get_monday_date()
    # Iterate over each day of the week
    for i in range(7):
        # Get the date for the current day in the loop
        current_date = monday_date + timedelta(days=i)

        # Format the date string
        day_DateString = current_date.strftime("%a %d")
        # Render the text
        text_surface = datefont.render(day_DateString, True, (0, 0, 0))

        # Blit the text surface onto the screen
        # Change colour of today's date to highlight it
        now = datetime.now()
        if (current_date.day == now.day):
            text_surface = datefont.render(day_DateString, True, (255, 0, 0))  # Change color to red
        screen.blit(text_surface, (x + (120 * i), y))



# Initialize Variables
sideBar = pygame.Rect(0,0,150,600)
dayBar = pygame.Rect(150,0,850,50)

# To add buttons just add here and chagne the array
# Buttons
inputButton = SideButton(0, 50, 100, 40, "INPUT")
sortButton = SideButton(0, 90, 100, 40, "SORT")
deleteButton = SideButton(0,130,100,40,"DELETE")
editButton = SideButton(0,170,100,40,"EDIT")

#upButton = SideButton(0,555,100,20,"UP")
#downButton = SideButton(0,575,100,20,"DOWN")

PlannerButtons = [sortButton, inputButton,deleteButton,editButton]

# Input handling
def handle_input():
    global running, window_height, window_width, screen,PlannerButtons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                for _button in PlannerButtons:
                    if _button.is_clicked(mouse_pos):
                        _button.isClicked = True
                for _scrollbar in scrollBars:
                    _scrollbar.detect_scroll(mouse_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            #stop scrolling
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                for _scrollbar in scrollBars:
                    _scrollbar.stop_scrolling(mouse_pos)

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            # Check if mouse is hovering over any button
            for _button in PlannerButtons:
                _button.isHovered = _button.is_hovered_over(pygame.mouse.get_pos())
            # Check if mouse is hovering over scroll bar
            for _scrollbar in scrollBars:
                _scrollbar.isHovered = _scrollbar.is_hovered_over(pygame.mouse.get_pos())
                if _scrollbar.barisDragged:
                    _scrollbar.scrolling(mouse_pos)



def update():
    global PlannerButtons

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
    # Clear the screen
    screen.fill(white_background)

    #testing
    # Draw the test rectangle at the calculated content position
    pygame.draw.rect(screen, (255, 0, 0), (400,Recty, 500, 100))
    #testing

    #draw Bars
    pygame.draw.rect(screen,(112,128,144),sideBar)
    pygame.draw.rect(screen,Slate_Gray,dayBar)

    draw_monthYear()
    draw_dayDate(150,30)

    #draw buttons
    for _button in PlannerButtons:
        _button.draw(screen)

    #draw scroll bar
    for _scrollbar in scrollBars:
        _scrollbar.draw(screen)



# Program Loop
running = True
while running:
    handle_input()
    draw()
    update()

# Quit
pygame.quit()