def sha1(*args, **kwargs):
    
    data = Element('plainText').element.value

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    bits = data_to_bits(data)
    pBits = pad_message(bits)

    for c in split_into_chunks(pBits, 512): 
        words = split_into_chunks(c, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #Main loop
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    hash_result = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    Element('hashResult').element.innerHTML = hash_result
    # return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def data_to_bits(data):
    # Convert the data to a binary string
    bytes = ''
    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    return bits

def pad_message(bits):
    # Pad the message until its length is a multiple of 512
    pBits = bits
    while len(pBits)%512 != 448:
        pBits+="0"
    #append the original length
    pBits+='{0:064b}'.format(len(bits)-1)

    return pBits

def split_into_chunks(data, chunk_size):
    # Split the data into chunks of the specified size
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def rol(n, b):
    # The rol() function (short for "rotate left") is a bitwise operation that shifts the bits in the binary representation of a number to the left by a specified number of places (b). The bits that are shifted out of the most significant position are wrapped around and inserted into the least significant position.
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# print (sha1("hello world"))