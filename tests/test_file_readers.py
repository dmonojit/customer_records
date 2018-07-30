import pytest
import os, shutil
from unittest import mock

from src import CustomerFileReader
from exceptions import InvalidInputError

class TestCustomerFileReader(object):

	def test_init(self):
		cfr = CustomerFileReader('abc.txt')
		assert cfr.input_file == 'abc.txt'

	def test_extract(self):
		mock_data = [
			'{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}',
			'{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}'
		]

		tmp_directory = 'tmp'
		if not os.path.exists(tmp_directory):
			os.makedirs(tmp_directory)

		with open('{}/test_file.txt'.format(tmp_directory), 'w') as f:
			for line in mock_data:
				f.write(line)
				f.write('\n')

		cfr = CustomerFileReader('{}/test_file.txt'.format(tmp_directory))
		customer_list = cfr.extract()

		assert len(customer_list) == 2
		
		assert customer_list[0].user_id == 12
		assert customer_list[0].name == 'Christina McArdle'
		assert customer_list[0].location.latitude == 52.986375
		assert customer_list[0].location.longitude == -6.043701

		assert customer_list[1].user_id == 1
		assert customer_list[1].name == 'Alice Cahill'
		assert customer_list[1].location.latitude == 51.92893
		assert customer_list[1].location.longitude == -10.27699

		shutil.rmtree(tmp_directory)

	def test_extract_invalid_input(self):
		mock_data = [
			'{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}',
			'{"user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}'
		]

		tmp_directory = 'tmp'
		if not os.path.exists(tmp_directory):
			os.makedirs(tmp_directory)

		with open('{}/test_file.txt'.format(tmp_directory), 'w') as f:
			for line in mock_data:
				f.write(line)
				f.write('\n')

		cfr = CustomerFileReader('{}/test_file.txt'.format(tmp_directory))
		
		with pytest.raises(InvalidInputError, message='latitude missing!'):
			cfr.extract()

		shutil.rmtree(tmp_directory)
