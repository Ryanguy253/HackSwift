import random
from Events import Priority, FixedEvent, DynamicEvent
import datetime
from ortools.sat.python import cp_model
from itertools import combinations, permutations
from typing import List

# TODO: Complete TimeTable class
# TODO: Add function to get empty time ranges in the timetable

# Each TimeTable object is a collection of FixedEvent and DynamicEvent objects seperately.
# Balanced Load:
# Load Factor = 5 * Min( [Free Time - Work : weekdays] ) + 2 * WeekEndScaleFactor * Min( [Free Time - Work : weekends] )

def time_del_to_min(time_obj: datetime.timedelta) -> int:
    total_minutes = int(time_obj.total_seconds() // 60)
    return total_minutes

def time_to_minutes(time_obj: datetime.time) -> int:
    total_minutes = time_obj.hour * 60 + time_obj.minute
    return total_minutes

class TimeTable:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos

        self.width=0
        self.height = 0
        self.events = 0
        self.fixed_events: List[FixedEvent] = []    # Contains FixedEvent objects which are not completed yet, and are recurring
        self.dynamic_events: List[DynamicEvent] = []  # Contains DynamicEvent objects which are not completed yet
        self.completed_events = []# Contains FixedEvent and DynamicEvent objects which are completed, 
                                  # ~ FixedEvent objects which are not recurring should not be here

    def sort_events(self):
        pass

    def add_fixed_event(self, event: FixedEvent):
        self.fixed_events.append(event)
        self.schedule_dynamic_events()

    def add_dynamic_event(self, event: DynamicEvent):
        self.dynamic_events.append(event)
        self.schedule_dynamic_events()

    def remove_fixed_event(self, id: int):
        # ...
        self.schedule_dynamic_events()
        pass # Check equality id

    def remove_dynamic_event(self, id: int):
        # ...
        self.schedule_dynamic_events()
        pass # Check equality id

    def get_fixed_events_by_week(self, week: datetime.date):
        pass

    def get_dynamic_events_by_week(self, week: datetime.date):
        pass
    
    def get_occupied_time_ranges(self):
        pass
        
    def print_dynamic_chrono(self):
        # Prints DynamicEvent objects in the timetable in chronological order, seperated by newlines per event.
        dynamic_counter = 0
        fixed_counter = 0
        # Print header
        print("Dynamic Events:")
        print("Name - Date - Start Time - Duration (mins) - Location - Description - Priority")
        dy_events = sorted(self.dynamic_events, key=lambda x: x.get_date() if x.get_date() != None else datetime.date(1, 1, 1))
        fx_events = sorted(self.fixed_events, key=lambda x: x.get_date() if x.get_date() != None else datetime.date(1, 1, 1))
        while dynamic_counter < len(dy_events) and fixed_counter < len(fx_events):
            if dy_events[dynamic_counter].get_date() < fx_events[fixed_counter].get_date():
                print(f"{dy_events[dynamic_counter].get_name()} - {dy_events[dynamic_counter].get_date()} - {dy_events[dynamic_counter].get_start_time()} - {dy_events[dynamic_counter].get_duration()} - {dy_events[dynamic_counter].get_location()} - {dy_events[dynamic_counter].get_description()} - {dy_events[dynamic_counter].get_priority()}")
                dynamic_counter += 1
            elif dy_events[dynamic_counter].get_date() > fx_events[fixed_counter].get_date():
                print(f"{fx_events[fixed_counter].get_name()} - {fx_events[fixed_counter].get_date()} - {fx_events[fixed_counter].get_start_time()} - {fx_events[fixed_counter].get_duration()} - {fx_events[fixed_counter].get_location()} - {fx_events[fixed_counter].get_description()} - {fx_events[fixed_counter].get_priority()}")
                fixed_counter += 1
            elif dy_events[dynamic_counter].get_start_time() < fx_events[fixed_counter].get_start_time():
                print(f"{dy_events[dynamic_counter].get_name()} - {dy_events[dynamic_counter].get_date()} - {dy_events[dynamic_counter].get_start_time()} - {dy_events[dynamic_counter].get_duration()} - {dy_events[dynamic_counter].get_location()} - {dy_events[dynamic_counter].get_description()} - {dy_events[dynamic_counter].get_priority()}")
                dynamic_counter += 1
            else:
                print(f"{fx_events[fixed_counter].get_name()} - {fx_events[fixed_counter].get_date()} - {fx_events[fixed_counter].get_start_time()} - {fx_events[fixed_counter].get_duration()} - {fx_events[fixed_counter].get_location()} - {fx_events[fixed_counter].get_description()} - {fx_events[fixed_counter].get_priority()}")
                fixed_counter += 1
        while dynamic_counter < len(dy_events):
            print(f"{dy_events[dynamic_counter].get_name()} - {dy_events[dynamic_counter].get_date()} - {dy_events[dynamic_counter].get_start_time()} - {dy_events[dynamic_counter].get_duration()} - {dy_events[dynamic_counter].get_location()} - {dy_events[dynamic_counter].get_description()} - {dy_events[dynamic_counter].get_priority()}")
            dynamic_counter += 1
        while fixed_counter < len(fx_events):
            print(f"{fx_events[fixed_counter].get_name()} - {fx_events[fixed_counter].get_date()} - {fx_events[fixed_counter].get_start_time()} - {fx_events[fixed_counter].get_duration()} - {fx_events[fixed_counter].get_location()} - {fx_events[fixed_counter].get_description()} - {fx_events[fixed_counter].get_priority()}")
            fixed_counter += 1
        
        

    def schedule_dynamic_events(self):
        current_day = datetime.date.today()
        model = cp_model.CpModel()
        solver = cp_model.CpSolver()
        dyev_start_time_var = []
        # solver.parameters.log_search_progress = True
        # Shuffle the dynamic events to get different permutations
        # for i in range(len(self.dynamic_events)):
        random.shuffle(self.dynamic_events)
        # Define variables
        dyev_start_time_var = [model.NewIntVar(0, 10080, dynamic_event.get_name()) for dynamic_event in self.dynamic_events]

        # Define constraints
        # No two dynamic events can overlap
        for i in range(len(dyev_start_time_var)):
            for j in range(i + 1, len(dyev_start_time_var)):
                model.Add(dyev_start_time_var[i] + (self.dynamic_events[i].get_duration()) <= dyev_start_time_var[j])
                # print(f"Mins:{self.dynamic_events[i].get_duration()}")
                # model.Add(dyev_start_time_var[j] + (dynamic_event.get_duration()) <= dyev_start_time_var[i])

        # Dynamic events should occur before their expiry date, and within 2 weeks
        for i, dynamic_event in enumerate(self.dynamic_events):
            expiry_time_min = time_del_to_min(dynamic_event.get_expiry_date() - current_day)
            if dynamic_event.get_expiry_date() != None: 
                model.Add(dyev_start_time_var[i] + dynamic_event.get_duration() <= expiry_time_min)
                model.Add(dyev_start_time_var[i] + dynamic_event.get_duration() <= 10080)

        # Dynamic events should occur during 08:00 - 23:00 of each day
        for i, dynamic_event in enumerate(self.dynamic_events):
            
            var_mod_begin = model.NewIntVar(0, 1339, dynamic_event.get_name() + "_mod_begin")
            var_mod_end =   model.NewIntVar(0, 1339, dynamic_event.get_name() + "_mod_end")

            model.AddModuloEquality(var_mod_begin ,dyev_start_time_var[i], 1440)
            model.AddModuloEquality(var_mod_end ,(dyev_start_time_var[i] + dynamic_event.get_duration()), 1440)

            model.Add(var_mod_begin >= time_to_minutes(datetime.time(8, 0)))
            model.Add(var_mod_end <= time_to_minutes(datetime.time(23, 0)))


        # Dynamic events should not overlap with ANY fixed events
        for i, dynamic_event in enumerate(self.dynamic_events):
            for fixed_event in self.fixed_events:
                # Skip if fixed_events are already past
                if fixed_event.get_date() >= current_day:
                    time_offset = time_del_to_min(fixed_event.get_date() - current_day)
                    fixed_event_start_time = time_to_minutes(fixed_event.get_start_time()) - time_offset
                    fixed_event_end_time = time_to_minutes(fixed_event.get_end_time()) - time_offset
                    # print(f"Ev start time: {fixed_event_start_time}, Ev end time: {fixed_event_end_time}")
                    # Add to the model a boolean constraint that the dynamic event should not overlap with the fixed event
                    # (StartDy <= EndFx) and (EndDy >= StartFx) means overlap
                    # (StartDy > EndFx) or (EndDy < StartFx) means no overlap
                    var_left_cond = model.NewBoolVar(dynamic_event.get_name() + "_left_cond")
                    var_right_cond = model.NewBoolVar(dynamic_event.get_name() + "_right_cond")
                    
                    model.Add(dyev_start_time_var[i] > fixed_event_end_time).OnlyEnforceIf(var_left_cond) # DyEv starts before FeEv
                    model.Add(dyev_start_time_var[i] + dynamic_event.get_duration() < fixed_event_start_time).OnlyEnforceIf(var_right_cond)

                    model.AddBoolOr([var_left_cond, var_right_cond])

        # Solve the model
        status = solver.Solve(model)

        if status == cp_model.OPTIMAL:
            # Extract solution
            print("Optimal solution found!")
            for i, dynamic_event_var in enumerate(dyev_start_time_var):
                start_time_minutes = solver.Value(dynamic_event_var)
                start_time_days = start_time_minutes // 1440
                start_time_hours = (start_time_minutes % 1440) // 60
                start_time_minutes %= 60
                self.dynamic_events[i].set_start_time(datetime.time(start_time_hours, start_time_minutes))
                self.dynamic_events[i].set_date(current_day + datetime.timedelta(days=start_time_days))

        elif status == cp_model.FEASIBLE:
            print("Feasible solution found!")
            for i, dynamic_event_var in enumerate(dyev_start_time_var):
                start_time_minutes = solver.Value(dynamic_event_var)
                start_time_days = start_time_minutes // 1440
                start_time_hours = (start_time_minutes % 1440) // 60
                start_time_minutes %= 60
                self.dynamic_events[i].set_start_time(datetime.time(start_time_hours, start_time_minutes))
                self.dynamic_events[i].set_date(current_day + datetime.timedelta(days=start_time_days))

        elif status == cp_model.INFEASIBLE:
            print("No feasible solution found.")

        elif status == cp_model.MODEL_INVALID:
            print("Invalid model.")
            print(model.Validate())

        elif status == cp_model.UNKNOWN:
            print("Failed. Unknown status.")