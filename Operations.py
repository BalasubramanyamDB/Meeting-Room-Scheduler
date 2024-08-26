import json
from datetime import datetime
import time
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
        if room_id in tmp:
            booked_room_data = booked_rooms[i][room_id]

    if not booked_room_data:
        new_data = {room_id : {date: [[start_time, end_time]]}}
        booked_rooms.append(new_data)
        with open("bookings.json", "w") as booking_json:
            json.dump(booked_rooms, booking_json, indent = 4)
    
    else:
        meetings_scheduled = []
        for key in booked_room_data.keys():
            if key == date:
                meetings_scheduled = booked_room_data[date]
                break
        if not meetings_scheduled:
            new_data =  [[start_time, end_time]]
            booked_room_data[date] = new_data
            with open("bookings.json", "w") as booking_json:
                json.dump(booked_rooms, booking_json, indent = 4)
            return
        print(meetings_scheduled)
        meeting_st_time = date + " " + start_time
        meeting_end_time = date + " " + end_time
        st_obj = datetime.strptime(meeting_st_time, '%Y-%m-%d %H:%M:%S')
        end_obj = datetime.strptime(meeting_end_time, '%Y-%m-%d %H:%M:%S')
        epoch_st = int(time.mktime(st_obj.timetuple()))
        epoch_end = int(time.mktime(end_obj.timetuple()))
        for i in range(len(meetings_scheduled)): 
            st = meetings_scheduled[i][0]
            end =meetings_scheduled[i][1]
            cur_st = date + " " + st
            cur_end = date + " " + end
            meeting_st_obj = datetime.strptime(cur_st, '%Y-%m-%d %H:%M:%S')
            meeting_end_obj = datetime.strptime(cur_end, '%Y-%m-%d %H:%M:%S')
            cur_st_epoch = int(time.mktime(meeting_st_obj.timetuple()))
            cur_end_epoch = int(time.mktime(meeting_end_obj.timetuple()))
            if not((epoch_st < cur_st_epoch and epoch_end <= cur_st_epoch) or (epoch_st >= cur_end_epoch and epoch_end>cur_end_epoch)):
                print("Conflict")
                checkAvailableRoomOnConflict(date ,start_time, end_time)
                return 
        booked_room_data[date].append([start_time, end_time])
        print("BOOKED")
        with open('bookings.json','w') as file:
            json.dump(booked_rooms, file, indent=4)
        

def checkAvailableRoomOnConflict(date ,start_time, end_time):
    meeting_st_time = date + " " + start_time
    meeting_end_time = date + " " + end_time
    st_obj = datetime.strptime(meeting_st_time, '%Y-%m-%d %H:%M:%S')
    end_obj = datetime.strptime(meeting_end_time, '%Y-%m-%d %H:%M:%S')
    epoch_st = int(time.mktime(st_obj.timetuple()))
    epoch_end = int(time.mktime(end_obj.timetuple()))
    with open("bookings.json",'r') as file:
        data = json.load(file)
    available_rooms = []
    for i in range(len(data)):
        room = data[i]
        for key, value in room.items():
            if date in value.keys():
                for d, val in value.items():
                    if date != d:
                        continue
                    flag = True
                    for i in range(len(val)):
                        st = val[i][0]
                        end =val[i][1]
                        cur_st = date + " " + st
                        cur_end = date + " " + end
                        meeting_st_obj = datetime.strptime(cur_st, '%Y-%m-%d %H:%M:%S')
                        meeting_end_obj = datetime.strptime(cur_end, '%Y-%m-%d %H:%M:%S')
                        cur_st_epoch = int(time.mktime(meeting_st_obj.timetuple()))
                        cur_end_epoch = int(time.mktime(meeting_end_obj.timetuple()))
                        if not ((epoch_st < cur_st_epoch and epoch_end <= cur_st_epoch) or (epoch_st >= cur_end_epoch and epoch_end>cur_end_epoch)):
                            flag = False
                            break
                    if flag:
                        available_rooms.append(key)
            else:
                available_rooms.append(key)
    if available_rooms:
        chooseFromAvailableRooms(available_rooms, date ,start_time, end_time)
    else:
        print("No room available")

def chooseFromAvailableRooms(available_rooms, date ,start_time, end_time):
    print("Other available rooms:", available_rooms)
    print("Enter room to be selected:")
    room_id = input()
    if room_id not in available_rooms:
        print("Room not available:", room_id)
    else:
        booking(room_id, date ,start_time, end_time)


def bookingForRecurringMeeting(room_id,  start_time, end_time, start_date, end_date):
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

    meeting_st = start_date + " " + end_time
    meeting_end = end_date + " " + end_time
    st_obj = datetime.strptime(meeting_st, '%Y-%m-%d %H:%M:%S')
    end_obj = datetime.strptime(meeting_end, '%Y-%m-%d %H:%M:%S')
    epoch_st = int(time.mktime(st_obj.timetuple()))
    epoch_end = int(time.mktime(end_obj.timetuple()))

    print("bkd", booked_room_data)
    if not booked_room_data:
        # new_data = {}
        # new_data[room_id] = {}
        data = {}
        while epoch_st != epoch_end: 
            date = datetime.fromtimestamp(epoch_st)
            date_str = date.strftime('%Y-%m-%d')
            data[date_str] = [[start_time, end_time]]
            epoch_st += 86400
            print("new data", data)
        booked_rooms.append({room_id : data})
        print("bor",booked_rooms)
        with open("bookings.json", "w") as booking_json:
            json.dump(booked_rooms, booking_json, indent = 4)
        print("BOOKED")

    else:
        meetings_scheduled = []
        print(booked_room_data)
        for key in booked_room_data.keys():
            if key == date:
                meetings_scheduled = booked_room_data[date]
                break
        if not meetings_scheduled:
            new_data =  [[start_time, end_time]]
            booked_room_data[date] = new_data
            with open("bookings.json", "w") as booking_json:
                json.dump(booked_rooms, booking_json, indent = 4)
            return
        


        for i in range(len(meetings_scheduled)): 
            st = meetings_scheduled[i][0]
            end =meetings_scheduled[i][1]
            cur_st = date + " " + st
            cur_end = date + " " + end
            meeting_st_obj = datetime.strptime(cur_st, '%Y-%m-%d %H:%M:%S')
            meeting_end_obj = datetime.strptime(cur_end, '%Y-%m-%d %H:%M:%S')
            cur_st_epoch = int(time.mktime(meeting_st_obj.timetuple()))
            cur_end_epoch = int(time.mktime(meeting_end_obj.timetuple()))
            if( not (epoch_st < cur_st_epoch and epoch_end < cur_st_epoch) or (epoch_st > cur_end_epoch and epoch_end>cur_end_epoch)):
                print("Conflict")
                checkAvailableRoomOnConflict(date ,start_time, end_time)
                return 