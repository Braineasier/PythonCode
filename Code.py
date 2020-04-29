class book:
    def __init__(self,tit=None,auth=None,pub=None,prc=None,royalty=None,copy=None):
        self.title=tit
        self.author=auth
        self.publisher=pub
        self.price=prc
        self.royalty=royalty
        self.copies=copy

    def get_title(self):
        return print("The title of the book is: {}".format(self.title))
    def get_author(self):
        return print("The author of he book is: {}".format(self.author))
    def get_publisher(self):
        return print("The publisher of the book is: {}".format(self.publisher))
    def get_price(self):
        return print("The price is: {}".format(self.price))

    def royalty_cal(self):
        if self.copies <= 500:
            self.royalty=0.1*self.price*self.copies
        if self.copies > 500 and self.copies <= 1500:
            self.royalty=0.1*self.price*500 + 0.125*self.price*(self.copies-500)
        if self.copies > 1500:
            self.royalty=0.1*self.price*500 + 0.125*self.price*1000 + 0.15*self.price*(self.copies-1500)
        return print("The royalty given is: {}".format(self.royalty))

    def set_title(self,a):
        self.title=a
    def set_author(self,a):
        self.author=a
    def set_publisher(self,a):
        self.publisher=a
    def set_price(self,a):
        self.price=a
    def set_copies(self,a):
        self.copies=a

b1=book()
b1.set_title("Harry Potter series")
b1.set_author("JK Rowling")
b1.set_publisher("Bloomsbury Publishing")
b1.set_price(3000)
b1.set_copies(5000)
b1.royalty_cal()
b1.get_title()
b1.get_author()
b1.get_publisher()
b1.get_price()



class eBook(book):
    def __init__(self,tit=None,auth=None,pub=None,prc=None,royalty=None,copy=None,format=None):
        super().__init__(tit=None,auth=None,pub=None,prc=None,royalty=None,copy=None)
        self.format=format

    def get_format(self):
        return self.get_format
    def set_format(self,a):
        self.format=a

    def royalty_cal(self):
        if self.copies <= 500:
            self.royalty = 0.1*self.copies*self.price
        if self.copies > 500 and self.copies <= 1500:
            self.royalty = 0.1*self.price*500 + 0.125*self.price*(self.copies-500)
        if self.copies > 1500:
            self.royalty = 0.1*self.price*500 + 0.125*self.price*1000 + 0.15*self.price*(self.copies-1500)

        #print("Total royalty is: {}".format(cost)
        #self.royalty = cost - 0.12*cost
        return print("The royalty on ebooks after 12% GST is: {}".format(0.88*self.royalty))


eb1=eBook()
eb1.set_title("Harry Potter series")
eb1.set_author("JK Rowling")
eb1.set_publisher("Pottermore")
eb1.set_price(3000)
eb1.set_copies(5000)
eb1.set_format("ePUB")
eb1.royalty_cal()
eb1.get_title()
eb1.get_author()
eb1.get_publisher()
eb1.get_price()
eb1.get_format()
