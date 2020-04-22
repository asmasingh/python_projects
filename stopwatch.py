#STOPWATCH PROJECT
import time
while True:
    try:
        print("Press Enter to start stopwatch ,CTRL-C to end")
        start_time=time.time()
        while True:
            print("Time Elapsed: ",round(time.time()-start_time),"seconds")
            time.sleep(1)
    except KeyboardInterrupt:
        end_time=time.time()
        print("Total time elapsed: ",round(end_time-start_time),"seconds")
        break
        
