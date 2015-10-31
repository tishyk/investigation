
import time, sys
i = 0
while i<20:
    sys.stdout.write("\r%0.3i"%(i))
    sys.stdout.flush()
    i+=1
    time.sleep(0.5)
