from Events import Priority, Event, FixedEvent, DynamicEvent
from TimeTable import TimeTable, time_del_to_min
import datetime
from random import randint
if __name__ == "__main__":

    # Create a TimeTable object
    tt = TimeTable(0,0)
    fev = FixedEvent("Fix 1", 
                datetime.time(9, 15), 
                datetime.time(12, 0), 
                datetime.date.today(), 
                7, 
                "Location 1", 
                "Description 1", 
                Priority.LOW)
    tt.add_fixed_event(fev)
    fev = FixedEvent("Fix 2",
                datetime.time(14, 0), 
                datetime.time(16, 0), 
                datetime.date.today(), 
                7, 
                "Location 2", 
                "Description 2", 
                Priority.HIGH)
    tt.add_fixed_event(fev)
    fev = FixedEvent("Fix 3",
                datetime.time(18, 0), 
                datetime.time(21, 0), 
                datetime.date.today(), 
                7, 
                "Location 3", 
                "Description 3", 
                Priority.MEDIUM)
    tt.add_fixed_event(fev)
    total_load_minutes = 0
    deadline = datetime.date(2024, 3, 22)
    for j in range(15):
        i = j + 1
        rand_dur =  randint(30, 120)
        total_load_minutes += rand_dur
        rand_priority = randint(0,3) 
        rand_priority = Priority(rand_priority)
        ev = DynamicEvent("Event " + str(i), 
                 randint(30, 120),
                deadline,
                "Location "+str(i), 
                "Description "+str(i), 
                rand_priority)
        print(f"adding: {ev.get_name()} - {ev.get_duration()} - {ev.get_priority()}")
        tt.add_dynamic_event(ev)
    print(f"total_minutes: {total_load_minutes}")
    print(f"avail_minutes: {(time_del_to_min(deadline - datetime.date.today()) // 1440 ) * 15 * 16 }" )

    
    tt.print_dynamic_chrono()


st = datetime.time(0,0)