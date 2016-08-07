lightX, lightY, initialTX, initialTY = [int(i) for i in raw_input().split()]
thorX, thorY = (initialTX, initialTY)
# game loop
while 1:
    directionX = ''
    directionY = ''
    if thorX > lightX:
        directionX = 'W'
        thorX -= 1
    elif thorX < lightX:
        directionX = 'E'
        thorX += 1

    if thorY > lightY:
        directionY = 'N'
        thorY -= 1
    elif thorY < lightY:
        directionY = 'S'
        thorY += 1

    print directionY+directionX
