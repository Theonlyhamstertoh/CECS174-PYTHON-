class Artist:
  # TODO: Define constructor with parameters to initialize instance attributes
  #       (name, birth_year, death_year)

  def __init__(self, name,  birth_year, death_year):
    self.name = name
    self.birth_year = birth_year
    self.death_year = death_year
  # TODO: Define print_info() method
  def print_info(self):
    death_year = "present" if self.death_year == -1 else self.death_year

    if self.birth_year == -1 and self.death_year == -1:
      print(f"Artist: {self.name} (unknown)")
    else:
      print(f"Artist: {self.name} ({self.birth_year} to {death_year}")
      

    
  

      
class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

  def __init__(self, title, year_created, artist):
    self.title = title
    self.year_created = year_created
    self.artist = artist

  def print_info(self):
    self.artist.print_info()
    print(f"Title: {self.title}, {self.year_created}")

    # TODO: Define print_info() method


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()
