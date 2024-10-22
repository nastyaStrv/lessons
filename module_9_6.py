def all_variants(text):
    n = len(text)
    for r in range(1, n + 1):
        for j in range(n - r + 1):
            yield text[j:j + r]

a = all_variants("abc")
for i in a:
    print(i)

