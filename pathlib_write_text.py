import pathlib

# pathlib.Path.cwd() gets the relative path the
# working directory then / joins cwd path to test.md path
# The / can join several paths or a mix of paths and strings
# an alternative to using / is .joinpath() method
# below can be written as path = pathlib.Path.cwd().joinpath("assets/test.md")
path = pathlib.Path.cwd() / "assets/test.md"
# write text to test.md-file in text mode and return the contents as a string.

with open(path, "a") as fid:
        path.write_text("Paths can also be specified as simple file names, "
                        "in which case they are interpreted relative to the "
                        "current working directory. The following example is "
                        "equivalent to the previous one:", encoding="UTF8")
print(path.read_text())