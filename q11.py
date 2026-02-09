#Write aprogramthattakesasinput.Usingconditionalstatements,calculatethebasedontheserules:Q1salaryfinaltaxrate•Ifsalary<30,000→5%•Ifsalaryis30,000–70,000→15%•Ifsalary>70,000→25% 
Your_salary=(float(input("Enter Your Salary:-")))
    
if Your_salary <=30000:
    print("Tax amount will be:-",Your_salary*5/100)
elif (Your_salary>=30000 and Your_salary<70000):
    print("Tax amount will be:-",Your_salary*15/100)
else:
    (Your_salary>=70000)
    print("Tax amount will be:-",Your_salary*25/100)