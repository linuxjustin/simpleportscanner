from socket import *
from threading import *
import threading
from queue import Queue
import optparse


aut = '''

******************************************...****
*                                               *
*         Simple Port scanner                   *
*                                               *
******************************************...****
'''
print aut

screenLock = Semaphore(value=1)


            
targe = raw_input("!!!! Please Enter the Host Address: ")
targip =gethostbyname(targe)
print "!!!!! Target ip Address: " , targip
print "!!!!! Starting scan on host: ", targip



def scanner(ports):
    conn = socket(AF_INET, SOCK_STREAM)
    conn.settimeout(0.5)
    
    try:
        res = conn.connect_ex((targip,int(ports)))
        screenLock.acquire()
        if (res ==0):
            print "!!!!  %d/TCP open port !!!!" %  ports
        
    except:
        screenLock.acquire()
             
        return False
    finally:
        screenLock.release()
        conn.close()


    setdefaulttimeout(1)




#small thread

#for ports in range(0,1024):
    #scanner(targip,int(ports))
    # t  = Thread(target=scanner, args(int(ports))
    # t.start()



#advance thread creating worker and queue

def threader():
    while True:
        worker = q.get()
        #worker1 = q.get()
        scanner(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


for worker in range(1,10000):
    q.put(worker)


#worker1 = targe
#q.put(worker1)

q.join()

