# Constant

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a guitar."""
        return f"{self.name}, Made in {self.year} year, ${self.cost}"

#

    # overloading the operator <
    def __lt__(self, other):
        """sort guitar by year"""
        return self.year < other.year
#
#
# def run_test():
#     """ simple run test or demo on guitar class"""
#     name = "Gibson L-5 CES"
#     year = 1922
#     cost = 16035.40
#
#     guitar = Guitar(name, year, cost)
#     other = Guitar("Another Guitar", 2012, 1512.9)
#
#
#
#
# if __name__ == '__main__':
#     run_test()
