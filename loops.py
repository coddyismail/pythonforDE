#iteration for all elments
the_list = ["North", "Iceburg", "Yawn", "Arrow", "Machine", "Anchor", "Takeway"]
#this code will let you know first letter of each elemnts
for i in the_list:
    print(i[0])

#if else in loops
table = ["Order", "Product", "Reviews"] 
for i in table:
    if(i.lower() == "order"):
        print("table order")
    else:
        print("no table order")