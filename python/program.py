import random
import string
import argparse


def createRandomText(len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def createFilename():
    return createRandomText(8)


def createTextRow():
    return createRandomText(64)


def main(arguments):
    for _ in range(arguments[0])
    with open("{0}.txt".format(createFilename()), "a") as f:
        f.write(createTextRow())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='This script is used to connect PostgreSQL and push some data to the database.',
                formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--filecount",
                        type=int,
                        required=True,
                        default=1,
                        help='Specify amount of files to create')

    arguments = parser.parse_args()
    main(arguments)
