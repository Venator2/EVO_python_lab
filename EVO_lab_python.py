def direction(facing, turn):
    way = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if facing not in way:
        return "Side does not exist"
    initial = way.index(facing)
    if turn >= 0:
        turn %= 360
    else:
        turn %= -360
    step = turn / 45
    n = initial + step
    if n > len(way) - 1:
        n -= len(way)
    elif n < 0:
        n += len(way)
    return way[int(n)]