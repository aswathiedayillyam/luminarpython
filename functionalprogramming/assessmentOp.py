





#highest score team?

from funtools import reduce
point_high=list(filter(lambda team:team["points"]=reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],isl_2019))))),isl_2019))
print(point_high)