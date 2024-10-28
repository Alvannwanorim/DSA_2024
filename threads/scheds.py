import sched
import time 
from datetime import datetime

def addition(a,b):
    print("Performaing addition:",datetime.now())
    print("time : ", time.monotonic())
    print("Result {} + {} ={}".format(a,b, a + b))

s = sched.scheduler()

print("Start Time: ", datetime.now())

event1 = s.enter(4,1,addition, argument=(5,6))
print('Event created', event1)
event2 = s.enter(2,1,addition, argument=(5,10))
print('Event created', event2)
event4 = s.enter(6,1,addition, argument=(0,6))
print('Event created', event4)
event3 = s.enter(10,1,addition, argument=(5,-6))

print('Event created', event3)
s.run()
print("End Time: ", datetime.now() )