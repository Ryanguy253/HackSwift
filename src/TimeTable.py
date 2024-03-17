from Events import Priority, FixedEvent, DynamicEvent

# Each TimeTable object is a collection of FixedEvent and DynamicEvent objects seperately.

class TimeTable:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos

        self.width=0
        self.height = 0
        self.events = 0