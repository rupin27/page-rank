import sys, os
import random

input_file = sys.argv[1]
f = open(os.path.join(sys.path[0], input_file), 'r', encoding='utf-8')
inlnk_out = open(os.path.join(sys.path[0].replace('/src', ''), 'inlinks.txt'), 'w', encoding='utf-8')
pgRk_out = open(os.path.join(sys.path[0].replace('/src', ''), 'pageRank.txt'), 'w', encoding='utf-8')
content = f.read().split()

source = []
target = []
lambd = 0.20
tau = 0.005
for i in range(len(content)):
    if (i%2==0):
        source.append(content[i])
    else:
        target.append(content[i])


def map(lst):
    linkFreq = {}
    for link in lst:
        if(link in linkFreq):
            linkFreq[link] += 1
        else:
            linkFreq[link] = 1
    return linkFreq

def map2(lst,dest):
    linkFreq = {}
    for i in range(len(lst)):
        if(lst[i] in linkFreq):
            linkFreq[lst[i]].append(dest[i])
        else:
            linkFreq[lst[i]] = []
            linkFreq[lst[i]].append(dest[i])
    return linkFreq

def map3(lst,lst2):
    linkFreq = {}
    for link in lst:
        if(link in linkFreq):
            linkFreq[link] += 1
        else:
            linkFreq[link] = 1
    for link in lst2:
        if(link in linkFreq):
            linkFreq[link] += 1
        else:
            linkFreq[link] = 1
    return linkFreq

def inlinkFreq(lst, numLinks):
    dict = map(lst)
    sort_by_val = {}
    sortedKeys = sorted(dict, key=dict.get) 
    for links in sortedKeys:
        sort_by_val[links] = dict[links]
    count = list(sort_by_val.values())
    link = list(sort_by_val.keys())
    count = [e for e in reversed(count)]
    link = [e for e in reversed(link)]
    for i in range(numLinks):
        inlnk_out.write(link[i])
        inlnk_out.write(' ' + str(i+1) + ' ' + str(count[i]) + '\n')

def pgRankVal(dict, numLinks):
    sort_by_val = {}
    sortedKeys = sorted(dict, key=dict.get) 
    for links in sortedKeys:
        sort_by_val[links] = dict[links]
    count = list(sort_by_val.values())
    link = list(sort_by_val.keys())
    count = [e for e in reversed(count)]
    link = [e for e in reversed(link)]
    for i in range(numLinks):
        pgRk_out.write(link[i])
        pgRk_out.write(' ' + str(i+1) + ' ' + str(count[i]) + '\n')

def pgRankLst(page, link, lam, tau):
    curPR = map3(page, link)
    resultPR = map3(page, link)
    mapped = map2(page, link)
    for k in curPR:
        curPR[k] = random.uniform(0, 1)
    converged = 0
    while (converged==0):
        sum = 0 
        convergeCheck = 0
        for k in resultPR:
            resultPR[k] = lam/(len(curPR))
        for k in resultPR:
            if k in mapped:
                outLinks = mapped[k]
                for i in range(len(outLinks)):
                    resultPR[outLinks[i]] += (1 - lam)*curPR[k]/len(outLinks)
            else:
                sum += (1 - lam)*curPR[k]/len(curPR)
        for k in resultPR:
            resultPR[k] += sum
        for k in resultPR:
            convergeCheck += abs(resultPR[k]-curPR[k])
        if convergeCheck < tau:
            converged = 1
        for k in resultPR:
            curPR[k] = resultPR[k]
    return resultPR


inlinkFreq(target, 100)
pageRank = pgRankLst(source, target, lambd, tau)
pgRankVal(pageRank, 100)
f.close()
inlnk_out.close()
pgRk_out.close()
