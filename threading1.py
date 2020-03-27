# to run a concurrent process we use threading
# this is a basic task for this example purpose
# start() will start the action
# join() will wait till the processes finishes
import threading
import time

def myfunction():
    print("Start of the action")
    time.sleep(10) # wait for 10 seconds
    print("Finishing of the action")

threads = []

for i in range(5): # we want to run 5 concurrent threads of the function defined above
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)
for th in threads: # now we close all the opened actions with this loop\
    th.join()
