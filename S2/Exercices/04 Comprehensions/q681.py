words = ['apple', 'banana', 'cherry', 'dog', 'ct']


vowel_counts_v2 = {word: sum(1 for char in word if char.lower() in 'aeiou') for word in words}
vowel_counts_v3 = {word: sum(1 if char.lower() in 'aeiou' else 0 for char in word ) for word in words}
vowel_counts = {word: sum(1 for char in word if char.lower() in 'aeiou') for word in words if
                any(char.lower() in 'aeiou' for char in word)}
print(words)

print(vowel_counts_v2)
print(vowel_counts_v3)
print(vowel_counts)