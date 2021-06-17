#The Platform module is used to retrieve as much possible information about the platform on which the program is being currently executed. 
#Now by platform info, it means information about the device, it’s OS, node, OS version, Python version, etc. 
#This module plays a crucial role when you want to check whether your program is compatible with the python version installed on a particular system or whether the hardware specifications meet the requirements of your program.
#This module already exists in the python library and does not require any installation using pip.

#It can be imported using the following syntax:

#import platform
# Python program to display platform processor

# import module
import platform

# displaying platform processor
print('Platform processor:', platform.processor())

