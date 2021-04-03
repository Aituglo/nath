 

class Station:
    # On définie une station par un tableau pour les lignes dont il fait parti, son nom et un tableau pour l'index de cette station pour chaque ligne auquel il appartient
    def __init__(self, line, name, index):
        self.line = line
        self.name = name
        self.index = index


class Travel:

    def __init__(self):
        self.start_station = None
        self.stop_station = None
        self.travel = []
    # On check si deux stations sont sur la meme ligne
    def is_same_line(self, start, stop):
        for line_start in start.line:
            for line_stop in stop.line:
                if line_start == line_stop:
                    return (True, line_start)
        return (False, None)
    # On récupère la position d'une sation sur une ligne
    def get_line_position(self, station, line):
        for i in range(len(station.line)):
            if station.line[i] == line:
                return station.index[i]
    # On renvoie l'intersection par laquelle on passe si on doti changer de ligne
    def get_good_intersection(self, all_stations):
        start_line = self.start_station.line[0]
        stop_line = self.stop_station.line[0]
        for station in all_stations:
            if start_line in station.line and stop_line in station.line:
                return station
        return False   
    # On récupère une station par son nom
    def get_station_by_name(self, name, all_stations):
        for station in all_stations:
            if station.name == name:
                return station
        return False
    # On récupère une station par sa position
    def get_station_by_index(self, index, line, all_stations):
        for station in all_stations:
            for i in range(len(station.line)):
                if station.line[i] == line and station.index[i] == index:
                    return station
        return False

    # On ajoute à notre trajet les stations entre 2 points
    def add_travel_from_two_point(self, start, stop, line, all_stations, reverse):
        if reverse:
            for index in range(start, stop, -1):
                self.travel.append(self.get_station_by_index(index, line, all_stations))
        else:
            for index in range(start, stop):
                self.travel.append(self.get_station_by_index(index, line, all_stations))

    # On écrit le trajet
    def print_travel(self):
        for station in self.travel:
            print(station.name)

all_stations = []

# Ligne 1

aeroport = Station([1], "Aéroport", [1])
republique = Station([1], "Place de la République", [2])
commercial = Station([1], "Centre commercial", [3])
universite = Station([1, 3], "Université", [4, 3])
gare_centrale = Station([1, 2], "Gare centrale", [5, 3])
marais = Station([1], "Le marais", [6])
tour_fer = Station([1], "La tour de fer", [7])
pont_fou = Station([1], "Pont du Fou", [8])

all_stations.extend([aeroport, republique, commercial, universite, gare_centrale, marais, tour_fer, pont_fou])

# Ligne 2

stade = Station([2], "Stade", [1])
synagogue = Station([2], "Synagogue", [2])
homme_fer = Station([2, 3], "Homme de fer", [4, 5])
lycee = Station([2], "Lycée", [5])
laiterie = Station([2], "Laiterie", [6])
eglise = Station([2], "Eglise", [7])
ilkirch = Station([2], "Ilkirch", [8])

all_stations.extend([stade, synagogue, homme_fer, lycee, laiterie, eglise, ilkirch])

# Ligne 3

piscine = Station([3], "Piscine", [1])
gallia = Station([3], "Gallia", [2])
pharmacie = Station([3], "Pharmacie", [4])
parc = Station([3], "Parc", [6])
jardiniers = Station([3], "Jardiniers", [7])

all_stations.extend([piscine, gallia, pharmacie, parc, jardiniers])



start = input("Choississez votre point de départ : ")
stop = input("Choisissez votre point d'arrivée : ")

travel = Travel()

start_station = travel.get_station_by_name(start, all_stations)
stop_station = travel.get_station_by_name(stop, all_stations)

travel.start_station = start_station
travel.stop_station = stop_station

# On check si les 2 sont sur la meme ligne
same_line = travel.is_same_line(travel.start_station, travel.stop_station)

if same_line[0]:
    # Si ils sont sur la meme ligne on récupere la pos des 2 et on itere pour avoir toutes les stations
    start_position = travel.get_line_position(travel.start_station, same_line[1])
    stop_position = travel.get_line_position(travel.stop_station, same_line[1])
    if start_position < stop_position:
        travel.add_travel_from_two_point(start_position, stop_position + 1, same_line[1], all_stations, False)
    else:
        travel.add_travel_from_two_point(start_position, stop_position - 1, same_line[1], all_stations, True)
else:
    # On récupère l'intersection qu'on va utiliser
    good_intersection = travel.get_good_intersection(all_stations)

    # On fait le chemin du départ jusqu'à l'intersection
    first_travel = travel.is_same_line(travel.start_station, good_intersection)
    start_position = travel.get_line_position(travel.start_station, first_travel[1])
    inter_position = travel.get_line_position(good_intersection, first_travel[1])
    if start_position < inter_position:
        travel.add_travel_from_two_point(start_position, inter_position + 1, first_travel[1], all_stations, False)
    else:
        travel.add_travel_from_two_point(start_position, inter_position - 1, first_travel[1], all_stations, True)

    # On fait le reste du chemin
    second_travel = travel.is_same_line(good_intersection, travel.stop_station)
    stop_position = travel.get_line_position(travel.stop_station, second_travel[1])
    inter_position = travel.get_line_position(good_intersection, second_travel[1])
    if inter_position < stop_position:
        travel.add_travel_from_two_point(inter_position + 1, stop_position + 1, second_travel[1], all_stations, False)
    else:
        travel.add_travel_from_two_point(inter_position - 1, stop_position - 1, second_travel[1], all_stations, True)

travel.print_travel()

