import threading
import time



def display():
    for i in range(1,10):
        time.sleep(5)
        print("child thread excecuting")
    print(threading.currentThread().getName())

display()
#t=threading.Thread(target=display)
#t.start()
#begintime=time.time()
#print("begin time",Begintime)
#t.join()

for i in range(1,10):
    time.sleep(5)
    print("main thread is executing")
print(threading.currentThread().getName())
#endtime=time.time()
#total=endtime-begintime
#print("total time taken",total)