import queue
import threading
import time 

exitFlag = 0 

class myThread(threading.Thread):
    def __init__(self,threadID, name, q) -> None:
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name 
        self.q = q 
    
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Existing " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" %(threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

threadList = ["Thread-1", "thread-2", "Thread-3"]
name_list = ["One", "Two","Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

#crete new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in name_list:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
    