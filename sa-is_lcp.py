import time
from sys import *
INF = 10**10
if len(argv) == 2:
    f = open("X.txt", "r", encoding="utf-8")
    string = f.read().replace(" ","").replace("\n","")
    sl = int(argv[1])
    string = string[:sl]
    #print("input end")
else:
    string = ""
    f = input()
    while (f):
        try:
            st = f.replace(" ","").replace("\n","")
            string += st
            f = input()
        except EOFError:
            #print("input end")
            break
# Sentinal / 番兵
string = string + "$"

#It takes O(nlogn) for the sort method and O(n) for string comparison. eventually O(n^2logn).
#Lets make it O(n) using suffix array and induced sort. (sa-is)

#sort()メソッドを使うとO(nlogn)で、文字列比較にO(n)なのでO(n^2logn)となってしまう。
#なのでこれからなるべくO(n)オーダーでsuffix array をソートする。(SA-IS法)
def max_l_n(l):
    m = -INF
    for i in l:
        if i>m:
            m = i
    return m


def is_lms(t,i):
    return i>0 and t[i-1] == "L" and t[i] == "S"

#induced_sort() will be used recursively.
#induced_sort部分は再起で使うので関数として定義しておく

def induced_sort(string, k, t, lms_index):
    if string == str(string):
        s_str = [None]*256
        for s in string:
            s_str[ord(s)] = s
        s_str = [s for s in s_str if s != None]
    else:
        s_str = [None]*k
        for s in string:
            s_str[s] = s
        s_str = [s for s in s_str if s != None]
    index_dic = {st:s for s,st in enumerate(s_str) }
    n = len(string)
    sa = [None]*n
    bins = [0]*k

    for s in string:
        bins[index_dic[s]] += 1
    for i in range(k-1):
        bins[i+1] += bins[i]
    lms_index = [i for i in range(n) if is_lms(t,i)]
    #step 1　# insert the LMS index into suffix array.
    #LMSのインデックスをsa(suffix arrat)に詰めていく
    count = [0]*k
    for lms in lms_index:
        ch = string[lms]
        index = index_dic[ch]
        sa[bins[index]-1-count[index]] = lms
        count[index] += 1
    #step2　#scan the sa in forward direction and insert the L type suffix
    #saを正順に走査してL型のsuffixを埋めていく
    count = [0]*k
    for s in sa:
        if s == None or s == 0 or t[s-1] == "S":
            continue
        ch = string[s-1]
        index = index_dic[ch]
        sa[bins[index-1]+count[index]] = s-1
        count[index] += 1
    #step3 #scan the sa in backward direction and insert the S type suffix
    #saを逆順に走査してS型のsuffixを埋めていく
    count = [0]*k
    for s in reversed(sa):
        if s == None or s == 0 or t[s-1] == "L":
            continue
        ch = string[s-1]
        index = index_dic[ch]
        sa[bins[index]-1-count[index]] = s-1
        count[index] +=1
    return sa


def sa_is(string,k):
    n = len(string)
    if string == str(string):
        s_str = [None]*256
        for s in string:
            s_str[ord(s)] = s
        s_str = [s for s in s_str if s != None]
    else:
        s_str = [None]*k
        for s in string:
            s_str[s] = s
        s_str = [s for s in s_str if s != None]
    index_dic = {st:s for s,st in enumerate(s_str) }
    if (n<2):
        return string
    # L or S type, L:s[i..]>s[i+1..] (Larger), S:s[i..]<s[i+1..] (Smaller)
    t = [None]*n
    t[-1] = "S"
    for i in range(n-2,-1,-1):
        if string[i] < string[i+1]:
            t[i] = "S"
        elif string[i] > string[i+1]:
            t[i] = "L"
        else:
            t[i] = t[i+1]
    #LMS:Left-Most-S, is_lms(t,i) judges wether t[i] is lms or not
    lms_index = [i for i in range(n) if is_lms(t,i)]
    # use the initial, temporary seed on purpose
    # 間違った種をわざと入れる
    seed = lms_index[:]
    sa = induced_sort(string, k, t, seed)
    sa = [s for s in sa if is_lms(t,s)]
    nums = [None]*n
    nums[sa[0]] = 0
    num = 0
    for s in range(len(sa)-1):
        i = sa[s]
        j = sa[s+1]
        dif = None
        for d in range(n):
            if i+d>=n or j+d>=n:
                break
            if string[i+d] != string[j+d] or is_lms(t,i+d) != is_lms(t,j+d):
                dif = True
                break
            elif d>0 and (is_lms(t,i+d) or is_lms(t,j+d)):
                break
        if dif:
            num+=1
        nums[j] = num
    nums = [s for s in nums if s != None]

    # use the list "nums" as an arguement of recursive call of sa_is()
    #ここで得られたnumsで再起を行う。
    if num +1 < len(nums):
        # the size of argument nums is less than half of the size of the original
        # so it becomes linear search (n+n/2+n/4+...=O(n))
        #ここで再帰をしても大きさが半分以下なので線形探索となる
        sa = sa_is(nums, num+1)
    else:
        # if there is no overlap in nums sa is obtained easily
        #nums内に重複がない場合saが求まる
        for i,ch in enumerate(nums):
            sa[index_dic[ch]] = i
    #correct seed is obtained
    #正しい種
    seed = [lms_index[i] for i in sa]
    k = len(s_str)
    sa = induced_sort(string,k,t,seed)
    return sa

def lcp(string, sa):
    # remove the sentinel
    # 番兵をなくす
    del sa[0]
    n = len(sa)
    #Longest Common Prefix
    r = [None]*n
    for i in range(n):
        r[sa[i]] = i
    l = 0
    LCP = [None]*n
    string = string[:-1]
    # this for loop contains important algorithm to maintain the order O(n)
    #　下のfor文の内容に注意。O(n)を保つためのアルゴリズムである。
    for i in range(n):
        k = r[i]
        j = sa[k-1]
        #print(i,j)
        while (l+j<n and l+i<n and string[j+l] == string[i+l]):
            l+=1
        LCP[k] = l
        if l>0:
            l-=1

    return LCP

start = time.time()
sorted_str = sorted(list(set(string)))
k = len(sorted_str)
sa = sa_is(string,k)

LCP = lcp(string, sa)

LCP[0] = -1000
m = max_l_n(LCP)
ind = LCP.index(m)
a,b = sa[ind],sa[ind-1]
a,b = min(a,b)+1,max(a,b)+1
n = len(string)
print("time {}".format(time.time() - start))
print(a,b,m)
