from Events import Priority, FixedEvent, DynamicEvent
import datetime
# TODO: Complete TimeTable class
# TODO: Add function to get empty time ranges in the timetable

# Each TimeTable object is a collection of FixedEvent and DynamicEvent objects seperately.
# Balanced Load:
# Load Factor = 5 * Min( [Free Time - Work : weekdays] ) + 2 * WeekEndScaleFactor * Min( [Free Time - Work : weekends] )

class TimeTable:
    def __init__(self):
        pass

    def get_empty_time_ranges(self):
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

    def shedule_dynamic_events(self):
        pass