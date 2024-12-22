from pakuri import Pakuri
from pakudex import Pakudex
def pakuri_program():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    #asking for the max capacity
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity >= 0:
                pakudex = Pakudex(capacity)
                print(f"The Pakudex can hold {capacity} species of Pakuri.")
                break
            else:
                print("Please enter a valid size.")
                #negative numbers cant work

        except:
            print("Please enter a valid size.")

    num = 0
    while True:
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            #simply lists the pakuri in the order inputted
            species_list = pakudex.get_species_array()
            if species_list:
                print("Pakuri In Pakudex:")
                for i, species in enumerate(species_list, start=1):
                    print(f"{i}. {species}")
            else:
                print("No Pakuri in Pakudex yet!")

        elif choice == "2":
            #shows the pakuri and its attributed
            species_to_display = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species_to_display)
            if stats:
                print(f"Species: {species_to_display}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

        elif choice == "3":
            #if capacity is full then error
            if num == capacity:
                print("Error: Pakudex is full!")
            else:
            #adds the pakuri to the list
                species_to_add = input("Enter the name of the species to add: ")
                success = pakudex.add_pakuri(species_to_add)
                if success:
                    print(f"Pakuri species {species_to_add} successfully added!")
                    num+=1

                else:
                    print("Error: Pakudex already contains this species!")

        elif choice == "4":
            #increases attributes of the pakuri
            species_to_evolve = input("Enter the name of the species to evolve: ")
            success = pakudex.evolve_species(species_to_evolve)
            if success:
                print(f"{species_to_evolve} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == "5":
            #sorts the pakuri alphabetically
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == "6":
            #exits the loop
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    pakuri_program()