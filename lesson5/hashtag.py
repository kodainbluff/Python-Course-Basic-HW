#This program will turn imported string into a hashtag
import string

ht_base = str(input("Please enter a phrase you want to turn into a hashtag: "))
ht_npunct = ht_base.translate(str.maketrans("", "", string.punctuation))
ht_title = ht_npunct.title()
ht_stripped = ht_title.replace(" ", "")
print(f"#{ht_stripped[:140]}")