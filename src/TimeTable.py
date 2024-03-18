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
        self.id_counter = 0
        self.width=0
        self.height = 0
        self.events = 0
        self.fixed_events = []
        self.dynamic_events = []

    def sort_events(self):
        pass

    def add_fixed_event(self, event: FixedEvent):
        event._unique_id = self.id_counter
        self.fixed_events.append(event)
        self.id_counter +=1
        pass

    def add_dynamic_event(self, event: DynamicEvent):
        event._unique_id = self.id_counter
        self.dynamic_events.append(event)
        self.id_counter += 1
        pass

    def remove_fixed_event(self, id: int):
        if len(self.fixed_events) == 0:
            return 0
        for event in self.fixed_events:
            if event._unique_id == id:
                pass
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




