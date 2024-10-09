def trailingZeros(n):
    if n < 0:
        return -1
    count = 0
    i = 5
    while n/i > 0:
        count += n //i
        i *= 5
    return count


def trailingZeros2(n):
    if n < 0:
        return -1
    count = 0
    while n>= 5:
        n //= 5
        count += n
    return count

print(trailingZeros(100))
print(trailingZeros2(100))