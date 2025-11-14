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
    digit_location = 0
    for char in formula[1:]:
        digit_location += 1
        if char.isdigit():
            break
    else:
        digit_location = len(formula)

    if digit_location == len(formula):
        return (formula, 1)
    else:
        prefix = formula[:digit_location]
        numeric_part_str = formula[digit_location:]
        return (prefix, int(numeric_part_str))

formula = "He98"
print(split_at_first_digit(formula))
