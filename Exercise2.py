import statistics
list1: list[float] = []
tall_players: float = 0
above_avg_players: int = 0
sum_players: int = 0
SENTINEL: int = -999
while True:
     height: float = float(input('enter height of player'))
     if height == SENTINEL:
         break
     if height < 1.60 or height > 3.0:
         continue
     sum_players += 1
     list1.append(height)
avg_height: float = sum_players/ len(list1)
for i in list1:
    if i > 2.0:
        tall_players += 1
for j in list1:
    if j > avg_height:
         above_avg_players += 1
print(list1)
print(f"average height of players is: ", statistics.mean(list1))
print(f"sum players is: {sum_players}")
print(f"the tallest player is: ", max(list1))
print(f"the lowest player is: ", min(list1))
print(f"number of players that height big than 2 meter is: {tall_players}")
print(f"The number of players whose height is above average: {above_avg_players}")