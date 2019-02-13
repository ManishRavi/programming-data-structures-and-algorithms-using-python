Question:

Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, 
every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other 
symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
  >>> matched("zb%78")
  True
  >>> matched("(7)(a")
  False
  >>> matched("a)*(?")
  False
  >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
  True
  
  Program/Solution
  
  def matched(s):
    ope = []
    clo = []
    for i in s:
        if i == "(":
            ope = ope + ["("]
        else:
            if i == ")":
                clo = clo  + [")"]
    if len(ope)==len(clo):
        return True
    else:
        return False 
