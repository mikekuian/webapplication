
RomanNumbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s= "LVIII"
number=0
for index in range(0, len(s)):
    if index < len(s) - 1 and RomanNumbers[s[index]] < RomanNumbers[s[index + 1]]:
        number = number + RomanNumbers[s[index + 1]] - RomanNumbers[s[index]]
        index = index + 12
        print(index)
    else:
        number = number + RomanNumbers[s[index]]
        index=index+1
        print(index)



