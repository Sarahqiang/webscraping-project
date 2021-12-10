import csv
import os,sys
import json
import random
from pathlib import Path

import pandas as pd
import numpy as np


def main():
    jsonfile =sys.argv[3]
    samplenum = sys.argv[4]
    outputfile = sys.argv[2]
    valuelist = []
    with open(jsonfile,'r')as f:
        l = f.readlines()
        sample = random.sample(l,int(samplenum))
        for i in sample:
            data = json.loads(i)
            name = data['data']['author_fullname']
            title = data['data']['title']
            value =[name,title,'']
            valuelist.append(value)
        headers =['Name','title','coding']
        with open(outputfile,'w')as j:
            parentdir = Path(__file__).resolve().parents[1]
            if (os.path.isdir(parentdir) == False):
                os.mkdir(parentdir)
            writer = csv.writer(j,delimiter='\t')
            writer.writerow(headers)
            writer.writerows(valuelist)
if __name__ == '__main__':
        main()

