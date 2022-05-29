class Room:
    def __init__(self, number, capacity, entry_fee, playlist):
        self.number = number
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.playlist = playlist
            
    def open_room(self, room_number, room_capacity, room_entry_fee, room_playlist):
        self.number = room_number
        self.capacity = room_capacity
        self.entry_fee = room_entry_fee
        self.playlist = room_playlist.copy()
        
    def check_availability(self, room, guests):
        if room.capacity - guests < 0:
            return False
        else:
            return True
        
    def check_in(self, room, guests):
        room.capacity -= len(guests)
        self.take_payment(room, guests)
        if self.guest_fav_song(room, guests):
            return "Whoo!"
        
        
    def check_out(self, room, guests):
        room.capacity += len(guests)
        
    def take_payment(self, room, guests):
        for guest in guests:
            guest.wallet -= room.entry_fee
            
    def guest_fav_song(self, room, guests):
        songs = [song.name for song in room.playlist]
    
        for guest in guests:
            for song in songs:
                if song == guest.fav_song:
                    return True
        return False