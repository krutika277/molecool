"""
measure.py
Python program for calculating atom properties

"""
import numpy as np

def calculate_distance(rA, rB):
    """
    This function calculates the distance between two points given as numpy arrays

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
         The distance between the two points.
    
    Example
    -------
    >>> r1 = np.array([1,0,0])
    >>> r2 = np.array([0,0,0])
    >>> calculate_distance(r1,r2)
    1.0

    """
     
    if not isinstance(rA, np.ndarray) or not isinstance(rB, np.ndarray):
        raise TypeError(" Input must be np.ndarray ")

    vector_distance = (rA - rB)
    distance = np.linalg.norm(vector_distance)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

