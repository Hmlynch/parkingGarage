text = {
    "garage_full": "Sorry, our parking garage is full! Please come back soon.",
}

class CarGarage:
    def __init__(self, tickets=[i for i in range(1,101)], parking_spaces=[i for i in range(100)], price=1.20):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {100:{"paid":"False in garage", 'price': "1.20 per hour"}, 99:{"paid":"False in garage", 'price': "1.70 per hour"}}
        self.price = price
        

    def take_ticket(self):
        if self.tickets:
            ticket=self.tickets.pop()
            self.parking_spaces.pop()
            print(f"Your ticket number is {ticket}")
            self.current_ticket[ticket] = {"paid": "False in garage", 'price': self.price}
        else:
            print(text["garage_full"])
    
    def pay_for_parking(self):
        while True:
            tic_num = int(input("What is your ticket number? "))
            if tic_num in self.tickets:
                print("Are you sure that's the right number?[Enter]")
            elif self.current_ticket[tic_num]['paid'] == "True Leave Garage":
                print("""
                    Thank you, have a nice day!""")
            else:
                print("You have not payed yet.")
                break
        hours = input("And how many hours were you parked today? ")
        while True:
            try:
                if float(hours): 
                    print(f'{"~="*8}')
                    print(f'Your total for the day is: ${float(hours)*self.current_ticket[tic_num]["price"]}')
                    print(f'{"~="*8}')

                    input("""Lucky you! Our currency acceptance machine is broken and you don't have to pay.\n 
                    You have 15 minutes to leave!
                        [Press Enter]""")
                    self.current_ticket['paid'] = 'True Leave Garage'
                    print("""
                    Thank you, have a nice day!""")
                    break
            except ValueError:
                hours = input("Sorry, that wasn't a number. Try again.")
        self.tickets.append(len(self.tickets)+1)
        self.parking_spaces.append(len(self.parking_spaces)+1)


The_Parking_Garage = CarGarage()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
            
        
The_Parking_Garage.pay_for_parking()