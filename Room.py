import json
class Room:
    def __init__(self, room_id: str,room_name:str, capacity:int, status:str, projector:str): 
        self.room_id = room_id
        self.room_name = room_name
        self.capacity = capacity
        self.status = status
        self.projector = projector


