#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Instructions to follow
#1 Install Python pillow package on windows
#2 Install Scipy 


# In[ ]:


from PIL import Image,ImageColor 
from scipy.stats import chisquare
filename = "image.png"
with Image.open(filename) as image: 
    width, height = image.size 
    size=image.size
    pix=image.load()


# In[ ]:


class ChiSquare:
    


# In[2]:


x=[]
chi=[]    
def chiSquareAttackTopToBottom(image,x,chi,size):
   
    width=image.size(0)
    height=image.size(1)
    block=0
    nBytes=1
    values=[0]*256
    expectedValues=[0]*128
    pov=[0]*128
    
    for i in range(length(values)):
        values[i]=1
        x[i]=i
    
    
    for j in range(height):
        
        for i in range(width):
            
            if(block < length(chi)):
                red=pix[i,j][0]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
            
            if(block < length(chi)):
                green=pix[i,j][1]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
             
            if(block < length(chi)):
                blue=pix[i,j][2]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
                


# In[ ]:


def chiSquareAttackLeftToRight(image,x,chi,size):
   
    width=image.size(0)
    height=image.size(1)
    block=0
    nBytes=1
    values=[0]*256
    expectedValues=[0]*128
    pov=[0]*128
    
    for i in range(length(values)):
        values[i]=1
        x[i]=i
    
        
    for i in range(width):
            
        for j in range(height):
            
            if(block < length(chi)):
                red=pix[i,j][0]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
            
            if(block < length(chi)):
                green=pix[i,j][1]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
             
            if(block < length(chi)):
                blue=pix[i,j][2]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1


# In[ ]:


def chiSquareAttackBottomToTop(image,x,chi,size):
   
    width=image.size(0)
    height=image.size(1)
    block=0
    nBytes=1
    values=[0]*256
    expectedValues=[0]*128
    pov=[0]*128
    
    for i in range(length(values)):
        values[i]=1
        x[i]=i
    
    
    for j in range(height-1,-1,-1):
        
        for i in range(width-1,-1,-1):
            
            if(block < length(chi)):
                red=pix[i,j][0]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
            
            if(block < length(chi)):
                green=pix[i,j][1]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
             
            if(block < length(chi)):
                blue=pix[i,j][2]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
                


# In[ ]:


def chiSquareAttackRightToLeft(image,x,chi,size):
   
    width=image.size(0)
    height=image.size(1)
    block=0
    nBytes=1
    values=[0]*256
    expectedValues=[0]*128
    pov=[0]*128
    
    for i in range(length(values)):
        values[i]=1
        x[i]=i
    
        
    for i in range(width-1,-1,-1):
            
        for j in range(height-1,-1,-1):
            
            if(block < length(chi)):
                red=pix[i,j][0]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
            
            if(block < length(chi)):
                green=pix[i,j][1]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1
             
            if(block < length(chi)):
                blue=pix[i,j][2]
                values[red]=values[red]+1
                nBytes+=1
                
                if(nbBytes > size):
                    for k in range(length(expectedValues)):
                        expectedValues[k] = (values[2*k]+values[2*k+1])/2
                        pov[k] = values[2*k]
#                         chi[block] = new ChiSquareTest().chiSquareTest(expectedValues, pov);
                        block+=1
                        nBytes=1

