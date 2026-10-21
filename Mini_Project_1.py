# Name:Tejaswini Dhakulkar
# Roll no.37
# Flight Management System using Searching and Sorting

flights = [
    {"number": "F101", "source": "Pune",
     "destination": "Delhi", "price": 4500, "duration": 2.5},

    {"number": "F102", "source": "Mumbai",
     "destination": "Goa", "price": 2500, "duration": 1.2},

    {"number": "F103", "source": "Pune",
     "destination": "Bangalore", "price": 3500, "duration": 1.8},

    {"number": "F104", "source": "Delhi",
     "destination": "Mumbai", "price": 5000, "duration": 2.3},

    {"number": "F105", "source": "Mumbai",
     "destination": "Chennai", "price": 4000, "duration": 2.0}
]


# Display all flights
def display_flights(data):
    print("\nFlight No.  Source       Destination  Price  Duration")
    print("-" * 60)

    for flight in data:
        print(
            f"{flight['number']:<11}"
            f"{flight['source']:<13}"
            f"{flight['destination']:<13}"
            f"Rs.{flight['price']:<6}"
            f"{flight['duration']} hrs"
        )


# Linear search by flight number
def search_flight(number):
    for flight in flights:
        if flight["number"].lower() == number.lower():
            print("\nFlight Found:")
            display_flights([flight])
            return

    print("\nFlight not found!")


# Bubble sort by ticket price
def sort_flights():
    sorted_flights = flights.copy()
    n = len(sorted_flights)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_flights[j]["price"] > sorted_flights[j + 1]["price"]:
                sorted_flights[j], sorted_flights[j + 1] = (
                    sorted_flights[j + 1],
                    sorted_flights[j]
                )

    print("\nFlights Sorted by Price (Low to High):")
    display_flights(sorted_flights)


# Search flights by destination
def search_destination(destination):
    found = [
        flight for flight in flights
        if flight["destination"].lower() == destination.lower()
    ]

    if found:
        print("\nFlights to", destination.title())
        display_flights(found)
    else:
        print("\nNo flights found for this destination!")


# Main menu
while True:
    print("\n===== FLIGHT MANAGEMENT SYSTEM =====")
    print("1. Display All Flights")
    print("2. Search by Flight Number")
    print("3. Search by Destination")
    print("4. Sort Flights by Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_flights(flights)

    elif choice == "2":
        number = input("Enter flight number: ").strip()
        search_flight(number)

    elif choice == "3":
        destination = input("Enter destination: ").strip()
        search_destination(destination)

    elif choice == "4":
        sort_flights()

    elif choice == "5":
        print("Thank you for using Flight Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
