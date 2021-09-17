# -*- coding: utf-8 -*-
"""Package to provide force fields from standard examples"""

from .parse_dreiding import parse_dreiding
from .parse_uff import parse_uff
from .parse_atomic_masses import parse_atomic_masses

DREIDING = parse_dreiding()
UFF = parse_uff()
atomic_mass = parse_atomic_masses()
