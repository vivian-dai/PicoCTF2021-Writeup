string = "ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿ½�}"
out = ""
temp = ""
index = 0
for char in string:
    temp += char
    index += 1
    if index%4 == 0:
        fwd = ""
        for temp_char in temp:
            fwd = temp_char + fwd
        out += fwd
        temp = ""
print(out)