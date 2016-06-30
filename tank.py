#tank System

#tank display unit

#showing rpm,speed,gear,engine power in use

#movement of turrent

#movement of cover to protect the solar plates

#override system for commander and gunner

#fast and slow movement of turret 


#as of now we have are not collaborating it with buttons


#so we have a menu system


class driver_view_channel:
	def __init__(self):
		print "driver viewer unit started"

	def rpm(self):
		print "get the rpm"
	def speed(self):
		print "get the speed"
	def gear(self):
		print "get the gear"
	def engine_power(self):
		print "get the engine power"


class driver:
	def __init__(self):
		print "driver class started"

	def give_fire_warning(self):
		print "all the chamber red light starts to blink"

	def claok_sun_panels(self):
		print "covered the solar panels to reduce damage"


class commander_view_channel:
	def __init__(self):
		print "commander class started"

	def get_turrent_angle(self):
		print "get the current tank turret angle"

	def get_commander_viewpoint(self):
		print "get the angle at which commander is viewing"

	def change_turret_angle(self):
		print "change the angle of turrent from current to the view angle"

	def get_gunner_view(self):
		print "show on the screen the view that the gunner is currently seeing"

	def override_gunner_angle(self):
		print "irrespective of what gunner is aimming for the turret moves on commander command"
	
	def get_gunner_angle(self):
		print "show gunner view angle"

	def get_arm_selected(self):
		print "show the weapon details selected"

	def change_arm(self):
		print "which arm to select"

	def select_movement(self):
		print "by default slow using pid equation"
		print "which mode do u want"

	def get_movement(self):
		print "the method of turrent movement"

class commander_get_display_unit:
	def __init__(self):
		print "the display of commander started"

	def get_turrent_angle(self):
		print "get the current tank turret angle"

	def get_commander_viewpoint(self):
		print "get the angle at which commander is viewing"

	def get_gunner_view(self):
		print "show on the screen the view that the gunner is currently seeing"

	def get_arm_selected(self):
		print "show the weapon details selected"

	def get_movement(self):
		print "the method of turrent movement"

