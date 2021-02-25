from sys import argv
from random import randint, gauss
from solution import parseInput
from get_intersections import get_intersections


def random_submission(intersections, max_simulation_time):
    no_of_intersections = len(intersections)
    schedules = []
    schedules.append(no_of_intersections)

    for intersection_index in range(len(intersections)):
        schedules.append(intersection_index)

        incoming_streets = intersections[intersection_index]
        no_of_incoming_streets = len(incoming_streets)
        
        schedules.append(no_of_incoming_streets)

        # allocate time to streets
        for street_name in incoming_streets:
            upper_limit = max(10, int(max_simulation_time / len(incoming_streets)))
            time_to_allocate = int(abs(gauss(0, 1) * upper_limit))
            schedules.append(f"{street_name} {time_to_allocate}")
    
    return schedules


def create_submission(schedules, file_name):
    schedules_string = [str(x) for x in schedules]

    with open(file_name, 'w') as file_stream:
        file_stream.write("\n".join(schedules_string))

def main():
    INPUT_FILE_NAME = argv[1]
    overview_dict, streets, cars = parseInput(INPUT_FILE_NAME)

    intersections = get_intersections(streets, overview_dict.get("num_intersections"))

    schedules = random_submission(intersections, overview_dict.get("sim_time"))
    create_submission(schedules, INPUT_FILE_NAME + '_submission')

if __name__ == '__main__':
    main()