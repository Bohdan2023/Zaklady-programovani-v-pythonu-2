def bits_count(number):
    if number < 0:
        number = -number
    if number == 0:
        return 1
    
    bit_count = 0
    while number > 0:
        bit_count = bit_count + 1
        number >>= 1
    return bit_count

# print(bits_count(16))


def convert(letter):
    bit = 1 << 5
    
    if 'a' <= letter <= 'z':
        return chr(ord(letter) & ~bit)
        
    elif 'A' <= letter <= 'Z':
        return chr(ord(letter) | bit)
    
    else:
        return letter

# print(convert('a'))
# print(convert('Z'))
# print(convert('5'))


def rotate_right(number, count):
    bit_length = number.bit_length()
    
    rotated_number = ((number >> count) |
                      (number << (bit_length - count) &
                       ((1 << bit_length) - 1)))
    
    return rotated_number

# print(bin(rotate_right(0b100100111, 2)))
