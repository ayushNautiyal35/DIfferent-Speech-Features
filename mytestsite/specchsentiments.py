import sys
from textblob import TextBlob
test_sentence1 = sys.argv[1]
output=TextBlob(test_sentence1)
if(output.sentiment.polarity<0):
    print("negative")
elif(round(output.sentiment.polarity)>0):
    print("positive")
else:
    print("neutral")
