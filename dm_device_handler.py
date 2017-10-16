'''This object will handle executing the task with the device'''

import Paramiko
import re

class Device_Handler(object):
	job = {}
	task = {}
	command_list = []

	def __init__(self, job, task):
		self.job = job
		self.task = task
	
	def get_command_list(self):
		filename = "ad3"
		self.command_list = job['vendor'][task['rule']]

	def parse_command_list(self):
		for line in command_list:
			command_arg = re.search('[^\s]*)\s\"(.*?)\"', line)
            func_map = command_arg.group(1)
            argument = command_arg.group(2)
            argument.replace( )
            self.task['message'] = argument
            #call method here with func_map
            #how to pass task to func_map?  maybe task is pointed to by reference?