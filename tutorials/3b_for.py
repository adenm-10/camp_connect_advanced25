sentence = ["these", "are", "words", "in", "a", "sentence"]

for word in sentence:
    print(word, end=" ")

print()

total = 0
for num in range(3):
    total = total + num
    print(f"num = {num}, total = {total}")