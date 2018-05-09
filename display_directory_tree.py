import pathlib

# pathlib.Path.cwd() gets the relative path the
# working directory
path = pathlib.Path.cwd()


def tree(directory):
    # print a visual tree representing the file hierarchy, rooted at
    # a given directory. Here, we want to list subdirectories as
    # well, so we use the .rglob() method
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        # The f-strings only work in Python 3.6 and later. In older Pythons,
        # the expression f'{spacer}+ {path.name}'
        # can be written '{0}+ {1}'.format(spacer, path.name)
        print(f'{spacer}+ {path.name}')


tree(path)