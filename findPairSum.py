def pair_sum(ls,k):
    seen = set()
    output = set()
    if k==0 or len(ls)<2:
        return 0
    else:

        for num in ls:
            if num<k:
             target=k-num
             if target in ls:
                  output.add((min(num,target),max(num,target)))
    return output


print(pair_sum( [1,3,3,2,2],4))
