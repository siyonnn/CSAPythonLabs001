# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")



# Application 1

str = "ghost"
result = ''
for char in str:
    result += char * 2
print(result)




# Application 2

str_range = "h-w"
start, end = str_range.split('-')
start_code = ord(start)
end_code = ord(end)
result = ''.join(chr(item) for item in range(start_code, end_code + 1))
print(result)  

