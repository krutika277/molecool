"""
Unit test for measure module

"""
import numpy as np 
import molecool
import pytest

def test_calculate_distance():
    """
    Tests the calculate_distance function
    """
    r1 = np.array([1,2,0])
    r2 = np.array([1,0,0])

    expected_distance = 2

    calculated_distance = molecool.calculate_distance(r1, r2)
    
    assert calculated_distance == expected_distance
def test_calculate_distance_typeerror():

    r1 = [1,0,0]
    r2 = [0,0,0]

    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)

def test_calculate_angle():
    """
    Test the calculate_angle function
    """

    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert calculated_angle == expected_angle

#@pytest.mark.parametrize("variable_name1,variable_name2, .......variable_nameN, expected_answer", [
#    (variable_value1, ... variable_valueN, expected_answer1),
#    (..)
#       ])
# def test_name(variable_name1,variable_name2, .......variable_namen, expected_answer)

@pytest.mark.parametrize("p1,p2,p3,expected_angle",[
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0,0,0]), np.array([1,0,0]), 45)
    
])
def test_calculate_angle_many(p1,p2,p3,expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert expected_angle == pytest.approx(calculated_angle)

#def test_molecular_mass(test_molecule):
#    symbols = ['C', 'H', 'H', 'H', 'H']
#    
#    calculated_mass = molecool.calculate_molecular_mass(symbols)
#
#    actual_mass = molecool.atom_data.atomic_weights['C'] + molecool.atom_data.atomic_weights['H'] +\
#         molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H']
#    
#    assert actual_mass == calculated_mass

#def test_center_of_mass():
#    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
#    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

#    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

#    expected_center = np.array([1,1,1])

#    assert center_of_mass.all() == expected_center.all()