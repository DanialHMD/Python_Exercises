# Music Suggestion🎶
In this exercise you have to write a code which contains functions of extracting data from dictionaries for music suggesting AI.

The data is stored in two dictionaries:
1. `all_user`
2. `all_albums`

You have to create two functions that each of them add data to the dictionaries above:
### 1. **USER**:

Define `add_user()` function the way that it takes `username`, `age`, `city`, a list of purchased albums (`albums`), dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as inputs, and adds the desired user to the dictionary of `all_users`.
   
   <details>
     <summary>See how to write it.</summary>
     
  ```python
def add_user(username, age, city, albums, all_users, all_albums):
  pass
  ```
   </details>
   
### 2. **ALBUM**:

Define `add_album()` funtion the way that it takes `album_name`, `artist_name`, `genre`, number of tracks (`tracks`), dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as inputs, and adds the desired album to the dictionary of `all_albums`.

<details>
  <summary>See how to write it.</summary>

  ```python
def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
    pass
  ```
</details>

## Now there will be requests from AI for suggesting musics. You have to create functions that return values that are useful for each request:

### Function query_user_artist:
Complete the query_user_artist function in a way that takes `username`, `artist_name`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs a user has purchased from an artist.

The general structure of this function is as follows:

```python
def query_user_artist(username, artist_name, all_users, all_albums):
    pass
```

### Function query_user_genre:
Complete the query_user_genre function in a way that takes `username`, `genre`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs a user has purchased from a genre.

The general structure of this function is as follows:

```python
def query_user_genre(username, genre, all_users, all_albums):
    pass
```

### Function query_age_artist:
Complete the query_age_artist function in a way that takes `age`, `artist_name`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs purchased by users of a specific age from an artist.

The general structure of this function is as follows:

```python
def query_age_artist(age, artist_name, all_users, all_albums):
    pass
```

### Function query_age_genre:
Complete the query_age_genre function in a way that takes `age`, `genre`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs purchased by users of a specific age from a genre.

The general structure of this function is as follows:

```python
def query_age_genre(age, genre, all_users, all_albums):
    pass
```

### Function query_city_artist:
Complete the query_city_artist function in a way that takes `city`, `artist_name`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs purchased by users residing in a specific city from an artist.

The general structure of this function is as follows:

```python
def query_city_artist(city, artist_name, all_users, all_albums):
    pass
```

### Function query_city_genre:
Complete the query_city_genre function in a way that takes `city`, `genre`, dictionary of all users (`all_users`), and dictionary of all albums (`all_albums`) as input and returns the number of songs purchased by users residing in a specific city from a genre.

The general structure of this function is as follows:

```python
def query_city_genre(city, genre, all_users, all_albums):
    pass
```
