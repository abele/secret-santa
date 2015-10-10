# -*- coding: utf-8 -*-
import random

random.seed(1)


def getRandomPerson(ppl):
    return ppl[random.randint(0,len(ppl)-1)]


def good_pair(ignore_ppl, chosen1, chosen2):
    for pair in ignore_ppl:
        if chosen1 in pair and chosen2 in pair:
            return False
    return True


def main():
    ppl = ['x', 'y', 'z', 'a', 'b', 'c']
    ignore_ppl = [['x', 'y'],['x', 'c']]

    #Ja lasa failu no stdin
    #ppl = [line.strip() for line in open(str(sys.argv[1]))]
    #ignore_ppl = [line.split() for line in open(str(sys.argv[2]))]

    result = []

    while len(ppl) > 0:
        chosen = getRandomPerson(ppl)
        while result and not good_pair(ignore_ppl, chosen, result[len(result) - 1]):
            chosen = getRandomPerson(ppl)
        result.append(chosen)
        ppl.remove(chosen)

    for i in range(0, len(result)):
        if i is len(result) - 1:
            print(result[i] + " dāvina dāvanu " + result[0])
        else:
            print(result[i] + " dāvina dāvanu " + result[i+1])


if __name__ == '__main__':
    main()
