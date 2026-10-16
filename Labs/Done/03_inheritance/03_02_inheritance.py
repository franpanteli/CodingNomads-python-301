# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

# 1) & 2) Define the `Movie()` class with a dunder init method for `year` and `title`
class Movie:

  def __init__(self, year, title):
    self.year = year
    self.title = title

  def get_info(self):
    return f"{self.title} ({self.year})"


# 3) Create a sub-class called `RomCom()` that inherits from `Movie`
class RomCom(Movie):
  pass  # Inherits year, title, and get_info() as-is


# 4) Create another sub-class called `ActionMovie()` that overwrites __init__
#    and adds an instance variable `pg` defaulted to 13.
class ActionMovie(Movie):

  def __init__(self, year, title, pg=13):
    super().__init__(year, title)  # Calls the parent class's __init__
    self.pg = pg  # Adds the new instance variable with a default of 13


# --- Quick Test of the Classes ---
if __name__ == "__main__":
  base_movie = Movie(1994, "The Shawshank Redemption")
  romcom = RomCom(1993, "Sleepless in Seattle")
  action = ActionMovie(1991, "Terminator 2: Judgment Day", pg=13)

  print(base_movie.get_info())
  print(romcom.get_info())  # Inherited method works!
  print(f"{action.get_info()} - PG Rating: {action.pg}")