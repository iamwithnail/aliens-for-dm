def location_reader(location_fragment):
    """
    Takes in a location fragment in the format direction1=place1 direction2=place2
    :param location_fragment: 
    :return: 
    """


def place_ok(place_string):
    print place_string
    special_characters = ['=', '!']
    if any(character in place_string for character in special_characters):
        return False
    else:
        return True


def row_handler(data_row):
    """
    Assume place is always in position 0 
    Need to assume that the place doesn't have an equals sign in, so check if it's ok 
    :param data_row: Data row string, in format current_place direction1=place1 direction2=place2
    :return: 
    """
    split_row = data_row.split(' ')
    place = split_row[0]
    if not place_ok(place):
        raise AttributeError('Place name should not contain any special characters')
    remainder = split_row[1:]
    return {place: dict(item.split('=') for item in remainder)
}

def file_handler(file_location):
    """
    Assume each line terminated with a newline character
    
    :param file_location: string 
    :return: list of rows  
    """
    with open(file_location) as data:
        return data.read().splitlines()

def map_reader(file_location):
    """Reads in a map file; assumes that the map is a series of rows separated """
    data = file_handler(file_location)
    map_dict = {}
    for line in data:
        #Assume that duplicate placenames should be overwritten, but these could be flagged or raised.
        map_dict.update(row_handler(line))
    return map_dict

