class Farhad:
    def faru(self,rest,due):
        if(res[0]<due[0]):
            return 0
        elif(res[0]>due[0]):
            return 10000
        elif(res[1]<due[1]):
            return 0
        elif(res[1]>due[1]):
            return 500*(res[1]-due[1])
        elif(res[2]<due[2]):
            return 0
        elif(res[2]>due[2]):
            return 15*(res[2]-due[2])
        else:
            return 0
        #pass
#print(res,due)
farhad=Farhad()
res = list(reversed([int(i) for i in input().split()]))
due = list(reversed([int(i) for i in input().split()]))
#print(res,due)
print(farhad.faru(res,due))