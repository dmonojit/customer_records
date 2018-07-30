from .location import Location

class Customer(object):
	def __init__(self, user_id, name, latitude, longitude):
		self.user_id = user_id
		self.name = name
		self.location = Location(float(latitude), float(longitude))
		self.distance_from_locations = {}

	def within(self, distance, from_location):
		return self.distance(from_location) < distance

	def distance(self, from_location):
		location_key = '_'.join([str(from_location.latitude), str(from_location.longitude)])

		if location_key not in self.distance_from_locations:
			self.distance_from_locations[location_key] = abs(self.location - from_location)

		return self.distance_from_locations[location_key]

	def display(self):
		return '{}: {}'.format(self.user_id, self.name)
