class TypeManager:
    def __init__(self):
        self.pointer=0
        self.blocks=200
        self.memory=[] #[dir,name,size,align,[trash]]
        self.trash=[]   # [ini,fin]

    def insert(self,name,size,align):
        index,elem=self.search_var(name)
        if index<0:
            if not self.pointer==0:
                if align<self.pointer:
                    pointer=self.pointer
                else:
                    if self.pointer+size>self.blocks*400:
                        return 1
                    else:
                        base=align
                        if base>self.pointer and base+size<self.blocks*4:
                            trash=[self.pointer,base]
                            self.trash.append(trash)
                            pointer=base
                            if size%4 !=0:
                                trash=[self.pointer,base]

    def search_var(self,name):
        index=-1
        elem=None
        for i in range(len(self.memory)):
            my_name=self.memory[i][1]
            if my_name==name:
                index=i
                elem=self.memory[i]
        return index,elem