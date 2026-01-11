
tweets = [
    "I love coding! #Python #coding #Life",
    "Just learned #coding and lists in #PYTHON",
    "#life is good but #coding is better",
    "Ignore this #viral #FYP post"
]
banned = {"#viral", "#fyp"}
def analyze_trends(tweets, banned_tags):

    hashtags = []
    for line in tweets:

        for word in line.split():
            if "#" in word:
                tags = word.lower()
            
                if tags not in banned_tags:
                    hashtags.append(tags)



    count = {}
    for tag in hashtags:
        if tag in count:
            count[tag] += 1
        else:
            count[tag] = 1
    sorted_tags = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_tags
result = analyze_trends(tweets, banned)
print(result)