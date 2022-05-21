
# Practice some concepts specially handling os.path [ Common pathname manipulations ]

import os.path
import csv


csv_path = "/Users/norberto.moreno/Desktop/csv_project/movie_metadata.csv"
this_dir, tail = os.path.split(csv_path)
#this_dir, tail = os.path.split(__file__)
full_path = os.path.join(this_dir, tail)

def _listing_gen():
    """
    Internal path generator method.
    :return: Path generator object
    """
    print(f"The header path is: {this_dir}")
    with os.scandir(this_dir) as entries:
        for entry in entries:
            if os.path.isfile(os.path.join(this_dir, entry)) and entry.name.endswith(".py"):
                    yield os.path.join(this_dir, entry)

def listing_paths(listing_func):
    """
    Lists paths.
    """
    for list_gen in listing_func:
        print(list_gen)


def csv_reader():
    with open(full_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'The column names are: {",".join(row)}')
                line_count += 1



def main():
    """ Main function."""
    csv_reader()





# Entry Point
if __name__=="__main__":
    main()