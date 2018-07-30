import pytest
from unittest import mock

from src import FilterCustomers
from src import Customer

class TestFilterCustomers(object):

	@mock.patch('src.filter_customers.CustomerFileReader')
	def test_init(self, mock_customer_file_reader):
		args = mock.Mock()
		args.input = 'customers.txt'
		args.output = 'STDOUT'
		args.origin = '10,-20'
		args.distance = 50

		mock_customer_file_reader = mock_customer_file_reader.return_value
		mock_customer_file_reader.extract.return_value = []

		fc = FilterCustomers(args)

		assert fc.input == args.input
		assert fc.output == args.output	
		assert fc.origin.__class__.__name__ == 'Location'
		assert fc.origin.latitude == 10.0
		assert fc.origin.longitude == -20.0
		assert fc.distance == float(args.distance)
		assert fc.customer_list == []

	@mock.patch('src.filter_customers.CustomerFileReader')
	def test_process(self, mock_customer_file_reader):
		args = mock.Mock()
		args.input = 'customers.txt'
		args.output = 'STDOUT'
		args.origin = '10,-20'
		args.distance = 250

		mock_customer_file_reader = mock_customer_file_reader.return_value
		mock_customer_file_reader.extract.return_value = [Customer(1, 'Mac', 10, 60), Customer(2, 'John', 10, -22), Customer(3, 'Doe', 10, -21)]

		filtered_customers = FilterCustomers(args).process()

		assert len(filtered_customers) == 2
		assert filtered_customers[0].user_id == 3
		assert filtered_customers[1].user_id == 2

		

