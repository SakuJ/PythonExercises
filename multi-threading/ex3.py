import threading
import time
import inspect

# class, where create threads
class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0
# locker what lock thread
lock = threading.Lock()

def incre():
    global count # set count to global
    cal = inspect.getouterframes(inspect.currentframe())[1][3] # tell which def is used
    print("Inside %s()" % cal)
    print("Acquiring lock")
    with lock:
        print("Lock acquired " + str(threading.currentThread())) # print string and current thread
        count += 1
        time.sleep(2)

# start incre() in while loop
def bye():
    while count < 5:
        incre()

# start incre() in while loop
def hello():
    while count < 5:
        incre()

def main():
    hello_there = Thread(hello) # start hello() in thread
    goodbye = Thread(bye) # start bye() in thread

if __name__ == '__main__':
    main()