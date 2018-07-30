import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from src import FilterCustomers

def main():
	parser = ArgumentParser('filter_customers',
                        	formatter_class=ArgumentDefaultsHelpFormatter,
                          	conflict_handler='resolve')

	parser.add_argument('--input', default='input/customers.txt', help='Input file - containing customers list')

	parser.add_argument('--output', default='STDOUT', help='Output file - will contain filtered customers list')

	parser.add_argument('--origin', default='53.339428,-6.257664', help='Origin location in <latitude,longitude> format')

	parser.add_argument('--distance', default='100', help='Distance in km')

	args = parser.parse_args()
	FilterCustomers(args).invoke()

if __name__ == '__main__':
	sys.exit(main())