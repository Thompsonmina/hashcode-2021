def get_intersections(street_dictionary, no_of_intersections):
    intersections = []
    for i in range (0, (no_of_intersections)):
        intersect = []
        for key in street_dictionary:
            if(street_dictionary[key][0][1] == i):
                intersect.append(key)
            else:
                continue
        intersections.append(intersect)
    return intersections

