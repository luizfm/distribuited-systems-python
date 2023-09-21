import time
from threading import Thread

class PethersonAlgorithim:
    def __init__(self):
        self.turn = 0
        self.flags = [False, False]
    
    def lock(self, id):
      other = 1 - id
      self.flags[id] = True
      self.turn = id

      while self.flags[other] and self.turn == id:
          pass

    def unlock(self, id):
        self.flags[id] = False



def thread_function(index, peterson):
    for i in range(5):
        print(f"Thread {index} is non-critical section")
        peterson.lock(index)
        print(f"Thread {index} is in critical section")
        time.sleep(1)
        print(f"Thread {index} is now leaving critical section")
        peterson.unlock(index)

peterson = PethersonAlgorithim()

t1 = Thread(target=thread_function, args=(0, peterson))
t2 = Thread(target=thread_function, args=(1, peterson))

t1.start()
t2.start()

t1.join()
t2.join()