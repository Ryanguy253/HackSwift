import Events
from Events import Priority, FixedEvent, DynamicEvent,Event
import datetime
import pygame
from enum import Enum
from datetime import date,time,timedelta


# TODO: Complete TimeTable class
# TODO: Add function to get empty time ranges in the timetable

# Each TimeTable object is a collection of FixedEvent and DynamicEvent objects seperately.
# Balanced Load:
# Load Factor = 5 * Min( [Free Time - Work : weekdays] ) + 2 * WeekEndScaleFactor * Min( [Free Time - Work : weekends] )

class TimeTable:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos

        self.width=0
        self.height = 0
        self.events = 0
        self.fixed_events = []
        self.dynamic_events = []

    def sort_events(self):
        pass

    def add_fixed_event(self, event: FixedEvent):
        pass

    def add_dynamic_event(self, event: DynamicEvent):
        pass

    def remove_fixed_event(self, id: int):
        pass # Check equality id

    def remove_dynamic_event(self, id: int):
        pass # Check equality id

    def get_fixed_events_by_week(self, week: datetime.date):
        pass

    def get_dynamic_events_by_week(self, week: datetime.date):
        pass

    def get_empty_time_ranges(self):
        pass
    
    def shedule_dynamic_events(self):
        pass




class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    URGENT = 3

class event():
    def init(self,
                 name: str,
                 start_time: datetime.time,
                 end_time: datetime.time,
                 recur_period: int,
                 date: datetime.date,
                 location: str,
                 description: str,
                 duration: str,
                 expiry_date: datetime.date,
                 priority_tag: Priority = Priority.LOW):
        self._name = name
        self._start_time = start_time
        self._date = date
        self._location = location
        self._description = description
        self._priority_tag = priority_tag
        self._end_time = end_time
        self._recur_period = recur_period
        self._duration = duration
        self._expiry_date = expiry_date


def testEvent(FixArray,DymArray):
    for i in range(0, 11, 2):
        a = i + 1
        Event = FixedEvent(name='Fix' + str(i),
                           start_time=datetime.time(i, 0, 0),
                           end_time=datetime.time(i, 30, 0),
                           date=datetime.datetime.now(),
                           recur_period=0,
                           recur_cycle=0,
                           location='Fix' + str(i),
                           description='Fix' + str(i),
                           priority_tag=Priority(i % 4))
        FixArray.append(Event)

        Event = DynamicEvent(name='Dym' + str(a),
                             duration=datetime.time(0, 30, 0),
                             expiry_date=datetime.datetime.now(),
                             location='Fix' + str(i),
                             description='Dym' + str(a),
                             priority_tag=Priority(a % 4))
        Event._start_time = datetime.time(a, 0, 0)
        Event._date = datetime.datetime.now()
        DymArray.append(Event)

    for item in FixArray:
        item.print_event()
    for item in DymArray:
        item.print_event()


class timetableBox():
    def init(self, x, y, height, width,
                 color,name,start_time,
                 priority): #, date,location, description,end_time, duration,expiry_date):
        box_image = pygame.Surface((height, width))
        box_image.fill(color)
        self.image = box_image
        self.rect = pygame.Rect(x, y, width, height)
        self.nameText = name
        self.start_timeText = start_time
        self.priority = priority
        self.dateText = date
        # self.locationText = location
        # self.descriptionText = description
        # self.end_timeText = end_time
        # self.durationText = duration
        # self.expiry_dateText = expiry_date

    def draw(self, priority):

        Yellow = (255, 255, 0)
        Green = (0, 255, 0)
        DarkGreen = (0, 128, 0)
        colour = Yellow
        # classify priority
        if priority == Priority(0):
            colour = DarkGreen
        elif priority == Priority(1):
            colour = Green
        elif priority == Priority(2):
            colour = Yellow
        elif priority == Priority(3):
            colour = (255, 0, 0)

        pygame.draw.rect(screen, colour, self.rect)
        text_surface = font.render(self.nameText, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery-2))
        screen.blit(text_surface, text_rect)
        text_surface = font.render(str(self.start_timeText), True, (0, 0, 0))
        text_rect = text_surface.get_rect(midtop=(self.rect.centerx, self.rect.centery+2))
        screen.blit(text_surface, text_rect)
        text_surface = font.render(str(self.start_timeText), True, (0, 0, 0))
        text_rect = text_surface.get_rect(midtop=(self.rect.centerx, self.rect.centery+2))
        screen.blit(text_surface, text_rect)



box_color = (255, 0, 0)  # Red color
box = timetableBox(100, 100, 50, 100, box_color, "EVENT1", 2, 3)



while True:

    screen.fill((255, 255, 255))  # Fill with white color

    current_day = eventsArray[0]._date
    # for i in range(len(eventsArray)):
    #     j = 0
    #     k = 0
    #     while (current_day != eventsArray[0]._date):
    #         hello = timetableBox(100*k ,60*j, 50, 100, box_color, eventsArray[i]._name, eventsArray[i]._start_time, eventsArray[i]._priority_tag)
    #                  #(eventsArray[i].name, eventsArray[i].start_time, eventsArray[i].date, eventsArray[i].location, eventsArray[i].description, eventsArray[i].priority_tag, eventsArray[i].end_time, eventsArray[i].duration, eventsArray[i].expiry_date))
    #         hello.draw(screen, hello.nameText, hello.priority)
    #         j +=1
    #     else:
    #         current_day = eventsArray[i]._date
    #         k +=1
    #         j = 0
    #         continue
    current_day = eventsArray[0]._date
    current_time = eventsArray[0]._start_time
    print(current_time)
    k = 0
    j = 0
    for i in range(len(eventsArray)):
        # If the current event is on a different day, reset the row counter (j) and update the day
        if current_day != eventsArray[i]._date:
            k += 1
            j = 0
            current_day = eventsArray[i]._date
        # Draw the event box
        hello = timetableBox(100 * k, 60 * j, 50, 100, box_color, eventsArray[i]._name,
                             eventsArray[i]._start_time, eventsArray[i]._priority_tag)
        hello.draw(hello.priority)
        j +=1


