def per(fst, lst):
    if len(lst) == 0:
        print fst
    else:
        for ele in lst:
            per(fst+[ele], [_lst for _lst in lst if _lst not in [ele]])

def permute(inplist):
    per([], inplist)

permute([1,2,3,4])
