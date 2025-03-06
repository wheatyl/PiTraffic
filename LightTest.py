import PiTraffic
import time

SouthRed = PiTraffic.Traffic("SOUTH", "RED")
SouthYellow = PiTraffic.Traffic("SOUTH", "YELLOW")
SouthGreen = PiTraffic.Traffic("SOUTH", "GREEN")


EastRed = PiTraffic.Traffic("EAST", "RED")
EastYellow = PiTraffic.Traffic("EAST", "YELLOW")
EastGreen = PiTraffic.Traffic("EAST", "GREEN")

NorthRed = PiTraffic.Traffic("NORTH", "RED")
NorthYellow = PiTraffic.Traffic("NORTH", "YELLOW")
NorthGreen = PiTraffic.Traffic("NORTH", "GREEN")


WestRed = PiTraffic.Traffic("WEST", "RED")
WestYellow = PiTraffic.Traffic("WEST", "YELLOW")
WestGreen = PiTraffic.Traffic("WEST", "GREEN")

Buzz = PiTraffic.Buzzer()

# All direction RED LED ON
def AllRed():
    SouthRed.on()
    EastRed.on()
    NorthRed.on()
    WestRed.on()

AllRed()
       

try:
    while True:

        SouthRed.on()
        EastRed.on()
        NorthRed.on()
        WestRed.on()
        SouthYellow.on()
        EastYellow.on()
        NorthYellow.on()
        WestYellow.on()
        SouthGreen.on()
        EastGreen.on()
        NorthGreen.on()
        WestGreen.on()
        
except KeyboardInterrupt:
    PiTraffic.closeGPIO()
    
    
 
