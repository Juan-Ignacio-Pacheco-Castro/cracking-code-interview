to_be_url = "Mr John Smith"

def URLfy(to_be_url):
    result = ""
    for i in to_be_url:
        if i == " ":
            result += "%20"
        else:
            result += i
    return result

print(URLfy(to_be_url))