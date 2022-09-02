import pathlib
import sys

path = pathlib.Path(sys.argv[1])

print('Exists.' if path.exists() else 'Cannot Find.')
