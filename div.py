def competitiveEating(t, width, precision):
    return '{:^{}.{}f}'.format(t, width, precision)

print(competitiveEating(223.33,10,3))
