def main():
    passwording_function=Shifrator()
    reading_function=De_shifrator()
    passwording_function.loading_aplication()
    reading_function.loading_aplication()
    print('DSH and SH installed successfull !!!')
    typing=True
    
    while typing:
        if passwording_function.key_passwording()=='stop':
            typing=False
            return 'You are dirty   !!!!!!!!!!!!!'
            
        else:
            reading_function.line_skiline()
            reading_function.clear()
            passwording_function.clear()
            


class De_shifrator:
    def __init__(self):
        self.abc=[  ['P','O','K','J','I'],
                    ['M','L','N','Q','Z'],
                    ['E','R','T','Y','U'],
                    ['A','S','D','F','G'],
                    ['B','V','C','H','X'] ] 
        
       
        self.code=None
        self.text=''
        
    def loading_aplication(self):
        loading=1
        load='#########'
        while(loading<100):
            [print('___________________________________',loading,'%') for procedures in range(400)]
            [print(load,'Complate_typing') for index in range(loading)]
            loading+=1
        return 'Shifrator_aktivate !!! '
        
    def number_scammer(self,number):
        return False if number==' ' else True
    
    def number_reader(self,column,index):
        return self.abc[column][index]
       
    def space_line(self):
        return ' '   
    
    def outside(self):
        return self.text
    
    def clear(self):
        self.__init__()
        
        
    def preprocessing(self):
        index=0
        while(index<len(self.code)):
            if self.number_scammer(self.code[index]):
                self.text+=self.number_reader(int(self.code[index]),int(self.code[index+1]))
                index=index+2
            else:
                self.text+=self.space_line()
                index=index+1
                
                
    def line_skiline(self):
        print('| Paste Your script |')
        print('#################')
        print('#################')
        print('#################')
        self.code=input()
        self.preprocessing()
        print('_________________')
        print('_________________')
        print(self.outside())











class Shifrator:
    def __init__(self):
        self.abc=[  ['P','O','K','J','I'],
                    ['M','L','N','Q','Z'],
                    ['E','R','T','Y','U'],
                    ['A','S','D','F','G'],
                    ['B','V','C','H','X'] ] 
        
       
        self.text=None
        self.code=''
        print('_________________________________________')
        
    
    
    def loading_aplication(self):
        loading=1
        load='#########'
        while(loading<100):
            [print('___________________________________',loading,'%') for procedures in range(500)]
            [print(load,'Complate_typing') for index in range(loading)]
            loading+=1
        return 'Shifrator_aktivate !!! '
    
    
    
    def word_scanner(self,word):
        word=str(word.upper())
        for column in range(len(self.abc)):
            moment=[1 if word in self.abc[column] else 0 for column in range(len(self.abc))]
            return True if sum(moment) else False
        
        
        
    def get_cordination(self,word):
        word=str(word.upper())
        for column in range(len(self.abc)):
            for index in range(len(self.abc)):
                if str(self.abc[column][index])==word:
                    return self.code+str(column)+str(index)
        return self.code+self.space_line()
            
    def space_line(self):
        return ' '   
    
    def clear(self):
        self.__init__()
    
    def outside(self):
        return self.code 
                
    def key_passwording(self):
        print('| Typing your text |')
        print('#################')
        print('#################')
        print('#################')
        self.text=input()
        if self.text!='fuck':
            for simvole in self.text: 
                if self.word_scanner(simvole):
                    self.code=self.get_cordination(simvole)
                else:
                    self.code=self.get_cordination(simvole)
            print( self.outside())
        else:
            return 'stop'
main()
