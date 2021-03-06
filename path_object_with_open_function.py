import pathlib

# pathlib.Path.cwd() gets the relative path the
# working directory then / joins cwd path to test.md path
# The / can join several paths or a mix of paths and strings
# an alternative to using / is .joinpath() method
# below can be written as path = pathlib.Path.cwd().joinpath("assets/test.md")
path = pathlib.Path.cwd() / "assets/test.md"
# finds all headers in a Markdown file and print them
# read file using open() function on the Path object:
# Path.open() is calling the built-in open() behind the scenes
with path.open(mode='r')as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
print('\n'.join(headers))