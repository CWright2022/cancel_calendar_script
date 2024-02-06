'''
in case you accidentally import a google calendar,
you can use this to make a new copy of the ICS file
with all the events listed as "cancelled".
re-import the file and all the events will go away.

Cayden Wright 11/30/2022
'''

import re

RE_PATTERN = "PRIORITY"


def cancel_calendar(filename):
    contents = ""
    # read file
    with open(filename) as file:
        for line in file:
            contents += line
            if re.match(RE_PATTERN, line):
                contents += "STATUS:CANCELLED\n"
    # write file
    with open(filename, "w") as file:
        file.write(contents)


def main():
    cancel_calendar("C:\\path\\to\\calender\\file.ics")


if __name__ == "__main__":
    main()
