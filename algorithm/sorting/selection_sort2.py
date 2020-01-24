l = [10,9,4,7,2,4]
# l = [1,2,3,4,5]
e = [2,4,4,7,9,10]

spot_marker = 0
while spot_marker < len(l):
    print(f"running for spot marker {spot_marker} :{l}")
    for i in range(spot_marker, len(l)):
        if l[spot_marker] > l[i]:
            l[spot_marker],l[i] = l[i] , l[spot_marker]

    spot_marker += 1

print("Is sorted properly", e == l, l)