def consult_score():
    file = open("score_file.txt", "r")
    return int(file.read())


def update_score(score):
    if score > consult_score():
        file = open("score_file.txt", "w")
        file.write(str(score))
        file.close()
