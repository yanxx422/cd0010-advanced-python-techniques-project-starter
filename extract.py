"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

import models


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    obj_lst = []
    with open(neo_csv_path) as infile:
        reader = csv.reader(infile)
        # skip the header
        next(reader, None)
        for line in reader:
            obj_lst.append(
                models.NearEarthObject(designation=line[3], name=line[4], diameter=line[15], hazardous=line[7]))

    return obj_lst


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    approach_lst = []
    with open(cad_json_path) as infile:
        contents = json.load(infile)
        data = contents['data']
        for entry in data:

            approach_lst.append(models.CloseApproach(_designation=entry[0], time=entry[3],
                                                     distance=entry[4], velocity=entry[7]))

    return approach_lst
