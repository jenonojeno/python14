student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for i in student:
    if i["score"] >= 80:
        print (i["name"],i["score"],"grade4")
    elif i["score"] >= 70:
        print (i["name"],i["score"],"grade3")
    elif i["score"] >= 60:
        print (i["name"],i["score"],"grade2")
    elif i["score"] >= 50:
        print (i["name"],i["score"],"grade1")
    else:
        print (i["name"],i["score"],"grade0")
#พัชนิดา 40