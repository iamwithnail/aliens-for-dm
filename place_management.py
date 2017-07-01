def destroy_related_roads(place, world_map):
    """
    Need to find the related roads in and out of a place so that those links can be moved from the graph dict. 
    :param place: 
    :return: 
    """
    #list of city names
    related_cities = [value for key, value in world_map[place].iteritems()]
    print related_cities
    #ditch the link to the destroyed city
    for city in related_cities:
        world_map[city] = {key:value for key, value in world_map[city].items() if value != place}
    return world_map


def destroy_place(place):
    """
    Destroying a place removes the place from the map.
    :param place: 
    :return: 
    """
