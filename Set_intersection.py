setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
setu = setx.union(sety)
print(setu)
setr = setu.difference(setx)
print(setr)
setg = setu.symmetric_difference(setr)
print(setg)