import threading
import time 

def schedule_event(name,start):
    now = time.time()
    elasped = int(now - start)
    print("Elasped:", elasped, "Name:", name )

start = time.time()
print("START:",time.ctime(start))

t1 = threading.Timer(10, schedule_event, args=("EVENT_1",start))
t2 = threading.Timer(2,schedule_event, args=("EVENT_2",start))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("End:", time.ctime(end))