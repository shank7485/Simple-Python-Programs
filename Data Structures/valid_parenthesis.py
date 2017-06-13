# Prints valid parenthesis. 
# http://algorithms.tutorialhorizon.com/generate-all-valid-parenthesis-strings-of-length-2n-of-given-n/

def v(o, c, str):
  if o == 0 and c == 0:
    print(str)
  if o > c:
    return
  if o > 0:
    x =  str + "("
    v(o-1, c, x)
  if c > 0:
    y = str + ")"
    v(o, c-1, y)

v(2, 2, "")
