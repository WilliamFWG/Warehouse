class Role:
    def __init__(self,nm,wp):
        self.name=nm
        self.weapon=wp
    def speak(self,word):
        print(word)

class Warrior(Role):
    #def __init__(self):
    def attack(self,target):
        print('攻击 %s' % target)
    pass
class Mage(Role):
    #def __init__(self):
    pass

class Weapon:
    def __init__(self,nm,type):
        self.wname=nm
        self.wtype=type

if __name__ == '__main__':
    ji1=Weapon('方天画戟','物理攻击')
    lb = Warrior('吕布',ji1)
    sz = Weapon('折扇','法术攻击')
    dc = Mage('貂蝉',sz)
    print(lb.name,lb.weapon.wname,lb.weapon.wtype)
    print(dc.name,dc.weapon.wname,dc.weapon.wtype)
    lb.speak("我是吕布")
    lb.attack('')