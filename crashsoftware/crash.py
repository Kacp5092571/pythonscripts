yes = 0
hej=1
hejstr=str(hej)
hi = "hithere" + hejstr + ".txt"
while yes==0:
    hejstr=str(hej)
    hi = "hithere" + hejstr + ".txt"
    hej = hej+1
    f = open(hi, "xt")
