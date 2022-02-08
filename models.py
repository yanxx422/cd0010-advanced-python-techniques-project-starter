"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
import helpers


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about
    the object, such as its primary designation (required, unique),
    IAU name (optional), diameter in kilometers (optional - sometimes
     unknown), and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close
    approaches - initialized to an empty collection, but eventually
    populated in the `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied
        to the constructor.
        """
        self.designation = str(info['designation']) \
            if 'designation' in info else ''
        self.name = str(info['name']) \
            if 'name' in info and info['name'] != "" else None
        self.diameter = float(info['diameter']) \
            if 'diameter' in info and info['diameter'] != "" else float('nan')
        self.hazardous = True \
            if 'hazardous' in info and info['hazardous'] == 'Y' else False
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        if self.name:
            return f"{self.designation} {self.name}"
        else:
            return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""

        if self.hazardous:
            return f"NEO {self.designation} {self.name} has a diameter" \
                   f"of {self.diameter:.3f} km and is potentially hazardous."
        else:
            return f"NEO {self.designation} {self.name} has a diameter" \
                   f"of {self.diameter:.3f} km and " \
                   f"is not potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string
        representation of this object."""

        return f"NearEarthObject(designation={self.designation!r}, " \
               f"name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, " \
               f"hazardous={self.hazardous!r})"

    def serialize(self):
        """ Return a dictionary that contains the parameters of the neo."""

        return {'designation': self.designation,
                'name': self.name,
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close
    approach to Earth, such as the date and time (in UTC) of closest
    approach, the nominal approach distance in astronomical units,
    and the relative approach velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its
    `NearEarthObject` - initially, this information (the NEO's primary
     designation) is saved in a private attribute, but the referenced
    NEO is eventually replaced in the `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied
         to the constructor.
        """

        self._designation = str(info['_designation']) \
            if '_designation' in info else ''
        self.distance = round(float(info['distance']), 2) \
            if 'distance' in info else 0.0
        self.velocity = round(float(info['velocity']), 2) \
            if 'velocity' in info else 0.0
        self.time = helpers.cd_to_datetime(info['time']) \
            if 'time' in info else None

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.
        """
        # build a formatted representation of the approach time.
        return helpers.datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility.
        # Peek at the __repr__
        # method for examples of advanced string formatting.

        if self.neo:

            return f"A Close Approach occured at " \
                   f"{self.time_str}, " \
                   f"{self.neo.designation} {self.neo.name} " \
                   f"approaches Earth at a distance of " \
                   f"{self.distance:.2f} au " \
                   f"and a velocity of {self.velocity:.2f}km/s."
        else:
            return f"A Close Approach occured at " \
                   f"{self.time_str}, " \
                   f"{self.neo.designation} {self.neo.name}  " \
                   f"approaches Earth at a distance of" \
                   f" {self.distance:.2f} au " \
                   f"and a velocity of {self.velocity:.2f}km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string
        representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, " \
               f"distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, " \
               f"neo={self.neo!r})"

    def serialize(self):
        """ Return a dictionary that contains the parameters of
        the approach."""
        return {'datetime_utc': self.time_str,
                'distance_au': self.distance,
                'velocity_km_s': self.velocity}
