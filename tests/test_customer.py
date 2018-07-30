import pytest

from src import Customer, Location

class TestCustomer(object):

	def test_init(self):
		user_id = 1
		name = 'John Doe'
		latitude = '10'
		longitude = '20'

		c = Customer(user_id, name, latitude, longitude)

		assert c.user_id == user_id
		assert c.name == name
		assert c.location.latitude == float(latitude)
		assert c.location.longitude == float(longitude)

	def test_distance(self):
		user_id = 1
		name = 'John Doe'
		latitude = '10'
		longitude = '20'

		c = Customer(user_id, name, latitude, longitude)
		from_location = Location(10, 20)

		assert c.distance(from_location) == 0.0

	def test_within(self):
		user_id = 1
		name = 'John Doe'
		latitude = '10'
		longitude = '20'

		c = Customer(user_id, name, latitude, longitude)

		from_location1 = Location(10, 20)
		from_location2 = Location(20, 20)

		assert c.within(1, from_location1) == True
		assert c.within(1, from_location2) == False

	def test_display(self):
		user_id = 1
		name = 'John Doe'
		latitude = '10'
		longitude = '20'

		c = Customer(user_id, name, latitude, longitude)

		assert c.display() == '1: John Doe'		
