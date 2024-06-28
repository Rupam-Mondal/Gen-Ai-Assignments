def reverse(s):
    p = ""
    for i in range(len(s) - 1 , -1 , -1):
        p = p + s[i]
    return p


print(reverse("Rupam"))