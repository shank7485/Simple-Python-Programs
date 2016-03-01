def toLower(input):
    output = ""
    for i in input:
        if i != ' ':
            value = ord(i)
            if value >= 65 and value <= 90:
                output = output + chr(value + 32)
            else:
                output = output + chr(value)
    return output

def panagram_check(input):
    input = toLower(input)
    char_array = [0]*26
    flag = True

    for i in input:
        char_array[ord(i) - 97] = 1

    print char_array

    for i in char_array:
        if i == 0:
            flag = False
            break

    if flag == True:
        print "pangram"
    else:
        print "not pangram"

input = raw_input()
panagram_check(input)
