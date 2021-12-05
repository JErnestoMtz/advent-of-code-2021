def parse_ins(ins):
    x = ins.split(' -> ')
    p1 = int(x[0].split(',')[0]) + int(x[0].split(',')[1])*1j 
    p2 = int(x[1].split(',')[0]) + int(x[1].split(',')[1])*1j
    return (p1,p2)

def get_points(cords):
    p1, p2 = cords
    if p1.real == p2.real:
        nfrom, nto = int(min(p1.imag,p2.imag)), int(max(p1.imag,p2.imag))
        return [p1.real + im*1j for im in range(nfrom,nto+1)]
    elif p1.imag == p2.imag:
        nfrom, nto = int(min(p1.real,p2.real)), int(max(p1.real,p2.real))
        return [r + p1.imag*1j for r in range(nfrom,nto+1)]
    else:
        # --------- Part 1 -------

        #return []

        # ------- Part 2 ---------
        abs1, abs2 = abs(p1), abs(p2)
        lenline = int(abs(p1-p2))
        if abs1 < abs2:
            return [(p1.real +i) + (p1.imag+i)*1j for i in range(lenline+1)]
        else:
            return [(p2.real +i) + (p2.imag+i)*1j for i in range(lenline+1)]

    

with open("sample.txt", "r") as f:
    ins = [parse_ins(line.strip()) for line in f]
    thermals = dict()
    for ther in ins:
        for point in get_points(ther):
            if point in thermals:
                thermals[point] += 1
            else:
                thermals[point] = 1
    result = 0 
    for x in thermals.values():
        if x > 1:
            result += 1
    print(result)



    

