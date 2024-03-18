from Events import Priority, FixedEvent, DynamicEvent
import datetime
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