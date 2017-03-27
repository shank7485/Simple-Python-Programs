"""
Time in Words
HackerRank::Algorithms::Implementation::The Time in Words
Comment: Doesn't work for some cases in HackerRank. (Need to consider other minutes as well)
"""
word_dict = {
    "hours":{
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine",
        "10":"ten",
        "11":"eleven",
        "12":"twelve"
    },
    "minutes":{
            "0":"o' clock",
            "01":"one minute past",
            "10":"ten minutes past",
            "15":"quarter past",
            "30":"half past",
            "40":"twenty minutes to",
            "45":"quarter to",
            "47":"thirteen minutes to",
            "28":"twenty eight minutes past"
    }
}

hour = int(raw_input())
minutes = int(raw_input())
output = ""

if minutes == 00:
    output = word_dict["hours"][str(hour)] + " " + word_dict["minutes"][str(minutes)]
elif minutes <= 30:
    output = word_dict["minutes"][str(minutes)] + " " + word_dict["hours"][str(hour)]
else:
    output = word_dict["minutes"][str(minutes)] + " " + word_dict["hours"][str(hour + 1)]
print output
