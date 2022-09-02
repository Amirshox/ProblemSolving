def barista(coffees):
    coffees.sort()
    waiting_times = []
    previous_waiting_time = 0
    for index, coffee in enumerate(coffees):
        if index == 0:
            waiting_times.append(coffee)
            previous_waiting_time = coffee
        else:
            waiting_time = coffee + 2 + previous_waiting_time
            waiting_times.append(waiting_time)
            previous_waiting_time = waiting_time
    return sum(waiting_times)


print(barista([4, 3, 2]))

"""
[4, 3, 2]

1) 4 = 4
2) 4 + 2 + 3 = 9
3) 4 + 2 + 3 + 2 + 2 = 13


[2, 3, 4]
1) 2 = 2
2) 2 + 2 + 3 = 7
3 ) 2 + 2 + 3 + 4 + 2 = 13

"""
