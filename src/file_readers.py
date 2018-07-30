import json

from .customer import Customer
from exceptions import InvalidInputError

class CustomerFileReader(object):
	def __init__(self, input_file):
		self.input_file = input_file

	def extract(self):
		with open(self.input_file) as f:
			customer_list = [self.create_customer(json.loads(payload)) for payload in f.readlines()]

		return customer_list

	def create_customer(self, payload):

		if 'user_id' not in payload: raise InvalidInputError('user_id missing!')
		if 'name' not in payload: raise InvalidInputError('name missing!')
		if 'latitude' not in payload: raise InvalidInputError('latitude missing!')
		if 'longitude' not in payload: raise InvalidInputError('longitude missing!')

		return Customer(payload['user_id'], payload['name'], payload['latitude'], payload['longitude'])
