from sys import argv
from utils import Reader
from collections import defaultdict

# INPUT_FOLDER = "input_datasets/"
# INPUT_FILE_NAME = argv[1]
# OUTPUT_FILE_NAME = argv[2]

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

# parseInput(INPUT_FILE_NAME)