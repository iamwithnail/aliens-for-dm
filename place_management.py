def destroy_related_roads(place, world_map):
    """
    Need to find the related roads in and out of a place so that those links can be moved from the graph dict. 
    :param place: 
    :return: 
    """
    #list of city names
    try:
        related_cities = [value for key, value in world_map[place].iteritems()]
    except KeyError:
        print "City already destroyed..."
        return world_map
    #print related_cities
    #ditch the link to the destroyed city
    try:
        for city in related_cities:
            world_map[city] = {key:value for key, value in world_map[city].items() if value != place}
    except KeyError, e:
         print KeyError, e
    return world_map


def world_exists(world_map):
    """
    Check that there still more than 0 available entries in the world map. 
    :param world_map: 
    :return: 
    """
    if len(world_map)>0:
        return True
    else:
        return False
