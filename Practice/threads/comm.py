from threading import Event, Thread
import time 

terminate = False
def signal_state():
    global terminate
    while not terminate:
        time.sleep(0.5)
        print("Trafiic Police Giving GREEN Signal")
        event.set()
        time.sleep(1)
        print("Trafiic Police Giving RED Signal")
        event.clear()

def traffic_flow():
    global terminate
    num = 0
    while num < 10 and not terminate:
        print("Waiting for GREEN Signal")
        event.wait()
        print("GREEN Signal... Tranffic can move")
        while event.is_set() and not terminate:
            num += 1
            print("vehicle No", num, " Crossing the Signal")
            time.sleep(1)
        print("RED Signal... Traffic has to wait")

event = Event()
t1 = Thread(target=signal_state)
t2 = Thread(target=traffic_flow)

t1.start()
t2.start()

time.sleep(5)
terminate = True

t1.join()
t2.join()