array_of_arrays = [['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]
new_arr = sorted([len(arr) if arr else 0 for arr in array_of_arrays])
print(new_arr)
n_arr = list(range(1,max(new_arr)+1))
print(n_arr)
print([num for num in n_arr if num not in new_arr][0])
arr =[1, 6, 9, -3, 4, -78, 0]
print(''.join(map(str,arr)))
print(str(-3)+str(4))
lst = [1,2,3,4]
print(repr(lst))