import psutil
import json
import threading

from psutil import cpu_count

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
        # Will take this out later and justify in README, maybe with a concrete example
        print("Invalid timeframe. Frequency and duration need to be a value greater than zero.")
        return None, None
    else:
        print("Collecting data every {} seconds for {} seconds.".format(frequency, duration))
        return frequency, duration


###
#   getData(process : Process) -> 
#
#   https://psutil.readthedocs.io/en/latest/
###
def getData(process, frequency):
    p = psutil.Process(process.pid)
    with p.oneshot():
        data = {"name": p.name(),
                "cpuTime": p.cpu_times(), 
                "cpuUsage": p.cpu_percent() / psutil.cpu_count(), 
                "memPercent": p.memory_percent()}
        print(data)
    return


    # cpu = psutil.Process(process.pid).cpu_percent() / psutil.cpu_count()
    # mem = psutil.Process(process.pid).memory_percent() * psutil.virtual_memory()
    # net = psutil.Process(process.pid).connections() 
    # mis = psutil.Process(process.pid).net_io_counters()


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


    getData(process, frequency)

    exit(0)


if (__name__ == "__main__"):
    main()