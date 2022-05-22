from fastapi import FastAPI
import csv
import os.path

app = FastAPI()

this_dir, tail = os.path.split(__file__)
csv_path = os.path.join(this_dir, "movie_metadata.csv")


@app.get("/")
def home_view():
    """The API endpoints docs."""
    return {"This is the Movie data API!."}

@app.get("/column_names")
def fetch_columns():
    """Fetch the data column names."""
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = dict()
        line_counter = 0
        for row in csv_reader:
            if line_counter == 0:
                data["column_names"] = ", ".join(row)
                line_counter += 1
    return data
