clamp = lambda n, min_n, max_n: max(min(max_n, n), min_n)

def rgb(r, g, b):
    r = clamp(r, 0, 255)
    g = clamp(g, 0, 255)
    b = clamp(b, 0, 255)

    return '#%02x%02x%02x' % (r, g, b)

def rgb_tight(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

if __name__ == "__main__":
    answer = rgb(233, 220, 467)
    print("Answer", answer)
