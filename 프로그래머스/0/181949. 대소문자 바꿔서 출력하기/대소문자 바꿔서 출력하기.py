str = input()
fixed_str = []
for i in str:
    if i.islower():
        fixed_str.append(i.upper())
    else:
        fixed_str.append(i.lower())
print(''.join(fixed_str))