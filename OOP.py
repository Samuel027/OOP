class Computer(object):
	def __init__(self, computer_type, name, model, screensize):
		self.computer_type = computer_type
		self.name = name
		self.model = model
		self.screensize = screensize

	def get_computer_type(self):
		return self.computer_type

	def get_name_type(self):
		return self.name

	def get_model(self):
		return self.model

	def get_screensize(self):
		return screensize


class Laptop(Computer):
	def __init__(self, args):
		Computer.__init__(args)
		self.battery = self._get_battery_status()

	def _get_battery_status(self):
		return "charging"

	def get_battery_status(self):
		return self.battery

	def set_screensize(size):
		self.screensize = size

	def get_model(self):
		return "Laptop: " + self.model()

class Desktop(Computer):
	def __init__(self, args):
		Computer.__init__(args)
		self.ups = True

	def get_model(self):
		return "Desktop: " + self.model() 
