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

<<<<<<< HEAD
=======
# print(get_intersections({'malik' : [(1,2), "11"], 'tunde' : [(1,0), "11"], 'vermont' : [(1,1), "11"], 'nunu' : [(1,3), "11"]}, 4))
>>>>>>> 9164d48b12e980126e14f61eff502dd8111179b4
