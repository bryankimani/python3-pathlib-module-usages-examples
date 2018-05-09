import pathlib

# pathlib.Path.cwd() gets the relative path the
# working directory then / joins cwd path to test.md path
# The / can join several paths or a mix of paths and strings
# an alternative to using / is .joinpath() method
# below can be written as path = pathlib.Path.cwd().joinpath("assets/test.md")
path = pathlib.Path.cwd() / "assets/test.md"
# read the content of the test.md-file in binary/bytes mode and return the contents as a bytestring.
content = path.read_bytes()
# print the content of test.md-file
print(content)