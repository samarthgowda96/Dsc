import classStacks

string="My name is Sammy"
reverseString=""
s= classStacks.Stack()
for i in string:
    s.push_items(i)

while not s.is_empty():
    reverseString= reverseString+ s.pop_items()

print(reverseString)
