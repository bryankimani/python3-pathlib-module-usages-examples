import pathlib
import collections

# pathlib.Path.cwd() gets the relative path the
# working directory then / joins cwd path to assets folder
# The / can join several paths or a mix of paths and strings
# an alternative to using / is .joinpath() method
# below can be written as path = pathlib.Path.cwd().joinpath("assets")
path = pathlib.Path.cwd() / "assets"
# The following example combines .iterdir() with the collections.Counter
# class to count how many files there are of each filetype in the
# current directory assets folder
counter = collections.Counter(p.suffix for p in path.iterdir())
print(counter)