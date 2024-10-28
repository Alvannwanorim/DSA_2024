import threading
import time 

semaphores = threading.Semaphore(2)

def worker():
    with semaphores:
        print("{} has started working...".format(threading.current_thread().name))
        time.sleep(2)
        print("{} has finished working...".format(threading.current_thread().name))

threads = []

for i in range(5):
    t = threading.Thread(target=worker, name="Thread-{}".format(i + 1))
    threads.append(t)
    print("{} has been created".format(t.name))
    t.start()

for t in threads:
    t.join()
    print("{} has terminated ".format(t.name))

print("Threads State: ALL FINISHED")
print("Main Thread FINISHED...")