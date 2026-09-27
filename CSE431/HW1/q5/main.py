ret = []

def calc_distance(cloud_leaves, leaf_wing_conv, frag_wing_conv):
    cloud_wings = cloud_leaves // leaf_wing_conv
    distance = 0
    cloud_frags = 0
    while cloud_wings > 0:
        cloud_wings -= 1
        distance += 1
        cloud_frags += 1
        if cloud_frags >= frag_wing_conv:
            cloud_wings += 1
            cloud_frags -= frag_wing_conv
    ret.append(distance)





# given template
num_tests = int(input())
for test_idx in range(num_tests):
    line = input().split()
    cloud_leaves = int(line[0])
    leaf_wing_conv = int(line[1])
    frag_wing_conv = int(line[2])
    calc_distance(cloud_leaves, leaf_wing_conv, frag_wing_conv)

for line in ret:
    print(line)