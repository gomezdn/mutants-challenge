# Mutants App

This repository provides a python application that tells whether a given DNA belongs to a human or a mutant.

It exposes two HTTP endpoints:
- GET /stats

    StatsObject: `{
      "count_mutant_dna": integer,
      "count_human_dna": integer,
      "ratio": float
    }`

    > Returns `StatsObject HTTP/200`

<br>
<br>

- POST /mutant

    > Accepts a JSON of the form of {
      "dna": DnaMatrix
    }

    DnaStr: A string containing only the following characters: A | T | C | G

    DnaMatrix: ["DnaStr1", "DnaStr2", "DnaStr3", "DnaStr4"...], an array of DnaStr of the same length, where this length must be a divisor of the array's length.

    > Returns `true HTTP/200` for a mutant or `false HTTP/403` for a human.

<br>
<br>

# Start the project locally

## Setting up the database
A Supabase db (PostgreSQL) is needed to store the analysed DNAs.

See `.env.example` and create an `.env` file at the root of this project with Supabase credentials.

### Inside the Supabase console:

Create the table by running ` CREATE TABLE dna(dna_hash TEXT PRIMARY KEY, dna JSONB UNIQUE, is_mutant BOOL);`

Create an index for `is_mutant` field by running `CREATE INDEX ON dna(is_mutant);`


## Running the API
Run these commands in the following order at the root of this repository

`python -m venv .venv`

`.venv/Scripts/activate`

`pip install -r requirements.txt`

`flask run -h localhost -p 3008`

Now you can send requests to the API running on http://localhost:3008
