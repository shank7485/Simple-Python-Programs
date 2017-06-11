def subset_print(main_set, set, N):
  if N == 0:
    return
  for i in main_set:
    new_set = set + i
    print(new_set)
    subset_print(main_set, new_set, N-1)
    
main_set = "abcd"
set = ""
N = len(main_set)

subset_print(main_set, set, N)
