regular_work=40
overtime=12

for i in range(1,11):
    work_hours=int(input("How many hours employee worked"))

    if(work_hours>regular_work):
        overtime_hr=work_hours-regular_work
        pay=overtime_hr*overtime
        print("employee work for and his pay rate is ",overtime,"=","and ","pay =",pay)
    else:
        print("employee not work for overtime")
