
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#/
#tank System

#tank display unit

#showing rpm,speed,gear,engine power in use

#movement of turrent

#movement of cover to protect the solar plates

#override system for commander and gunner

#fast and slow movement of turret 


#as of now we have are not collaborating it with buttons


#so we have a menu system
fire=0
cloak=0

class driver_view_channel:
	def __init__(self):
		print "driver viewer unit started"

	def rpm(self):
		return "get the rpm"
	def speed(self):
		return "get the speed"
	def gear(self):
		return "get the gear"
	def engine_power(self):
		return "get the engine power"
	def get_fire_warning(self):
		#print fire
		if(fire==1):
			return "true"
		else:
			return "false"
	def get_solar_panel_status(self):
		#print cloak
		if(cloak==1):
			return "true"
		else:
			return "false"


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
	
	def change_turret_angle(self):
		commander=commander_get_display_unit()
		y=commander.get_turrent_angle()
		x=int(raw_input("enter your new turret angle"))
		new_angle=(y-x)
		print "new angle is" , 
		print new_angle
		print "change the angle of turrent from current to the view angle"
		return new_angle

	def override_gunner_angle(self):
		return "irrespective of what gunner is aimming for the turret moves on commander command"
	
	def last_gunner_angle(self):
		return "last gunners angle"

	def change_arm(self):
		print "which arm to select"
		print "*************************************************************************"
		print "option_available"
		print "press 1 for anti tank gun "
		print "press 2 for range missile"
		print "press 3 for machine gun "
		print "*************************************************************************"
		x=int(raw_input("enter ur option"))

		while (x!=-14642):	
			if (x==1):
				print "anti tank gun selected"
				break
			elif (x==2):
				print "range missile selected"
				break
			elif(x==3):
				print "machine gun selected"
				break
			else :
				print "wrong input"
				print "*************************************************************************"
				print "option_available"
				print "press 1 for anti tank gun "
				print "press 2 for range missile"
				print "press 3 for machine gun "
				print "*************************************************************************"
				x=int(raw_input("enter ur option"))
		return x

	def select_movement(self):
		print "by default slow using pid equation"
		print "which mode do u want"


class commander_get_display_unit:
	def __init__(self):
		print "the display of commander started"

	def get_turrent_angle(self):
		x=0;
		print "get the current tank turret angle"
		return x
		

	def get_commander_viewpoint(self):
		return "get the angle at which commander is viewing"

	def get_gunner_view(self):
		return "show on the screen the view that the gunner is currently seeing"

	def get_arm_selected(self):
		return "show the weapon details selected"

	def get_gunner_angle(self):
		return "show gunner view angle"

	def get_movement(self):
		return "the method of turrent movement"


def menu():
	print "*************************************************************************"
	print "				main interface console								"
	print "what do u want"
	print "press one for driver"
	print "press two for gunner"
	print "press three for commander"
	print "press four to exit"
	print "**************************************************************************"
	x=raw_input("enter ur number ")
	return x



def menu1():
	print "***************************************************************************"
	print "			Driver Interface console								"
	driver_view=driver_view_channel()
	print driver_view.rpm()
	print driver_view.speed()
	print driver_view.gear()
	print driver_view.engine_power()
	print driver_view.get_fire_warning()
	print driver_view.get_solar_panel_status()
	print "press 1 for fire Warning in manual mode"
	print "press 2 for cloak solar panels in manual mode"
	print "press 3 for closing fire Warning in manual mode"
	print "press 4 for closing cloak solar panels in manual mode"
	print "press 5 to exit driver mode"
	print "****************************************************************************"
	x=int(raw_input("enter your number"))
	print "the no u pressed",
	print x
	return x

def menu1_cmd(y):
	if (y==1):
		#print "in 1"
		fire=1
		#print fire
	elif (y==2):
		cloak=1
	elif (y==3):
		fire=0
	elif (y==4):
		cloak=0
	else:
		print "wrong input"

def menu2():
	print "******************************************************************************"
	print "		Gunner Interface console								"
	commander=commander_get_display_unit()
	print commander.get_turrent_angle()
	print commander.get_commander_viewpoint()
	print commander.get_gunner_view()
	print commander.get_gunner_angle()
	print commander.get_arm_selected()
	print commander.get_movement()
	print "press 1 for change turret angle"
	#print "press 2 for override gunner angle"
	print "press 2 for changing back to gunner's angle"
	print "press 3 for changing arms"
	print "press 4 for changing movement of turrent option"
	print "press 5 to exit"
	print "*******************************************************************************"
	y=int(raw_input("enter your number"))
	return y

def menu2_cmd():
	commander=commander_view_channel()
	if(y==1):
		commander.change_turret_angle()
	elif(y==2):
		commander.last_gunner_angle()
	elif(y==3):
		commander.change_arm()
	elif(y==4):
		commander.select_movement()
	else:
		print "wrong input"


def menu3():
	print "********************************************************************************"
	print "		Commander Interface console								"
	commander=commander_get_display_unit()
	print commander.get_turrent_angle()
	print commander.get_commander_viewpoint()
	print commander.get_gunner_view()
	print commander.get_gunner_angle()
	print commander.get_arm_selected()
	print commander.get_movement()
	print "press 1 for change turret angle"
	print "press 2 for override gunner angle"
	print "press 3 for changing back to gunner's angle"
	print "press 4 for changing arms"
	print "press 5 for changing movement of turrent option"
	print "press 6 to exit"
	print "*******************************************************************************"
	y=int(raw_input("enter your number"))
	return y



def menu3_cmd(y):
	commander=commander_view_channel()
	if(y==1):
		commander.change_turret_angle()
	elif(y==2):
		commander.override_gunner_angle()
	elif(y==3):
		commander.last_gunner_angle()
	elif(y==4):
		commander.change_arm()
	elif(y==5):
		commander.select_movement()
	else:
		print "wrong input"


def main():
	x=int(menu())
	print x
	while (x!=4):
		print x
		while (x==1):
			#print "you have pressed 1"
			#print "welcome to driver mode"
			y=menu1()
			print y
			while(y!=5):
				menu1_cmd(y)
				y=menu1()
			if (y==5):
				break

		while (x==2):
			y=menu2()
			while (y!=5):
				menu2_cmd(y)
				y=menu2()
			if(y==5):
				break

		while (x==3):
			y=menu3()
			while (y!=6):
				menu3_cmd(y)
				y=menu3()
			if(y==6):
				break


		x=int(menu())


if __name__=='__main__':
	main()

