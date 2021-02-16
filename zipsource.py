from zipfile import Zipfile
from sys import argv


with Zipfile("source.zip", "w") as zipobj:
	for pyfile in argv[1:]:
		zipobj.write(pyfile)


