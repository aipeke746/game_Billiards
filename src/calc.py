

def judge_shot(mx, my, bx, by, br):
    if ((mx-bx)**2 + (my-by)**2) <= br**2:
        return True
    return False
