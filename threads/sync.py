import threading

counter = 0 
def consumer(cv):
    global counter
    with cv:
        print("Consumer is waiting") 
        cv.wait()
        print("Consumer has been notified. Current counter value", counter)

def increment(cv, N):
    global counter
    with cv:
        print("increment is producing items")
        for i in range(N):
            counter += i 
            cv.notify()
        # cv.notify()
        print("increment has finished")

cv = threading.Condition()

consumer_thread = threading.Thread(target=consumer, args=[cv])
increment_thread = threading.Thread(target=increment, args=[cv, 5])

consumer_thread.start()
increment_thread.start()

consumer_thread.join()
increment_thread.join()

print("The Final Counter Value",counter)