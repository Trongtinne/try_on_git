import re
def extract_hashtag(text):
    hashtag=re.findall(r'#\w+' , text)
    return hashtag
text="Please share for us and using hashtag #fptschools #SxM when you share"
print(extract_hashtag(text))
