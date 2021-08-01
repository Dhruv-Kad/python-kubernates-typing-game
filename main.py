#List of questions that will be asked
question_grid = ["kubectl rollout", "kubectl get nodes", "kubectl apply", "kubectl expose",
                 "kubectl get", "kubectl patch", "kubectl delete", "kubectl apply" ]
question_grid_test = ["kubectl rollout", "kubectl get pods"]
#function that asks the questions
print("There are " + str(len(question_grid)) + " questions in this set")
def asker():
    c = 0
    for str in question_grid:
        ans = input(str + ":")
        if ans == str:
         #tallies correct ans
            c += 1

        else:
            print("incorrect")
#returns number of correct ans
    return c
#asks the number of attempts the user wants
print("How many attempts do you want to have? ")
attempts = int(input("Enter a number:"))
#sets a permanant value for attempts to be used later on
permanantattempts = attempts
#repeats until attemps are zero

while attempts > 0:
    result = asker()
    attempts -= 1

    # when attemps are zero it prints the percent correct
    if attempts == 0:
        print("over")

    else:
        # gets value of corrent answers minus
        per = str(result / len(question_grid) * 100)
        print("you got " + per + "% right on attempt number " + str(attempts))












