def calculateMomentum(x1, y1, x2, y2):
    q = 1
    k = 1
    r_sq = (x1 - x2)**2 + (y1 - y2) ** 2 + 0.001
    m = k * (q ** 2) / r_sq
    if m > 10:
        m = 10
    vec_x = x1 - x2
    vec_y = y1 - y2
    mx = vec_x * m
    my = vec_y * m
    return mx, my
