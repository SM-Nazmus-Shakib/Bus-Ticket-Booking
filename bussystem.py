from bus import Bus
from passenger import Passenger
from admin import Admin
class BusSystem:
    def __init__(self):
        self.buses=[]
        self.passengers=[]
        self.admin=Admin("admin",1234)
    
    def add_bus(self,number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print("Bus already exists")
                return
        self.buses.append(Bus(number, route, seats))
        print("Bus added successfully")
    
    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None

    def book_ticket(self,bus_number, name, phone):
        bus=self.find_bus(bus_number)
        if not bus:
            print("Bus not found.")
            return
        if bus.available_seats() > 0:
           bus.book_seat()
           self.passengers.append(Passenger(name,phone,bus))
           print(f"{name} booked a ticket for: 500tk")
        else:
            print('No seats available')
    
    def show_buses(self):
        for bus in self.buses:
            print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.available_seats()}")
    
    def admin_login(self):
        un=input('Enter your Username[admin]: ')
        pw=int(input('Enter your Passwaord[1234]: '))
        if self.admin.login(un,pw):
            return True
        return False
        
