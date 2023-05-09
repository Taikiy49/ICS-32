import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    my_dict = {}
    for tup in all_clubs:
        if tup.getSport() not in my_dict:
            my_dict[tup.getSport()] = []
        my_dict[tup.getSport()].append(tup)
    return list(my_dict.values())


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    return sorted(sport, key=lambda sport_tuple: (-sport_tuple.getCount(), sport_tuple.getName()))
            

def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    print(sorted_sports)
    with open('survey_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Team Name", "Sport", "Number of Times Picked"])
        for sport in sorted_sports:
            for club in sport[:3]:
                writer.writerow([club.getCity(), club.getName(), club.getSport(), club.getCount()])

