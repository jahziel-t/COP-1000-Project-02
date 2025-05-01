# Define the list of allowed vehicles
AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan'
]

# Function to print all allowed vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print("\n********************************")
# Function to search for a specific vehicle
def search_vehicle():
    search_term = input("\nPlease Enter the full Vehicle name: ").strip()
    found = False

    for vehicle in AllowedVehiclesList:
        if search_term.lower() == vehicle.lower():
            print(f"\n✔ '{vehicle}' is an authorized vehicle.")
            found = True
            break

    if not found:
        print(f"\n✘ '{search_term}' is not an authorized vehicle, "
              "if you received this in error please check the spelling "
              "and try again.")

    print("\n********************************")

# Function to display the menu
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. Exit")

# Main function to handle the menu selection and program flow
def main():
    while True:
        display_menu()
        
        # Get user input for menu choice
        try:
            choice = int(input("Enter your choice (1, 2, or 3.): "))
            if choice == 1:
                print_vehicles()
            elif choice == 2:  # Correct indentation for the elif block
                search_vehicle()
            elif choice == 3:
                print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
                break  # Exit the loop and end the program                    
            else:
                print("Invalid choice, please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
