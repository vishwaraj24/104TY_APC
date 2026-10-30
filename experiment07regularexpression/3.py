import re

def extract_hashtags(text):
    pattern = r'#[A-Za-z0-9_]+'
    hashtags = re.findall(pattern, text)
    return hashtags


text = input("Enter social media post: ")

result = extract_hashtags(text)

print("Hashtags:", result)