# A Caesar Cipher is a simple cipher that works by shifting each letter in
# the given message by a certain number. For example, if we shift the message
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given
# message by shift letters. You are guaranteed that message is a string, and
# that shift is an integer between -25 and 25. Capital letters should stay capital
# and lowercase letters should stay lowercase, and non-letter characters should not be changed.
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
    str_lower = "abcdefghijklmnopqrstuvwxyz"
    str_upper = str_lower.upper()
    data = []
    print(str_upper)
    for i in msg:
        if i == " ":
            continue
        if i in str_lower:
            data.append(str_lower[(str_lower.index(i)+shift) % 26])
        elif i in str_upper:
            data.append(str_upper[(str_upper.index(i)+shift) % 26])
    new_msg = ""
    new_msg.join(data)
    print(new_msg)


fun_applycaesarcipher("We Attack At Dawn", 1)
