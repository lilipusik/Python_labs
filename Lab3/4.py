def get_level(child_parent, level, main_p, child):
    parent = child_parent[child]
    if parent == main_p: return level
    return get_level(child_parent, level+1, main_p, parent)

n = int(input("Введите количество человек: "))

child = set()
parent = set()
child_parent = dict()
for i in range(n-1):
    pair = input(f"{i+1} пара: ").split(' ')
    child_parent[pair[0]] = pair[1]
    child.add(pair[0])
    parent.add(pair[1])

main_parent = str(*(parent - child))
name_level = dict()
name_level[main_parent] = 0
for child, parent in child_parent.items():
    name_level[child] = get_level(child_parent, 1, main_parent, child)
    
name_level = dict(sorted(name_level.items()))
for name, level in name_level.items():
    print(name + ": " + str(level))