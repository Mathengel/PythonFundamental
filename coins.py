


def coins():

    heads = 0
    tails = 0
    import random
    for x in range(1,5001):
        random_num = random.random()
        flip = round(random_num)
        if flip == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... it's a head! ...Got {} heads so far!".format(x, heads)
        else:
            tails +=1
            print "Attempt #{}: Throwing a coin... it's a tails! ...Got {} heads so far!".format(x, tails)
        



coins()
        