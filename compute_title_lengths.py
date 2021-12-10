import os,sys
import json


def main():
    inputfile = sys.argv[1]

    with open(inputfile,encoding="utf-8",errors="ignore")as j:
        l = j.readlines()
        #data =l['data']['title']
        length =0
        line =0
        for jsonboj in l:
            newjson = json.loads(jsonboj)
            title = newjson['data']['title']
            length += len(title)
            line+=1

    avalen = length/line
    print(avalen)







if __name__ =='__main__' :
    main()