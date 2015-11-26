print("Welcome to the GPA calculator.")

courses=int(input("Enter number of courses:"))
GpaList=[]
CreditList=[]
Markcount=0
Creditcount=0
print('Enter marks in percentage and then credit for that course in the next line')

for a in range(courses):
    Markcount+=1
    Creditcount+=1
    mark=int(input('mark'+ str(Markcount)+':'))
    credit=float(input('credit'+ str(Creditcount)+':'))

    if mark>=85 and mark<=100:
        gpa=float(4.0)

    elif mark>=80 and mark<=84:
        gpa=float(3.7)

    elif mark>=77 and mark<=79:
        gpa=float(3.3)

    elif mark>=73 and mark<=76:
        gpa=float(3.0)

    elif mark>=70 and mark<=72:
        gpa=float(2.7)

    elif mark>=67 and mark<=69:
        gpa=float(2.3)

    elif mark>=63 and mark<=66:
        gpa=float(2.0)

    elif mark>=60 and mark<=62:
        gpa=float(1.7)

    elif mark>=57 and mark<=59:
        gpa=float(1.3)

    elif mark>=53 and mark<=56:
        gpa=float(1.0)

    elif mark>=50 and mark<=52:
        gpa=float(0.7)

    else:
        gpa=float(0.0)

    weightGpa= float(gpa*credit)
    (GpaList.append(weightGpa))
    (CreditList.append(credit))

    totalSum=float(sum(GpaList))
    totalCredit=float(sum(CreditList))
    FinalGpa=totalSum/totalCredit
    print(FinalGpa)






























