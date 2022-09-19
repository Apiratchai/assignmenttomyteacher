class Book():
    def sumup(self):
        n = int(input("\nenter your quantity of books "))
        sum = (self).price*n
        if sum >400:
            total = sum*0.85
        else:
            total = sum
        print("total price is  ", total)

        def cashing():
            cash = int(input("Enter receieved cash "))
            if cash >= total:
                change = cash - total
                print("your change is ", change)
            else:
                print("cash is not enough")
                sum = 0
                cashing()
                    
        cashing()

## assign another books here 
BookA = Book()
BookA.price = 100

BookB = Book()
BookB.price = 50


##operation part
BookA.sumup()


            
        
            
