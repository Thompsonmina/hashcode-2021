from random import randint

def random_submission(intersections):
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
            time_to_allocate = randint(0, 10)
            schedules.append(f"{street_name} {time_to_allocate}")
    
    return schedules


def create_submission(schedules, file_name):
    schedules_string = [str(x) for x in schedules]

    with open(file_name, 'w') as file_stream:
        file_stream.write("\n".join(schedules_string))

def main():
    intersections = [['rome', 'chater'], ['paris', 'ikeja']]
    schedules = random_submission(intersections)
    create_submission(schedules, 'testing')

if __name__ == '__main__':
    main()