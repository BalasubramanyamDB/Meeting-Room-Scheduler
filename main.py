import json
from Operations import booking,addToRoomsDB, bookingForRecurringMeeting
from Room import Room
while True:
    print("Enter id")
    id = input()
    with open('users.json', 'r') as file:   
        data = json.load(file)
    role = ""
    for i in range(len(data)):
        print(data[i]["id"])
        if  data[i]["id"] == id:
            role = data[i]["role"]
            break
    if not role:
        print("No data found") 
        break 
    if role == "admin":
        print("1.ADD ROOM\n2.BOOK ROOM\n3.BOOK RECURRING MEETING")
        print("Enter choice")
        op = int(input())
        if op == 1:
            print("ADD ROOM")
            print("Enter Room ID:")
            id = input()
            print("Enter Room Name")
            name = input()
            print("Enter Capacity")
            capacity = int(input())
            print("Enter status")
            status = input()
            print("Is Projector available:")
            projector =input()
            new_room = Room(id, name, capacity, status, projector)
            print(new_room)
            addToRoomsDB(new_room)

        if op == 2:
            print("BOOK ROOM")
            print("Enter Room ID:")
            id = input()
            print("Enter date(YYYY-MM-DD):")
            date = input()
            print("Enter start time(HH:MM:SS)")
            st_time = input()
            print("Enter end time(HH:MM:SS)")
            end_time = input()
            booking(id, date, st_time, end_time)
        
        if op == 3:
            print("BOOK RECURRING MEETING ROOM")
            print("Enter Room ID:")
            id = input()
            print("Enter start date(YYYY-MM-DD):")
            st_date = input()
            print("Enter end date(YYYY-MM-DD):")
            end_date = input()
            print("Enter start time(HH:MM:SS)")
            st_time = input()
            print("Enter end time(HH:MM:SS)")
            end_time = input()
            bookingForRecurringMeeting(id, st_time, end_time,st_date, end_date)


            
    else:
        print("BOOK ROOM")
        print("Enter Room ID:")
        id = input()
        print("Enter date(YYYY-MM-DD):")
        date = input()
        print("Enter start time(HH:MM:SS)")
        st_time = input()
        print("Enter end time(HH:MM:SS)")
        end_time = input()
        booking(id, date, st_time, end_time)

    

    

                

