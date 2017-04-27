import sys
import argparse
import csv
def gettime(input):
    res = []
    zeros = [1,2,4,5,6,7,8,9]
    length = 11
    for i in range(len(input)):
        part = [input[i][j] for j in zeros]
        print (part)
        if (not all(x == '0' for x in part)):
            tmp = input[i]
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

def getMatrix(input):
    with open(input, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        labeledFeature = list(csvreader)
    return labeledFeature

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise argparse.ArgumentTypeError('the number of argument has to be 1')
        exit(-1)
    labeledFeature = getMatrix(sys.argv[1])
    res = gettime(labeledFeature)
    createosu(res)