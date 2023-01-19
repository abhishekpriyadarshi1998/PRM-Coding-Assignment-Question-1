def sort_list(lst):
  list.sort(key=lambda x: x[-2]) 
  return lst
list = ['great','hello','hiyo','abc']
result = sort_list(list)
print(result)