surfaceN = int(raw_input())  # the number of points used to draw the surface of Mars.
for i in xrange(surfaceN):
    # landX: X coordinate of a surface point. (0 to 6999)
    # landY: Y coordinate of a surface point.
    # By linking all the points together in a sequential fashion,
    # you form the surface of Mars.
    landX, landY = [int(j) for j in raw_input().split()]

# game loop
while 1:
    # hSpeed: the horizontal speed (in m/s), can be negative.
    # vSpeed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    X, Y, hSpeed, vSpeed, fuel, rotate, power = [int(i) for i in raw_input().split()]

    # rotate is the desired rotation angle. power is the desired thrust power.
    if vSpeed <= -40:
        power = '4'
    else:
        power = '0'
    print "0 "+power  # rotate power.
