def split_before_each_uppercases(formula):
   if not formula:
       return []
   start = 0
   split_formula = []
   for end in range(1, len(formula)):
       if formula[end].isupper():
           split_formula.append(formula[start:end])
           start = end

   split_formula.append(formula[start:len(formula)])

   return split_formula

def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
