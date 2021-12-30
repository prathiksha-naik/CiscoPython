#duck typing in oops
class python3:
    def excute(self):
        print("compile")
        print("run")
class Myeditor:
    def excute(self):
        print("Spell check")
        print("Convention check")
        print("compile")
        print("run")
    
class laptop:
    def code(self,ide):
        ide.excute()
ide=Myeditor()
a=laptop()
a.code(ide)
