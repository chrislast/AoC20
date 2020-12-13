from utils import *
import math

DAY = day(__file__)
DATA = get_input(DAY)
#DATA = ["0","17,x,13,19"]
#DATA = ["","67,7,59,61"]
#DATA = ["","67,7,x,59,61"]
#DATA = ["","1789,37,47,1889"]

def next_bus(interval, after, offset=0):
    return math.ceil((after + offset) / interval) * interval

@part1
def func(expect=2215):
    timestamp = int(DATA[0])
    buses = [int(id) for id in DATA[1].split(",") if id != "x"]
    bus_times = {next_bus(bus, timestamp):bus for bus in buses}
    earliest = min(bus_times)
    return (earliest - timestamp) * bus_times[earliest]

@part2
def func(expect=1058443396696792):
    # bus offset
    buses = {int(bus):idx for idx, bus in enumerate(DATA[1].split(",")) if bus != "x"}
    ids = sorted(buses, reverse=True)
    step = ids[0]
    val = -buses[ids[0]]
    n = 0

    while True:
        step = lcm(*ids[0:n+1]) # step by LCM of all synced buses
        bus = ids[n+1]       # next bus id
        offset = buses[bus]  # next bus offset
        # find when the next bus arrives at the correct index
        while (val%bus+offset)%bus:
            val += step
        # step to next bus
        n += 1
        # return answer if all synched
        if n + 1 == len(buses):
            return val
