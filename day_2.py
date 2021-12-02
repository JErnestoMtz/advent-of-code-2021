with open("input.txt", "r") as f:
    ins = [line.strip() for line in f]
    (a,x,y) = (0,0,0)
    for line in ins:
        word = line[0]
        quant = int(line[-1])
        if word == "f":
            x += quant
            y += a * quant
        elif word == "d":
            a += quant
        elif word == "u":
            a -= quant
    print(x*y)

