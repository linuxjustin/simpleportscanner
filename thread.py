from queue import Queue

print_lock = threading.Lock()


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


for worker in range(1,10000):
    q.put(worker)

q.join()
