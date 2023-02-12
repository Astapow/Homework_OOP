class Element:
    def __init__(self, melting_point, boiling_point):
        self.melting_point = melting_point
        self.boiling_point = boiling_point

    def agg_state(self, temp, scale='C'):
        self.melting_point = self.convert_to_c(temp=self.melting_point, scale=scale)
        self.boiling_point = self.convert_to_c(temp=self.boiling_point, scale=scale)

        if temp > self.melting_point and temp < self.boiling_point:
            return f'melt'
        elif temp > self.boiling_point:
            return f'boil'
        else:
            return f'in its aggregate state'

    def convert_to_c(self, temp, scale='C'):
        if scale == 'K':
            return temp + 273, 15
        elif scale == 'F':
            return (temp * (9 / 5)) + 32
        else:
            return temp


if __name__ == '__main__':
    h2o = Element(melting_point=0, boiling_point=100)
    print(h2o.agg_state(temp=1200, scale='F'))
    print(h2o.convert_to_c(temp=800, scale='C'))
