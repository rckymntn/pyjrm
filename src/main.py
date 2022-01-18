import psutil
import threading

###
#   findProcess(Nothing) -> process : Process 
###
def findProcess():
    processName = input("Enter a process name: ")
    print("Searching for a process with the name {}.".format(processName))
    for process in psutil.process_iter():
        #print(process.name)
        if processName == process.name():
            print("Process {} found.".format(processName))
            return process
    print("Process {} not found.".format(processName))
    return None


###
#   timeframe(Nothing) -> frequency : int, duration : int
###
def timeframe():
    frequency = input("How often data will be collected, in seconds: ")
    duration = input("How long data will be collected, in seconds: ")
    try:
        frequency = int(frequency)
        duration = int(duration)
    except:
        print("Invalid timeframe specified.")
        return None, None
    if (frequency > duration):
        print("Invalid timeframe specified. Frequency of data collection is greater than the duration of data collection.")
        return None, None
    elif (frequency <= 0 or duration <= 0):
        # Could this be caught if bad input returned -1 instead and the while loop was performed while frequency, duration <= 0? 
        # Yes. However, the procedure for handling user input would be less graceful. 
        # So instead we're returning and looping on None for bad input and keeping that consistent.
        # Take this out later and justify in README, maybe with a concrete example
        print("Invalid timeframe. Frequency and duration need to be a value greater than zero.")
        return None, None
    else:
        print("Collecting data every {} seconds for {} seconds.".format(frequency, duration))
        return frequency, duration


###
#   getData(process : Process) -> 
###
def getData(frequency):
    threading.Timer(frequency, getData).start()
    return


###
#   jsonify() -> Nothing
###
def jsonify():
    return


###
#
###
def main():
    # Find the process
    process = None
    while (process == None):
        process = findProcess()

    # How long and how often the program should run for 
    frequency, duration = None, None
    while (frequency == None or duration == None):
        frequency, duration = timeframe()

    exit(0)


if (__name__ == "__main__"):
    main()