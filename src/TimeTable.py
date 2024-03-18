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

    def sort_fixed_events(self):
        TNow = datetime.datetime.now()
        TempList = []
        OutputList = []
        for item in self.fixed_events:
            TDiff = datetime.datetime.combine(item.get_date(),item.get_start_time())-TNow
            TimeTillEvent = TDiff.days * (24*60*60) + TDiff.seconds
            TempList.append((TimeTillEvent,item))
        TempList.sort()
        for item in TempList:
            OutputList.append(item[1])
        self.fixed_events = OutputList

    def sort_dynamic_events(self):
        TNow = datetime.datetime.now()
        TempList = []
        OutputList = []
        for item in self.dynamic_events:
            TDiff = datetime.datetime.combine(item.get_date(),item.get_start_time())-TNow
            TimeTillEvent = TDiff.days * (24*60*60) + TDiff.seconds
            TempList.append((TimeTillEvent,item))
        TempList.sort()
        for item in TempList:
            OutputList.append(item[1])
        self.dynamic_events = OutputList

    def add_fixed_event(self, event: FixedEvent):
        event._unique_id = self.id_counter
        self.fixed_events.append(event)
        self.id_counter += 1
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
                self.fixed_events.remove(event)
                return 1
        # Check equality id

    def remove_dynamic_event(self, id: int):
        if len(self.dynamic_events) == 0:
            return 0
        for event in self.dynamic_events:
            if event._unique_id == id:
                self.dynamic_events.remove(event)
                return 1
        # Check equality id

    def get_fixed_events_by_week(self, week: datetime.date):
        output = []
        today = datetime.datetime.now()
        days_to_monday = today.weekday()
        monday_date = today - datetime.timedelta(days=days_to_monday)
        self.sort_fixed_events()

        end_date = monday_date + datetime.timedelta(days=7)
        for item in self.fixed_events:
            if item.get_date() < end_date:
                output.append(item)
            else:
                break
        return output

    def get_dynamic_events_by_week(self, week: datetime.date):
        output = []
        today = datetime.datetime.now()
        days_to_monday = today.weekday()
        monday_date = today - datetime.timedelta(days=days_to_monday)
        self.sort_dynamic_events()

        end_date = monday_date + datetime.timedelta(days=7)
        for item in self.fixed_events:
            if item.get_date() < end_date:
                output.append(item)
            else:
                break
        return output

    def get_empty_time_ranges(self):
        pass
    
    def shedule_dynamic_events(self):
        pass