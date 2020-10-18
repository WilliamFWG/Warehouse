class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return '<<%s>>,author:%s' % (self.title,self.author)

if __name__ == '__main__':
    pybook= book('Python基础教程','Magnus Lie Hetland')
    print(pybook)