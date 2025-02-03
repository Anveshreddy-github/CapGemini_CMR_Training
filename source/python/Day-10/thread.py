import threading
import time

def single_task():
    print("Task started")
    time.sleep(2)
    print("task completed")

def second_task():
    print("Task 2 started")
    time.sleep(2)
    print("task 2 completed")

thread=threading.Thread(target=single_task)
thread_2=threading.Thread(target=second_task)
thread.start()      
thread.join()
thread_2.start()      
thread_2.join()
print("The main thread execution completed")