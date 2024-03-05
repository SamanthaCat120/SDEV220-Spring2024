import multiprocessing
import random
from datetime import datetime
from time import sleep



def now(seconds):
    sleep(seconds)
    current_time = datetime.now()
    print('wait', seconds, 'seconds, time is', current_time.isoformat())

def ransec():
    processes = []
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()
        processes.append(proc)

    for proc in processes:
        proc.join()
#        print(processes)


if __name__ == '__main__':
    seconds = random.random()
    ransec()
    now(seconds)