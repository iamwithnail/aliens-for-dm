import random
class Alien():
    def __init__(self, main_map, id):
        self.can_move = True
        self.alive = True
        self.location = random.choice(main_map.keys())
        self.id = id
    def __eq__(self, other):
        return self.location == other.location
    def __repr__(self):
        return 'Alien %s' % (self.id)

def create_aliens(number_of_aliens):
    """
    Create aliens at random places on the map 
    :param: number_of_aliens  - int representing number of aliens to be created
    :return: 
    """
    # create an alien, assign it to a place.
    # Assume two aliens can be started in the same place.

    return []

def check_for_initial_conflicts(list_of_aliens):
    """
    If any aliens start in the same place, well, that place has had it.  
    
    :param list_of_aliens: 
    :return: 
    """
    for alien in list_of_aliens:
        fights = [other for other in list_of_aliens if other.location == alien.location ]
    return fights


