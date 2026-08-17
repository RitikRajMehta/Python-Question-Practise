# 19. Tuple Intersection
t1 = (1, 2, 3, 4, 5, 6)
t2 = (4, 5, 6, 7, 8, 9)
common = tuple(x for x in t1 if x in t2)
print("Common elements:", common)
