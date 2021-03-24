# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:07:54 2021

@author: levir
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:40:23 2021

@author: levir
"""


def revword(word:str) -> str:

    i=len(word)
    new_str= ""
    while i:
        i =i-1
        new_str = new_str + word[i]
    # new_str=new_str.lower()
    return new_str.lower()

# print(revword('RoTem'))

def countword()->int:

    
    file= open('text.txt')
    first_line = file.readline()
    count=0
    for line in file:
        line=line.rsplit()
        
        # reading each word        
        for word in line:
            
            word= revword(word)
            
            if  word in first_line:
                count= count+1
    return(count)

print(countword())    
    
            
            
            
            
            
            