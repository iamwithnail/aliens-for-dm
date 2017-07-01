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
    def __hash__(self):
        return hash(self.location)
    def kill(self):
        self.alive = False
        self.can_move = False

def create_aliens(number_of_aliens, world_map):
    """
    Create aliens at random places on the map 
    :param: number_of_aliens  - int representing number of aliens to be created
    :return: 
    """
    # create an alien, assign it to a place.
    # Assume two+ aliens can be started in the same place.

    return [Alien(world_map, id) for id in xrange(0,number_of_aliens)]


def conflict_handler(kill_list,world_map, location):
    """
    Aliens in same location kill each, remove that location from world map and all references to it 
    elsewhere in the world map. 
    :param kill_list: 
    :param world_map: 
    :param location: 
    :return: 
    """
    from place_management import destroy_related_roads
    destroy_related_roads(location,world_map)
    print "%s has been destroyed by %s!" %(location, " and ".join([str(value) for value in kill_list]))
    world_map.pop(location)
    for alien in kill_list:
        alien.kill()
    return world_map, kill_list

def are_conflicts(alien, list_of_aliens):
    aliens_in_same_location = filter(lambda x: x.location == alien.location, list_of_aliens)

    print aliens_in_same_location
    if len(aliens_in_same_location) > 1:
        return aliens_in_same_location
    else:
        return []

def check_for_initial_conflicts(list_of_aliens, world_map):
    """
    If any aliens start in the same place, well, that place has had it.  
    
    :param list_of_aliens: 
    :return: modified list of aliens
    """
    for alien in list_of_aliens:
        #check here that we haven't killed them on previous iteration.
        if alien.alive:
            aliens_in_same_location = are_conflicts(alien, list_of_aliens)
            if aliens_in_same_location:
                conflict_handler(aliens_in_same_location,world_map, alien.location)
    return list_of_aliens, world_map


def move_alien(alien, world_map):
    """
    Moves the alien in a random direction.   
    :param alien: Alien object
    :param world_map:  Current version of world map
    :return: tuple of alien object and Boolean of whether or not we were able to move it. 
    """
    print alien.location
    #print world_map
    import random
    if alien.can_move:
        directions = world_map[alien.location]
        try:
            alien.location = directions[random.choice(directions.keys())]
            return alien, True
        except IndexError:
            #Caused by no available directions to move.
            alien.can_move = False
            return alien, False







