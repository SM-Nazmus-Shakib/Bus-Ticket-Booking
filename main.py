from bussystem import BusSystem
def admin_menu(self):
    while True:
        print("Welcome Admin!")
        print("1.Add Bus")
        print("2.View All Buses")
        print("3.Exit")
    
        choice=int(input('Enter Your Choice: '))
        if choice==1:
            number=int(input("Enter bus number: "))
            route=input("Enter bus route: ")
            seats=int(input("Enter total seats: "))
            self.add_bus(number,route,seats)
        elif choice==2:
            self.show_buses()
        elif choice==3:
            break
my_system=BusSystem()
while True:
    print("-------Welcome!-------")
    print("1.Admin Login")
    print("2.Book Ticket")
    print("3.View Buses")
    print("4.Exit")
    choice=int(input('Enter Your Choice: '))
    if choice==1:
        if my_system.admin_login():
            admin_menu(my_system)
        else:
            print('Login Failed!..Try Again')
    elif choice==2:
        bus_number=int(input("Enter bus number: "))
        name=input("Enter your name: ")
        phone=input("Enter your phone number: ")
        my_system.book_ticket(bus_number,name,phone)
    elif choice==3:
        my_system.show_buses()
    elif choice==4:
        break
    else:
        print('Invalid Choice!')
            