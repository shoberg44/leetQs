import heapq
room_heap = []
num_rooms, amount_to_explore = input().split()
num_rooms = int(num_rooms)
amount_to_explore = int(amount_to_explore)

for room_index in range(num_rooms):
    room_animals = int(input())
    heapq.heappush(room_heap, -1*room_animals)

for _ in range(amount_to_explore):
    print(-1*heapq.heappop(room_heap))
