from .file_readers import CustomerFileReader
from .location import Location
from .file_writer import open_file

class FilterCustomers(object):
	def __init__(self, args):
		self.input = args.input
		self.output = args.output
		self.origin = Location(*[float(x) for x in args.origin.split(',')])
		self.distance = float(args.distance)
		self.customer_list = CustomerFileReader(args.input).extract()

	def invoke(self):
		filtered_customers = self.process()
		self._write_to_output(filtered_customers)

	def process(self):
		filtered_customers = list(filter(lambda customer: customer.within(self.distance, self.origin), self.customer_list))
		filtered_customers.sort(key=lambda customer: customer.distance(self.origin))

		return filtered_customers

	def _write_to_output(self, customer_list):
		with open_file(self.output) as f:
			if customer_list:
				f.write('\n'.join([customer.display() for customer in customer_list]))
				f.write('\n')
			else:
				f.write('No customers found with {} km from {}\n'.format(self.distance, self.origin.display()))
