import time
from bebop import Bebop


drone = Bebop()
drone.takeoff()
drone.flyToAltitude(1)
drone.update( cmd=movePCMDCmd( True, 0, 5, 0, 0 ) )
wait( 1 )
drone.update( cmd=movePCMDCmd( True, 0, -5, 0, 0 ) )
drone.land()