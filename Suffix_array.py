def make_buckets(a,x): #x番目の値で10こに分ける,aは一次元リスト
    buckets=[[], [],[],[],[],[],[],[],[],[],[]]
    for i in a:
        if i+x+1<=n:
            buckets[int(A[i+x])+1].append(i) 
        else:
            buckets[0].append(i) #x番目の次の値がないときは一番最初のリストにいれる
    return buckets

def get_index(buckets,index,count,x): #該当するリストの位置を探す
    for i in range(len(buckets)):
        if index-count<=len(buckets[i]):
            buckets=make_buckets(buckets[i],x)
            break
        else:
            count+=len(buckets[i])
    return buckets,count

def listcheck(buckets): #各リストの合計要素が１になったときにTrueを返す
    sum1=0
    for i in range(len(buckets)):
        if len(buckets[i])>1:
            return False
        elif len(buckets[i])==1 :
            sum1+=1
    if sum1==1:
        return True
    else:
        return False

def double_to_single_list(ls): #二次元配列を一次元配列に直す
    res = []
    for i in range(len(ls)):
        if ls[i] != []:
            for j in range(len(ls[i])):
                res.append(ls[i][j])
    return res
    
import time
start = time.time()
n=20000000
A =[] #Aにn桁までの値を読み込む
i=0
with open('pi200M.txt', 'r') as f:
    for line in f:
        if i==(n/20):
            break
        A.append(line.strip())
        i+=1
A=''.join(A) #Aを文字列としてつなぐ
    
buckets=[[],[],[],[],[],[],[],[],[],[],[]]
for i in range(len(A)):
    buckets[int(A[i])+1].append(i)

s_index=[(n//5)*i for i in range(1,5)] #求めるべきインデックス
s_array=[] #答えを格納するリスト

for i in range(4):
    bb=buckets
    #print(bb)
    count=0
    x=0
    while True: #listcheckがTrueになるまで回し続ける
        bb,count=get_index(bb, s_index[i], count, x)
        #print(bb)
        #print(count)
        x+=1
        if listcheck(bb):
            break 
    #print()
    for j in range(len(bb)):
        if len(bb[j])==1:
            s_array.append(bb[j])

            
s_array=double_to_single_list(s_array) #１次元リストに直して各要素に１を足す
for i in range(len(s_array)):
    s_array[i]+=1
    
print(s_array)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time))