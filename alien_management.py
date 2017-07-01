class Alien():
    def __init__(self, initial_location):
        self.can_move = True
        self.alive = True
        self.location = initial_location


def create_aliens(number_of_aliens):
    """
    Create aliens at random places on the map 
    :param: number_of_aliens  - int representing number of aliens to be created
    :return: 
    """
    # create an alien, assign it to a place.

