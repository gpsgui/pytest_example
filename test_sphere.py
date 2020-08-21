import geom_elements
import math
# testing  : pytest --log-format="%(asctime)s %(levelname)s %(message)s" --log-date-format="%Y-%m-%d %H:%M:%S" >> test.log
def test_volume_calculation():
    r = 3
    s = geom_elements.Sphere([0,0,0],r)
    assert s.get_volume() == (4/3) * math.pi * (r**3)

def test_is_inside_method():
    r = 2
    p1 = geom_elements.Point([1,1,1])
    p2 = geom_elements.Point([3,3,3])
    s = geom_elements.Sphere([0,0,0],r)
    assert s.is_inside(p1) == True
    assert s.is_inside(p2) == False