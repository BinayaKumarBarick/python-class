import Geometry.area as A
import Geometry.volume as V 


print("area of circle=",A.circle(5))
print("area of rectangle=",A.rectangle(3,4))

print("volume of cube=",V.cube(4))
print("volume of cuboid=",V.cuboid(2,3,5))

     #OR

from Geometry.area import rectangle,circle
from Geometry.volume import cube,cuboid
result1=rectangle(3,4),circle(5)
result2=cube(4),cuboid(2,3,5)
print(result1 )
print (result2)
