import threading
import time

data1=list(range(100000))
data2=list(range(100000,200000))
data3=list(range(200000,300000))


print("Main thread started")
threads=[]
results=[]
def find_sum(data,results):
    result=sum(data)
    results.append(result)
    time.sleep(4)
for data in [data1,data2,data3]:
    thread= threading.Thread(target=find_sum,args=(data,results))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
for result in results:
    print(result)
    
print("Main thread exucution is completed ")

