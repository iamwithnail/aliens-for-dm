from data_loader import map_reader

def world_exists(world_map):
    if len(world_map)>0:
        return True
    else:
        return False

def __main__(mapfile, number_of_aliens):
    try:
        main_map = map_reader(mapfile)
    except IOError:
        print "File %s does not exist " % (mapfile)

    # create_initial_aliens
    # fights = check_for_initial_conflicts
    # pass the fights to the normal conflict handling system
    number_of_moves = 0

    active_aliens = []
    while number_of_moves <=10001 and world_exists(main_map):
        #loop through the list of aliens and move them randomly
        pass
        for


