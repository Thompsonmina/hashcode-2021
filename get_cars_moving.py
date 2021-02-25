import math
def get_cars_moving(street_frequency, intersections, total_simulation_time):
    intersections_schedule = []
    for i in range(0,len(intersections)):
        interct = []
        temporary_dict = {}
        for j in range(0, len(intersections[i])):
            for key in street_frequency:
                if key == intersections[i][j]:
                    interct.append(street_frequency[key])
                else:
                    continue
        for k in range(0, len(interct)):
            for m in range(0, len(intersections[i])):
                if(interct[k]==0):
                    continue
                else:
                    temporary_dict[intersections[i][m]] = math.floor((interct[k]/sum(interct)) * total_simulation_time)
        intersections_schedule.append(temporary_dict)
