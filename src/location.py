import math

class Location(object):

    PI = 22/7
    RADIUS = 6371

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        self.lat_in_radian = self.__class__.to_radian(self.latitude)
        self.long_in_radian = self.__class__.to_radian(self.longitude)

    def __sub__(self, another_point):
        delta_lat = abs(self.lat_in_radian - another_point.lat_in_radian)
        delta_long = abs(self.long_in_radian - another_point.long_in_radian)

        num1 = math.cos(another_point.lat_in_radian) * math.sin(delta_long)
        num2 = (math.cos(self.lat_in_radian) * math.sin(another_point.lat_in_radian)) - \
               (math.sin(self.lat_in_radian) * math.cos(another_point.lat_in_radian) * math.cos(delta_long))

        numerator = math.sqrt(math.pow(num1, 2) + math.pow(num2, 2))
        denominator = (math.sin(self.lat_in_radian) * math.sin(another_point.lat_in_radian)) +  \
                      (math.cos(self.lat_in_radian) * math.cos(another_point.lat_in_radian) * math.cos(delta_long))

        return self.__class__.RADIUS * math.atan2(numerator, denominator)

    def display(self):
        return 'Lat/Long: {}, {}'.format(self.latitude, self.longitude)

    @classmethod
    def to_radian(cls, degree):
        return degree*(cls.PI/180)
