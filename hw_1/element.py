class Element:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point
        self.boiling_point = boiling_point

    def agg_state(self, temp, scale='C'):
        temp = self.convert_to_c(temp, scale)
        if temp >= self.boiling_point:
            return 'Gaz'
        elif self.melting_point <= temp < self.boiling_point:
            return 'Liquid'
        else:
            return 'Solid'

    def convert_to_c(self, temp, scale='C'):
        if scale == 'K':
            return temp - 273.15
        elif scale == 'F':
            return (temp - 32) * (5 / 9)
        else:
            return temp


if __name__ == '__main__':
    h2o = Element(melting_point=0, boiling_point=100)
    selenium = Element(221, 685)
    print(h2o.agg_state(temp=1200, scale='F'))
    print(selenium.agg_state(222))
