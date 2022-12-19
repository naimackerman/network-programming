def sha1(*args, **kwargs):
    
    # get the value of the input field that contains the data to be hashed
    data = Element('plainText').element.value

    # initialize the value of an hexadecimal used for hashing
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # convert data to binary string 
    bits = data_to_bits(data)
    # Pad the message until its length is a multiple of 512
    pBits = pad_message(bits)

    # Split the data into chunks of the specified size
    for c in split_into_chunks(pBits, 512): 
        words = split_into_chunks(c, 32)
        # initializes a list of 80 zeros, which will be used to store the processed message blocks.
        w = [0]*80
        for n in range(0, 16):
            # Convert the 32-bit words into integers
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
                # b AND c OR NOT b AND d
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                # b XOR c XOR d
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                # b AND c OR b AND d OR c AND d
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                # b XOR c XOR d
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

    # format value of h0, h1, h2, h3, h4 to hexadecimal string
    hash_result = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    # print the result of hashing in the text field
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
    # append the original length
    pBits+='{0:064b}'.format(len(bits)-1)

    return pBits

def split_into_chunks(data, chunk_size):
    # Split the data into chunks of the specified size
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def rol(n, b):
    # Bitwise operation that shifts the bits in the binary representation of a number to the left by a specified number of places (b).
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


# print (sha1("hello world"))