


def slots(quarters, m1, m2, m3):
    playCount = 0
    mSelect = 1

    while quarters > 0:
        
        quarters = quarters - 1
        playCount += 1

        if mSelect == 1: 
            if m1%35 == 0:
                quarters += 30
                mSelect = 2
                m1 += 1
            elif m1%35 > 0:
                mSelect = 2
                m1 += 1

        elif mSelect == 2:
            if m2%100 == 0:
                quarters += 60
                mSelect = 3
                m2 += 1
            elif m2%100 > 0:
                mSelect = 3
                m2 += 1

        elif mSelect == 3: 
            if m3%10 == 0:
                quarters += 9
                mSelect = 1
                m3 += 1
            elif m3%10 > 0:
                mSelect = 1
                m3 += 1

    print(f"Martha plays {playCount} times before going broke")

# should be 152
slots(77, 4, 9, 3)
