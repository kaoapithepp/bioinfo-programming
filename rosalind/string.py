# seq = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
seq = 'axsIAgy1GorABart7PyQShLV4h74RZEQE9XrHWbijToqdve9j3czUXnp3a4gqKmvmK9ej0F7itihJNUSnzN6W02jUqaq39UnciahWspHnwXqda1Ey0vmRrEaG2PQGcMnNWp1KD76Kw8AajIzZi3bRVKvaC79A8yixbkBDm0RJ0FSuibpHRby2zXHNSxGyn8kuGfNv0.'
cs1 = 94
ce1 = 98
cs2 = 101
ce2 = 102

def chopandslice(seq, s1, e1, s2, e2):
    str1 = seq[s1:e1+1]
    str2 = seq[s2:e2+1]
    return str1, str2

print(chopandslice(seq, cs1, ce1, cs2, ce2))