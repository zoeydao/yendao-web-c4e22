import mlab
from river import River

mlab.connect()

print("Ex2")
river_list = River.objects()
for p in river_list:
    if p.continent == "Africa":
        print(p.name)
        print(p.continent)
        print(p.length)
        print("*****")

print("Ex3")
river_list2 = River.objects(length__lt=1000)
for p in river_list2:
    if p.continent == "S. America":
        print(p.name)
        print(p.continent)
        print(p.length)