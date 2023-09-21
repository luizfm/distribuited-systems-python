from threading import Thread, Lock

counter = 0
lock = Lock()

def increment():
    global counter
    with lock:
        counter += 1

threads = [Thread(target=increment) for _ in range(1000)]
[t.start() for t in threads]
[t.join() for t in threads]

secondThreads = [Thread(target=increment) for _ in range(1000)]
[st.start() for st in secondThreads]
[st.join() for st in secondThreads]

print(counter)