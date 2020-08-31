#!/root/mypy/bin/python

def set_name_age(name,age):
    if not 0<int(age)<120:
        raise ValueError('Invalid Age')
    print(name,type(age),age)

def set_name_age2(name,age):
    assert  0<int(age)<120, "age out of range"
    print(name,type(age),age)


if __name__=='__main__':
    set_name_age2('bob','130')