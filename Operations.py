import json

def addToRoomsDB(new_room):
    new_data = {
        "id":new_room.room_id,
        "name":new_room.room_name,
        "capacity":new_room.capacity,
        "status":new_room.status,
        "projector":new_room.projector
    }
    with open("rooms.json", 'r') as file:
        data = json.load(file)
    print(data)
    data.append(new_data)
    print(data)
    with open("rooms.json", 'w') as file:
        json.dump(data, file, indent=4)


def booking(room_id, date ,start_time, end_time):
    with open("rooms.json", "r") as file:
        rooms = json.load(file)
    is_available = False
    for i in range(len(rooms)):
        if rooms[i]["id"] == room_id:
            is_available = True
    if not is_available:
        return False 
    with open("bookings.json", "r") as booking_json:
        booked_rooms = json.load(booking_json)
    booked_room_data = ""
    for i in range(len(booked_rooms)):
        tmp = booked_rooms[i].keys()
        print(tmp)
        if room_id in tmp:
            booked_room_data = booked_rooms[i][room_id]
    print(booked_room_data,"nn")
    if not booked_room_data:
        new_data = {room_id : {date: [[start_time, end_time]]}}
        booked_rooms.append(new_data)
        with open("bookings.json", "w") as booking_json:
            json.dump(booked_rooms, booking_json, indent = 4)
    
    else:
        pass
