question_grid = ["kubectl rollout", "kubectl get nodes", "kubectl apply", "kubectl expose",
                 "kubectl get", "kubectl patch", "kubectl delete", "kubectl apply" ]

def asker():
    for str in question_grid:
        ans = input(str + ":")
        if ans == str:
            print("correct")
        else:
            print("wrong")

print("How many attempts do you want to have? ")
attempts = int(input("Enter a number:"))
while attempts > 0:
    asker()
    attempts -= 1
    if attempts == 0:
        print("nice try")
    else:
        print("new attempt")











