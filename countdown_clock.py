import time

print("To stop input X")
global timerInput
class Clock():
    def StartClock():
        counterTime = time.time()
        while counterTime+timerInput < time.time():
            if input() == "X":
                break; 
            print(timerInput-(time.time()-counterTime))
        print("Timer Finished")
        Clock.StartProgram()

    def StartProgram():
        timerInput = int(input("Timer Length (in seconds): "))
        Clock.StartClock(timerInput)

Clock.StartProgram()
