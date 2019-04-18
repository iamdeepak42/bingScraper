from os import listdir
from os.path import isfile, join
mypath=r"./"
import re
import pandas as pd
import random

hero = []
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for files in onlyfiles:
    print(files)
    f=open(files)
    data = f.read()
    f.close()
    emails = re.findall('[\w\.-]+@[\w\.-]+', data)
    for  i in emails:
        i=i.lstrip('.')
        hero.append(i)
    
    # print(len(hero))

hero  =list(set(hero))
print(len(hero))
random.shuffle(hero)

with open(str(len(hero))+'.csv','a') as f:
    for email in hero:
        f.write(email+'\n')


print('Unique emails found:',len(hero))