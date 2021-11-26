H = 10
W = 10
N = 1

info_list = []

while N <= 100:

    room = 0
    room_level = []

    i = 1

    while i <= N:
        room_level.append(i)
        i = i+H

    if N == 1:
        room = 1
    else: 
        room = len(room_level)

    floor = N % H

    if floor == 0:
        floor = H

    if floor < 10:
        floor = "0" + str(floor)

    if room < 10: 
        room = "0" + str(room)
   
    info_list.append(str(floor)+str(room))

    N += 1

for x in info_list:
    print(x)
