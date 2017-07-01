


def run_all(mapfile, number_of_aliens):
    import sys
    from data_loader import map_reader
    from place_management import world_exists
    from alien_management import create_aliens, conflict_handler, move_alien, are_conflicts, check_for_initial_conflicts
    try:
        main_map = map_reader(mapfile)
    except IOError:
        print "File %s does not exist " % (mapfile)
        sys.exit()

    number_of_moves = 0
    active_aliens = create_aliens(number_of_aliens, main_map)
    active_aliens, main_map = check_for_initial_conflicts(active_aliens, main_map)

    while number_of_moves <=10000 and world_exists(main_map):
        #filter out dead and stuck aliens
        current_aliens = filter(lambda x: x.can_move == True and x.alive, active_aliens)
        for index, alien in enumerate(current_aliens):
            alien, moved = move_alien(alien, main_map)
            aliens_in_same_location = are_conflicts(alien, current_aliens)
            if aliens_in_same_location:
                main_map, _ = conflict_handler(aliens_in_same_location, main_map, alien.location)
        #loop through the list of aliens and move them randomly

    print "The survivors may envy the dead."
    print main_map


