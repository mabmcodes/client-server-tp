import threading
import time


star = time.perf_counter()


  

def do_something(_step):
    
    time.sleep(_step[1])
    print(f'FINISHED {_step[0]} after {_step[1]} second(s).')
    

def _Threads(_steps):

     threads = []
     for step in _steps:
         thread = threading.Thread(target=do_something, args=[step])
         thread.start()
         threads.append(thread)

     for thread in threads :
        thread.join()



finish = time.perf_counter()

print(f'finished in {round(finish-star,2)} "second(s)')
