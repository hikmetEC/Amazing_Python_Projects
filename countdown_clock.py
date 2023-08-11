import time

print("To stop input X")
global timerInput

class Clock():
    def StartClock(timerInput):
        counterTime = time.time()
        while counterTime+timerInput > time.time():
            print(round(timerInput-(time.time()-counterTime),2))
            
        print("Timer Finished")
        Clock.StartProgram()

    def StartProgram():
        if(input("Do you want to exit?(Y/N)): ") == "Y"): 
            exit()

        timerInput = int(input("Timer Length (in seconds): "))
        
        if(timerInput == "X"): 
            exit()
        Clock.StartClock(timerInput)

Clock.StartProgram()
