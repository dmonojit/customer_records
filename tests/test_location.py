import pytest

from src import Location

class TestLocation(object):

	def test_init(self):
		l = Location(10, 20)
		pi = 22/7

		assert l.latitude == 10
		assert l.longitude == 20
		assert l.lat_in_radian == 10 * (pi / 180)
		assert l.long_in_radian == 20 * (pi / 180)

	def test_distance(self):
		l1 = Location(10, 20)
		l2 = Location(10, 20)

		assert (l1 - l2) == 0.0

		l3 = Location(10, 20.5)

		assert 50 < (l1 - l3) < 100
		