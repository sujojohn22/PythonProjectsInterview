def large_sum(arr):
  if len(arr)==0:
    return 0
  max_sum=curr_sum=arr[0]

  for num in arr[1:]:
      curr_sum=max(curr_sum+num , num)
      max_sum=max(curr_sum,max_sum)
  return max_sum

print("largesum",large_sum([4,1,-4,5,-5,8,7,9]))