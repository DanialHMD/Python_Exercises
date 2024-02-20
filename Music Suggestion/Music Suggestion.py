all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = {"age": age, "city": city, "albums": albums}


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = {"artist":artist_name , "genre":genre , "tracks":tracks}


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    return sum(all_albums[album]["tracks"] for user, userdata in all_users.items() if user == username for album in userdata["albums"] if all_albums.get(album, {}).get("artist") == artist_name)

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    return sum(all_albums[album]["tracks"] for user, userdata in all_users.items() if user == username for album in userdata["albums"] if all_albums.get(album, {}).get("genre") == genre)


def query_age_artist(age, artist_name, all_users, all_albums):
    return sum(all_albums[album]["tracks"] for user, userdata in all_users.items() if userdata["age"] == age for album in userdata["albums"] if all_albums.get(album, {}).get("artist") == artist_name)


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    return sum(all_albums[album]["tracks"] for user, userdata in all_users.items() if userdata["age"] == age for album in userdata["albums"] if all_albums.get(album, {}).get("genre") == genre)


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    return sum(all_albums[album]["tracks"] for user, user_data in all_users.items() if user_data["city"] == city for album in user_data["albums"] if all_albums.get(album, {}).get("artist") == artist_name)


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    return sum(all_albums[album]["tracks"] for user, user_data in all_users.items() if user_data["city"] == city for album in user_data["albums"] if all_albums.get(album, {}).get("genre") == genre)
    
    
