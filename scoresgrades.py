

def scoresgrades():
    print "Scores and Grades"
    for i in range(0,10):
        score = input("What is your test score?")

        
        if 100 >= score >=90:
            print "Score: {}; Your grade is A".format(score)
        elif 89 >= score >=80:
            print "Score: {}; Your grade is B".format(score)
        elif 79 >= score >=70:
            print "Score: {}; Your grade is C".format(score)
        else:
            print "Score: {}; Your grade is D".format(score)

            



scoresgrades()