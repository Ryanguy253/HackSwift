from Events import Priority, Event, FixedEvent, DynamicEvent
from TimeTable import TimeTable
import datetime
from random import randint
if __name__ == "__main__":

    # Create a TimeTable object
    tt = TimeTable(0,0)
    for j in range(15):
        i = j + 1
        ev = DynamicEvent("Event " + str(i), 
                randint(30, 120),
                datetime.date(2024,3,20),
                "Location "+str(i), 
                "Description "+str(i), 
                Priority.LOW)
        print(f"adding: {ev.get_name()} - {ev.get_duration()} - {ev.get_priority()}")
        tt.add_dynamic_event(ev)

    
    tt.print_dynamic_chrono()


st = datetime.time(0,0)