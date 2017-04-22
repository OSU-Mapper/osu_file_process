import sys
import argparse

def gettime(input):
    res = []
    zeros = [1,2,4,5,6,7,8,9]
    for i in range(len(input)):
        part = [input[i][j] for j in zeros]
        if (not all(i == 0 for i in part)):
            tmp = list(map(str, input[i]))
            addition = tmp[6]+":"+tmp[7]+":"+tmp[8]+":"+tmp[9]
            tmp = tmp[1:6]
            tmp.append(addition)
            res.append(tmp)
    return res

def createosu(input):
    with open("example1.osu", 'w') as osu_file:
        osu_file.write("osu file format v5\n\n[General]\n...\n\n[Metadata]\n...\n\n[Difficulty]\n...\n\n[TimingPoints]\n...\n\n[HitObjects]\n")
        for i in range(len(input)):
            osu_file.write(input[i][0]+","+input[i][1]+","+input[i][2]+","+input[i][3]+","+input[i][4]+","+input[i][5]+"\n")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        # print( "usage: inputfile outputfile")
        raise argparse.ArgumentTypeError('the number of argument has to be 1')
        exit(-1)
    test = [[1, 0, 0, 20001, 0, 0, 0, 0, 0, 0], [2, 0, 0, 25678, 0, 0, 0, 0, 0, 0], [3, 0, 0, 27876, 0, 0, 0, 0, 0, 0], [4, 64, 280, 30168, 1, 0, 0, 0, 0, 0], [5, 192, 280, 31650, 1, 0, 0, 0, 0, 0], [6, 0, 0, 32331, 0, 0, 0, 0, 0, 0], [7, 328, 280, 33165, 1, 0, 0, 0, 0, 0], [8, 456, 280, 34662, 1, 0, 0, 0, 0, 0], [9, 0, 0, 56789, 0, 0, 0, 0, 0, 0], [10, 0, 0, 76345, 0, 0, 0, 0, 0, 0], [11, 72, 192, 84046, 6, 0, 0, 0, 0, 0], [12, 440, 272, 87039, 2, 0, 0, 0, 0, 0], [13, 136, 352, 90032, 2, 0, 0, 0, 0, 0], [14, 0, 0, 10765, 0, 0, 0, 0, 0, 0], [15, 256, 192, 113976, 12, 0, 0, 0, 0, 0], [16, 0, 0, 120009, 0, 0, 0, 0, 0, 0]]
    res = gettime(test)
    createosu(res)