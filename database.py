"""A database encapsulating collections of near-Earth objects and their close
approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches
        self.neo_names_map = {}
        self.neo_designation_map = {}

        for neo in self._neos:
            if neo.designation not in self.neo_designation_map:
                self.neo_designation_map[neo.designation] = neo
            if neo.name not in self.neo_names_map:
                self.neo_names_map[neo.name] = neo

        for approach in self._approaches:
            if approach._designation in self.neo_designation_map:
                approach.neo = self.neo_designation_map[approach._designation]
                approach.neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.


        :param designation: The primary designation of
         the NEO to search for.
        :return: The `NearEarthObject` with the desired
         primary designation, or `None`.
        """
        if designation in self.neo_designation_map:
            return self.neo_designation_map[designation]
        return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        if name in self.neo_names_map:
            return self.neo_names_map[name]
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a
        collection of filters.

        This generates a stream of `CloseApproach` objects that
         match all of the
        provided filters.

        If no arguments are provided, generate all known close
         approaches.

        The `CloseApproach` objects are generated in internal
         order, which isn't
        guaranteed to be sorted meaningfully, although is often
        sorted by time.

        :param filters: A collection of filters capturing
        user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            # flags is a list of boolean values
            flags = map(lambda f: f(approach), filters)
            if all(flag is True for flag in flags):
                yield approach
