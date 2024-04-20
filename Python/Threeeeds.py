import threading
from time import sleep

## DEFAULT THREADS

class PersonalThread :
    def __init__(self, target, args, name=None, daemon=False) -> None:
        self.thread = threading.Thread(target=target, args=args, name=name, daemon=daemon) #MAIN
    def start(self) -> None :
        self.thread.start()
    def setDaemon(self, state : bool) -> None :
        self.thread.setDaemon(state)

def oneFunc(num) :
    sleep(num)
    print("Hello Nu")
    
'''
def twoFunc(num, l) :
    res = 0
    for i in range(l) :
        sleep(num)
        print(f"mb X{i+1}")
        x = i ** 2
        res += x
    print("yes sir", res)

t1 = PersonalThread(oneFunc, (1,), "Hello")
t2 = PersonalThread(twoFunc, (1, 3), "HelloEnd", daemon=True) # демон поток

print(threading.main_thread().name)

t1.start()
t2.start()

print("Finish то есть все потоки завершились")

## Lock

value = 0
myLock = threading.Lock()

def incVal() :
    global value 
    with myLock :
        for _ in range(10) :
            sleep(0.05)
            value += 1
            print(value)

for i in range(5) :
    threading.Thread(target=incVal, args=(), name=f"t{i}").start()

## RLock 

myR = threading.RLock()

myR.acquire()
myR.acquire()
myR.acquire()

myR.release()
myR.release()
myR.release()

# Semaphore

cap = 5
mySBD = threading.BoundedSemaphore(5)

def hiFuncSBD(num) :
    with mySBD :
        sleep(num)
        print("HI")

with myLock :
    for i in range(cap) :
        th = threading.Thread(target=hiFuncSBD, args=(0.5, ))
        th.start()
'''

# Event
'''
def eventFunc() :
    print("start", threading.current_thread().name)
    myEvent.wait() # или можно поставить timeout=0
    print("end \n")

myEvent = threading.Event()

for i in range(10) :
    PersonalThread(eventFunc, (), f'event-{i+1}').start()
    sleep(0.25)

myEvent.clear() # IS SET = FALSE
myEvent.set() '''

# Condition

def condFunc1(a) :
    for i in range(a) :
        with myCond :
            myCond.wait()
            sleep(0.02)
            print(f"Следущие {a}-элементы")

def condFunc2(a, b) :
    for i in range(a) :
        if i % b == 0 :
            with myCond :
                myCond.notify()
        else :
            print(i)
        sleep(0.01)
myCond = threading.Condition()

th1 = PersonalThread(condFunc1, (10,))
th2 = PersonalThread(condFunc2, (100,10))

th1.start()
th2.start()
