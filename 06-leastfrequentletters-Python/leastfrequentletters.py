# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!")
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally,
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
    # Your code goes here
    length = len(s)
    s = s.lower()
    least = ""
    for i in range(length):
        if not s[i].isalpha():
            continue
        repeat = False
        for j in range(length):
            if s[i] == s[j] and i != j:
                repeat = True
                break
        flag = False
        if not repeat:
            for k in range(len(least)):
                if s[i] < least[k]:
                    least = least[:k]+s[i]+least[k:]
                    flag = True
                    break
            if not flag:
                least += s[i]
    print(least)
    return least


leastfrequentletters("aDq efQ? FB'daf!!!")
