import os
import time

print(" Program to demonstrate wait() method:")
print("\n")
print("Creating child process:")
pr = os.fork()
if pr is 0:    
    print("Child process will print the numbers from the range 0 to 5")
    for i in range(0, 5):
        print("Child process printing the number %d"%(i))    
    time.sleep(1.0)  
else:    
    print("The parent process is now waiting")
    cpe = os.wait()
