num_tests = int(input())
birds = input().split()
for i,bird_dist in enumerate(birds):
    birds[i] = int(bird_dist)

# main process loop
def process_timestep(birds):
    prev_birds_left = 0
    while True:
        birds_left = 0
        for i, bird_distance in enumerate(birds):
            if bird_distance > 0    :
                birds_left += 1
                birds[i] -= 1

        # only print on change
        if birds_left != prev_birds_left and birds_left > 0:
            print(birds_left)
        prev_birds_left = birds_left

        # base base
        if birds_left == 0:
            return

process_timestep(birds)