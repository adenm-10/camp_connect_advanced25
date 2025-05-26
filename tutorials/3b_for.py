sentence = ["these", "are", "words", "in", "a", "sentence"]
number_sequence = [1, 2, 3, 4 ,5]

for word in sentence:
    print(word, end=" ")

print()

for number in number_sequence:
    print(number, end=", ")

print()

total = 0
for num in range(3):
    total = total + num
    print(f"num = {num}, total = {total}")