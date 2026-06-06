letter = ''' Dear <|Name|>,
             You are selected! 
              <|Date|>   '''

print(letter.replace("<|Name|>", 
                 "Anay").replace ("<|Date|>", 
                    "24 Auguest 2050"))