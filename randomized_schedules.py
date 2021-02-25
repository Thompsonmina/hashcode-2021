from sys import argv
from utils import Reader
from random import randint, gauss
from collections import defaultdict


def parseInput(filepath):
	reader = Reader(filepath)
	overview_line = [int(x) for x in reader.get_first_line().split()]
	overview_dict = {
						"sim_time": overview_line[0],
						"num_intersections": overview_line[1],
						"num_streets": overview_line[2],
						"num_cars": overview_line[3],
						"finishscore": overview_line[4]
	}

	streets = defaultdict(list)
	for streetdetails in reader.get_n_sections(start=2, sectionsize=1, n=overview_dict["num_streets"]):
		streetdetails = streetdetails[0].split()
		# print(streetdetails)

		streets[streetdetails[2]].append(tuple(int(x) for x in [streetdetails[0], streetdetails[1]]))		
		streets[streetdetails[2]].append(int(streetdetails[3]))

	cars = [0 for x in range(overview_dict["num_cars"])]

	carlines = reader.get_n_sections(start=overview_dict["num_streets"] + 2, sectionsize=1, n=overview_dict["num_cars"] + overview_dict["num_streets"])
	for i, carsdetails in enumerate(carlines):
		# print("here")
		carsdetails = carsdetails[0].split()
		# print(carsdetails)
		cars[i] = carsdetails[1:]

	
	# a car is a list with each index as its name and it contains the routes it will pass
	return overview_dict, streets, cars


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

def random_submission(intersections, simulation_time):
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
            upper_limit = simulation_time // len(incoming_streets)
            time_to_allocate = randint(1, upper_limit)
            
            # time_to_allocate = int(abs(gauss(0, upper_limit)))
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