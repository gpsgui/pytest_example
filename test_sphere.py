import geom_elements
import math

def testVolume_calculation():
    r = 3
    s = geom_elements.Sphere([0,0,0],r)
    assert s.get_volume() == (4/3) * math.pi * (r**3)