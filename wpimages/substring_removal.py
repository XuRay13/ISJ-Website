


#ABABBA --> BA --> AA


def substring_removal(seq):
  i = 0
  length = len(seq)
  min = 0
  while i < length:
    c = seq[length - i - 1]
    print(c)
    if c == 'A':
      min += 1
    elif c == 'B':
      break

    i += 1

  remaining = length - min
  if remaining % 2 == 0:
    return min

  return min + 1 # not even so they'll be 1 leftover


x = substring_removal("ABABBA")
print(x)