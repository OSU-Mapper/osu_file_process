import sys
import argparse

def search(input):
    hitobject = []
    with open(sys.argv[1], 'r') as my_file:
        lines = my_file.readlines()
        line_iter = iter(lines)
        find = False
        target = "[" + input + "]"
        for line in line_iter:
            if target in line:
                find = True
                break
        if (find):
            for line in line_iter:
                if len(line.strip()) != 0:
                    tmp = line.split(",")
                    if len(tmp) == 5:
                        tmp = list(map(int, tmp))
                        for i in range(4):
                            tmp.append(0)
                    else:
                        lastele = tmp[len(tmp)-1]
                        tmp = tmp[0:5]
                        tmp = list(map(int, tmp))
                        addition = lastele.split(":")
                        if len(addition) == 4:
                            for i in range(4):
                                tmp.append(int(addition[i]))
                        else:
                            for i in range(4):
                                tmp.append(0)
                    hitobject.append(tmp)
                else: 
                    break	
            return hitobject	
        else:
            print("No such infomation in file")

def getbeat(input):
    beats = []
    with open(input, 'r') as my_file:
        lines = my_file.readlines()
        line_iter = iter(lines)
        for line in line_iter:
            line = line.split(",")
            line = list(map(int, line))
            beats.append(line)
    return beats

def closestindex(x, y):
    for i in range(len(y)):
        if y[i][1] == x:
            return i
        elif y[i][1] > x:
            if abs(y[i][1] - x) <= abs(y[i-1][1] - x):
                return i
            else:
                return i - 1

def merge(x, y):
    for i in range(len(x)):
        index = closestindex(x[i][2], y)
        x[i][2] = y[index][1]
        y[index] = [y[index][0]] + x[i]
    for i in range(len(y)):
        if len(y[i]) == 2:
            y[i] = [y[i][0],0,0,y[i][1],0,0,0,0,0,0]
    return y
if __name__ == "__main__":
    if len(sys.argv) != 3:
        # print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 3')
        exit(-1)
    hitobject = search("HitObjects")
    print (hitobject)
    beats = getbeat(sys.argv[2])
    print(beats)
    result = merge(hitobject, beats)
    print(result)