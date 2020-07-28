def reverse(s):
    answer=""

    for i in range(0, len(s)):
        answer+=s[len(s)-i-1]
    return answer

print(reverse("Hello world!"))