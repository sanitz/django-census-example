class Census(object):
    def __init__(self, citizens):
        self.citizens = citizens

    def sum(self):
        return len(self.citizens)

    def median_age(self):
        return sum([c.age for c in self.citizens]) / self.sum()
