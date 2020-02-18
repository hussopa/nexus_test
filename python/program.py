import random
import string
import argparse
import shutil
import os


def createRandomText(len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def createFilename():
    return createRandomText(8)


def createTextRow():
    return createRandomText(64)


def main(arguments):
    if arguments.flushdata:
        shutil.rmtree("data")
        os.makedirs("data")

    for _ in range(arguments.filecount):
        with open("data/{0}.txt".format(createFilename()), "a") as f:
            f.write(createTextRow())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='This script is used to connect PostgreSQL and push some data to the database.',
                formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--filecount",
                        type=int,
                        required=False,
                        default=1,
                        help='Specify amount of files to create')

    parser.add_argument("--flushdata",
                        type=bool,
                        required=False,
                        default=True,
                        help='Specify if "data" is flushed')

    arguments = parser.parse_args()
    print(arguments)
    main(arguments)
