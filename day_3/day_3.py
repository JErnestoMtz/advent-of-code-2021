def  which_has_more(li):
    if li.count('1') < li.count('0'):
        return '1'
    else:
        return '0'

def trnaspose(li):
    return [[code[k] for code in li] for k in range(12)]

def countn(li):
    return list(map(which_has_more, li))
def p2(l,i):
    if len(l) == 1:
        return l
    else:
        nl = []
        t = trnaspose(l)
        c = countn(t)
        for code in l:
            if code[i] == c[i]:
                nl.append(code)
        i += 1
        p2(nl,i) 

with open("input.txt") as f:
    codes = [line.strip() for line in f]
    #r = p2(codes,0)
    #print(r)
    a = int('001110100101',2)
    b = int('111000100110',2)
    print(a*b)
    #transpose = [[code[i] for code in codes] for i in range(12)]
    #gama = list(map(which_has_more, transpose))
    #epslion = list(map(lambda x : str(int(x) ^ 1) , gama))
    #g = int(''.join(gama,2)
    #e = int(''.join(epsilon,2)
    #print(e*g)
