import threading

def worker():
    """thread worker function"""
    print("Here is our worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
