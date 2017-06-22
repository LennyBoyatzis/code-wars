def sqInRect(lng, wdth):
    # [ expression for item in list if conditional else conditional ]
    squares = []
    max_val = max(lng, wdth)
    min_val = min(lng, wdth)
    difference = max_val - min_val
    squares.push(min_val)

    while min_val > 1:
        squares.push(min(lng, wdth))

    return None
