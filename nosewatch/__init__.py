"""
A nose plugin that re-runs test suite on filesystem event.
"""


VERSION = (0, 9, 2)

__version__ = '.'.join((str(each) for each in VERSION[:4]))

def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))

