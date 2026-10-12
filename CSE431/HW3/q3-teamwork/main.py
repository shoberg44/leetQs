n_str, x_str = input().split()
n = int(n_str)
robot_id = int(x_str)
colors = input().split()

# map of color index to str, handles duplicates
color_to_id = {color: i for i, color in enumerate(colors)}
other_robot_colors = input().split()
# Sum the integer values of all colors Robot X can see
others_sum = sum(color_to_id[c] for c in other_robot_colors)

# calculate the missing value of summed colors
my_color_id = (robot_id - others_sum) % n

print(colors[my_color_id])