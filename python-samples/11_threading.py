# use thread / _thread for old, low-lvl methods 
# use threading for class-based
import _thread, time

# LOCKS
lock1 = _thread.allocate_lock()
def MyThreadedFunction(sleeptime, name, nr):
    global lock1
    with lock1: # calls lock.acquire and lock.finish
        print(name, " - ", str(nr))
    time.sleep(sleeptime)

# main thread
_thread.start_new_thread(MyThreadedFunction, (1, "T1", 1))
_thread.start_new_thread(MyThreadedFunction, (2, "T2", 2))


# waiting for thread to finish

lock1.acquire()
def Func():
    print("This")
    lock1.release() # lock1 is locked by program start, and will get released after this finishes
_thread.start_new_thread(Func, ())
lock1.acquire() # executed only after the first one finishes (after release is passed)

# obs: exceptions do not close the main thread, only that thread


##################
# THREADING module
##################
import threading, time

def BasicWaiter(seconds):
    time.sleep(seconds)
    print("Basic thread finished.")

t = threading.Thread(target=BasicWaiter, args = (4,)) # careful with the needed comma to make it a tuple
t.start()
print("Waiting for basic thread to execute.")
t.join() # waits for the t thread


# to inherit from Thread
class myThread(threading.Thread):
    def __init__(self, seconds):
        threading.Thread.__init__(self)
        self.seconds = seconds
    def run(self):
        time.sleep(self.seconds)
thr = myThread(3)
thr.start() # use start not RUN
thr.join()


# locks - they do not keep ordering
l = threading.Lock()
def LstModifier(lock, lst, nr):
    for i in range(0, 1):
        with lock:
            lst += [nr]
        time.sleep(1)
lst = []
t1 = threading.Thread(target=LstModifier, args=(l, lst, 1))
t2 = threading.Thread(target=LstModifier, args=(l, lst, 2))
t1.start()
t2.start()
t1.join()
t2.join()
print(lst)

# use threading.Rloc to allow locks inside locks

# Conditions - provide wait / notify mechanism
c = threading.Condition()
def MethodThatWaits():
    global c
    with c:
        c.wait()
        print("Finished waiting.")
def MethodThatNotifies():
    global c
    with c:
        print("I do work.")
        time.sleep(4)
        c.notify()
t1 = threading.Thread(target=MethodThatWaits)
t2 = threading.Thread(target=MethodThatNotifies)
t1.start()
t2.start()
t1.join()
t2.join()

# threading.Semaphore(k) = allows maximum k threads running in parallel on that ressource
# use events to cycle through stuff
# barrier = wait for multiple threads to start at the same time. barrier(2) = each thread waits for 2 threads to run