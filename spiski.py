from module import*
Capitals=dict()
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Germany"]="Berlin"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany"]
for country in Countries:
    country=input("Введите страну: ")
    if country in Capitals:
        print("Столица страны "+country+": " +Capitals[country])
    else:
        print("В базе данных не страны с названием " +country)
        v=input("Хотите внести " +country+ " в базу данных?: ")
        if v=="Да":
            ca=input("Введите столицу страны "+country)
            Capitals.update({country: ca})
        elif v=="Нет":
            print("Всего доброго!")
            break