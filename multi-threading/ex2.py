import threading
import time

# class, where print happens
class MyThread(threading.Thread):
    def __init__(self, number):
        super(MyThread, self).__init__()
        self.number = number
    def run(self): # funktio, where print happens
        print('Hello world! ' + str(self.number))
        time.sleep(1) #keep thread alive longer

#List of threads
thread_list = []
for i in range(4):
    thread = MyThread(i) #start new thread of class
    thread_list.append(thread) #add it in list
    thread.start() #start a thread
    time.sleep(0.49) #it blocking the loop
    