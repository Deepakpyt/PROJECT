string = 'AABCAAADA'
k = 3
sub_st = [string [k * i : k * (i + 1)] for i in range(int(len(string) / k))]

print(sub_st)

for ele in sub_st:
    merg = ''
    for i in range(len(ele)):
        if i == ele.index(ele[i]):
            merg += ele[i]
            
    print(merg)
        