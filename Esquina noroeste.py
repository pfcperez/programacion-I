# https://medium.com/@geekrodion/transportation-problem-north-west-corner-method-6965aa137689
# https://gist.github.com/dzhuang/34c03d50a10dadb4b332ff51c67d990e


def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
    return bfs


supply = [240, 260, 500]
demand = [300, 260, 440, 1000]
bfs = north_west_corner(supply, demand)
print(bfs)