from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity=20):
        self.__capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.__capacity

    def get_species_array(self):
        if not self.pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]
#actually gets the stats for the pakuri
    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None


    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda x: x.get_species())
#sorts the pakuri alphabetically
    def add_pakuri(self, species):
        if len(self.pakuri_list) >= self.__capacity:
            return False

        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return False

        new_pakuri = Pakuri(species)
        self.pakuri_list.append(new_pakuri)
        return True
#adds the pakuri to the list
    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
    #evolves the pakuri