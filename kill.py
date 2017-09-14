from bebop import Bebop

drone = Bebop()

if drone.flyingState is None or drone.flyingState == 1:
	drone.emergency()
drone.land()