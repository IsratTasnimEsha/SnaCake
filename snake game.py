#BISMILLAHIR RAHMANIR RAHIM

print()

import pygame
import sys
import time
from pygame.locals import *
from PIL import Image, ImageEnhance
import random

SIZE=60
TIME=.1
LEVEL=0
SCREEN_SIZE=(1538, 800)
INITIAL_LENGTH=1


class Food:

    def __init__(self, parent_screen, game_level):
        self.parent_screen=parent_screen

        if game_level==0:
            #food image in screen
            self.food=pygame.image.load('Resourses\\food0.jpg').convert()

        if game_level==1:
            self.food=pygame.image.load('Resourses\\food1.jpg').convert()

        elif game_level==2:
            self.food=pygame.image.load('Resourses\\food2.jpg').convert()

        elif game_level==3:
            self.food=pygame.image.load('Resourses\\food3.jpg').convert()

        elif game_level==4:
            self.food=pygame.image.load('Resourses\\food4.jpg').convert()

        elif game_level==5:
            self.food=pygame.image.load('Resourses\\food5.jpg').convert()

        elif game_level==6:
            self.food=pygame.image.load('Resourses\\food6.jpg').convert()

        #initial position of food
        self.move(game_level)
    
    def draw(self):
        self.parent_screen.blit(self.food, (self.x, self.y))
        pygame.display.flip()
    
    def move(self, level):
        screen_x=int(1260/SIZE)
        screen_y=int(780/SIZE)

        if level==0 or level==1:
            choice1=list(range(0, screen_x))
            choice2=list(range(0, screen_y))
            self.x=random.choice(choice1)*SIZE
            self.y=random.choice(choice2)*SIZE

        elif level==2:
            choice1=list(range(1, screen_x-1))
            choice2=list(range(1, screen_y-1))
            self.x=random.choice(choice1)*SIZE
            self.y=random.choice(choice2)*SIZE

        elif level==3:
            border=[]

            for j in range(0, 780, SIZE):
                if j==SIZE*4  or j==SIZE*8:
                    for k in range(0, 4*SIZE, SIZE):
                        border.append([k, j])
                    for k in range(1260-5*SIZE,  1260, SIZE):
                        border.append([k, j])

                elif j==5*SIZE or j==6*SIZE or j==7*SIZE:
                    for k in range(0, 1260, SIZE):
                        border.append([k, j])

                elif j==0 or j==780-SIZE:
                    for k in range(4*SIZE, 1260-4*SIZE, SIZE):
                        border.append([k, j])
            
                elif j==SIZE or j==SIZE*2 or j==SIZE*3 or j==780-2*SIZE or j==780-3*SIZE or j==780-4*SIZE:
                    for k in range(SIZE, 1260-SIZE, SIZE):
                        border.append([k, j])    

            self.x, self.y=random.choice(border)

        elif level==4:
            border2=[]

            for j in range(0, 780, SIZE):
                if  j==SIZE*2:
                    for k in range(0, 1260-7*SIZE, SIZE):
                        if k!=6*SIZE:
                            border2.append([k, j])

                elif j==SIZE*10:
                    for k in range(8*SIZE, 1260, SIZE):
                        if k!=1260-SIZE*7:
                            border2.append([k, j])
                    
            for k in range(0, 1260, SIZE):
                if k==SIZE*6:
                    for j in range(8*SIZE, 780, SIZE):
                        if j!= 780-SIZE*3:
                            border2.append([k, j])

                elif k==1260-SIZE*7:
                    for j in range(0, 780-8*SIZE, SIZE):
                        if j!=SIZE*2:
                            border2.append([k, j])

            self.x, self.y=random.choice(border2)

        elif level==5:
            border3=[]

            for j in range(0, 780, SIZE):
                if j==SIZE*3  or j==SIZE*9:
                    for k in range(SIZE, 5*SIZE, SIZE): 
                        border3.append([k, j])
                    for k in range(1260-5*SIZE, 1260-SIZE, SIZE):
                        border3.append([k, j])
                
                elif j==SIZE or j==2*SIZE or  j==SIZE*4 or j==SIZE*8 or j==10*SIZE or j==11*SIZE:
                    for k in range(SIZE, 1260-SIZE, SIZE): 
                        border3.append([k, j])
                        
            for k in range(0, 1260, SIZE):
                if k==0  or k==1260-SIZE:
                    for j in range(5*SIZE, 8*SIZE, SIZE):
                        border3.append([k, j])

            self.x, self.y=random.choice(border3)
        
        elif level==6:
            border4=[]

            for j in range(0, 780, SIZE):
                if j==780-SIZE*9:
                    for k in range(SIZE*9, SIZE*12, SIZE):
                        border4.append([k, j])
                    
                elif j==0:
                    for k in range(SIZE*3, SIZE*6, SIZE):
                        border4.append([k, j])
                    for k in range(1260-SIZE*3, 1260, SIZE):
                        border4.append([k, j])
            
            for k in range(0, 1260, SIZE):
                if k==SIZE*12:
                    for j in range(SIZE, 780-SIZE*6, SIZE):
                        if j!=SIZE*4:
                            border4.append([k, j])

                elif k==SIZE*8:
                    for j in range(SIZE*5, 780, SIZE):
                        if j!=SIZE*7:
                            border4.append([k, j])

                elif k==0:
                    for j in range(SIZE*3, 780, SIZE):
                        if  j!=SIZE*4 and j!=SIZE*7:
                            border4.append([k, j])

            self.x, self.y=random.choice(border4)
        

class Snake:

    def __init__(self, parent_screen, length, game_level):
        self.parent_screen=parent_screen

        if game_level==0:
            self.block_initial=pygame.image.load('Resourses\\block_initial0.png').convert()
            self.block=pygame.image.load('Resourses\\block0.png').convert()

        elif game_level==1:
            self.block_initial=pygame.image.load('Resourses\\block_initial1.png').convert()
            self.block=pygame.image.load('Resourses\\block1.png').convert()

        elif game_level==2:
            self.block_initial=pygame.image.load('Resourses\\block_initial2.png').convert()
            self.block=pygame.image.load('Resourses\\block2.png').convert()

        elif game_level==3:
            self.block_initial=pygame.image.load('Resourses\\block_initial3.png').convert()
            self.block=pygame.image.load('Resourses\\block3.png').convert()

        elif game_level==4:
            self.block_initial=pygame.image.load('Resourses\\block_initial4.png').convert()
            self.block=pygame.image.load('Resourses\\block4.png').convert()

        elif game_level==5:
            self.block_initial=pygame.image.load('Resourses\\block_initial5.png').convert()
            self.block=pygame.image.load('Resourses\\block5.png').convert()

        elif game_level==6:
            self.block_initial=pygame.image.load('Resourses\\block_initial6.png').convert()
            self.block=pygame.image.load('Resourses\\block6.png').convert()

        #Length of snake
        self.length=length

        #Initial position of snake
        self.x=[SIZE]*length
        self.y=[6*SIZE]*length

        #Initial direction of block
        self.direction='right'

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        if self.direction!='down':
            self.direction='up'
    
    def move_down(self):
        if self.direction!='up':
            self.direction='down'

    def move_left(self):
        if self.direction!='right':
            self.direction='left'

    def move_right(self):
        if self.direction!='left':
            self.direction='right'

    def draw(self):
        self.parent_screen.blit(self.block_initial, (self.x[0], self.y[0]))
        for i in range(1, self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

        #Display screen
        pygame.display.flip()

    def last_border(self):
        self.border_block=pygame.image.load('Resourses\\border_side.jpg').convert()
        for i in range(0, 780, 20):
            self.parent_screen.blit(self.border_block, (1260, i))

        self.border_block=pygame.image.load('Resourses\\border_side.jpg').convert()
        for i in range(0, 1538, 20):
            self.parent_screen.blit(self.border_block, (i, 780))

    def walk1(self):
        self.last_border()

        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if self.y[0]-SIZE<0:
                self.y[0]=780-SIZE
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if self.y[0]+SIZE>780-SIZE:
                self.y[0]=0
            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':
            if self.x[0]-SIZE<0:
                self.x[0]=1260-SIZE
            else:
                 self.x[0]-=SIZE
            
        elif self.direction=='right':
            if self.x[0]+SIZE>1260-SIZE:
                self.x[0]=0
            else:
                self.x[0]+=SIZE
            
        self.draw()

    def walk2(self):
        self.last_border()
        self.border_block=pygame.image.load('Resourses\\border_block2.jpg').convert()

        for i in range(0, 1260, SIZE):
            self.parent_screen.blit(self.border_block, (i, 0))
            self.parent_screen.blit(self.border_block, (i, 780-SIZE))
        
        for i in range(SIZE, 780-SIZE, SIZE):
            self.parent_screen.blit(self.border_block, (0, i))
            self.parent_screen.blit(self.border_block, (1260-SIZE, i))

        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if self.y[0]-SIZE<SIZE:
                self.play_sound('crash')
                raise "Game over"
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if self.y[0]+SIZE>780-2*SIZE:
                self.play_sound('crash')
                raise "Game over"
            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':
            if self.x[0]-SIZE<SIZE:
                self.play_sound('crash')
                raise "Game over"
            else:
                 self.x[0]-=SIZE
            
        elif self.direction=='right':
            if self.x[0]+SIZE>1260-2*SIZE:
                self.play_sound('crash')
                raise "Game over"
            else:
                self.x[0]+=SIZE
            
        self.draw()
       
    def walk3(self):
        self.last_border()
        self.border_block=pygame.image.load('Resourses\\border_block3.jpg').convert()
        
        for j in range(0, 780, SIZE):
            if j==SIZE*4  or j==SIZE*8:
                for k in range(5*SIZE, 1260-6*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
            
            if j==0 or j==780-SIZE:
                for k in range(0, 4*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                for k in range(1260-4*SIZE, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
            
            if j==SIZE or j==SIZE*2 or j==SIZE*3 or j==780-2*SIZE or j==780-3*SIZE or j==780-4*SIZE:
                for k in range(0, SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                for k in range(1260-SIZE, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if (self.y[0]-SIZE==SIZE*4 or  self.y[0]-SIZE==SIZE*8) and self.x[0] in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]-SIZE==0 or self.y[0]-SIZE==780-SIZE) and (self.x[0] in range(0, 4*SIZE, SIZE) or 
                self.x[0] in range(1260-4*SIZE, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]-SIZE==SIZE or self.y[0]-SIZE==SIZE*2 or self.y[0]-SIZE==SIZE*3 or self.y[0]-SIZE==780-2*SIZE or 
                self.y[0]-SIZE==780-3*SIZE or self.y[0]-SIZE==780-4*SIZE) and (self.x[0]==0 or self.x[0]==1260-SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]-SIZE<0:
                self.y[0]=780-SIZE
                      
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if (self.y[0]+SIZE==SIZE*4 or  self.y[0]+SIZE==SIZE*8) and self.x[0] in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]+SIZE==0 or self.y[0]+SIZE==780 or self.y[0]+SIZE==780-SIZE) and (self.x[0] in range(0, 4*SIZE, SIZE) or 
                self.x[0] in range(1260-4*SIZE, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]+SIZE==SIZE or self.y[0]+SIZE==SIZE*2 or self.y[0]+SIZE==SIZE*3 or self.y[0]+SIZE==780-2*SIZE or 
                self.y[0]+SIZE==780-3*SIZE or self.y[0]+SIZE==780-4*SIZE) and (self.x[0]==0 or self.x[0]==1260-SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]+SIZE>780-SIZE:
                self.y[0]=0

            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':
            if (self.y[0]==SIZE*4 or  self.y[0]==SIZE*8) and self.x[0]-SIZE in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]==0 or self.y[0]==780-SIZE) and (self.x[0]-SIZE in range(0, 4*SIZE, SIZE) or 
                self.x[0]-SIZE in range(1260-4*SIZE, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]==SIZE or self.y[0]==SIZE*2 or self.y[0]==SIZE*3 or self.y[0]==780-2*SIZE or 
                self.y[0]==780-3*SIZE or self.y[0]==780-4*SIZE) and (self.x[0]-SIZE==0 or self.x[0]-SIZE==1260-SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE<0:
                self.x[0]=1260-SIZE

            else:
                self.x[0]-=SIZE
            
        elif self.direction=='right':
            if (self.y[0]==SIZE*4 or  self.y[0]==SIZE*8) and self.x[0]+SIZE in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]==0 or self.y[0]==780-SIZE) and (self.x[0]+SIZE in range(0, 4*SIZE, SIZE) or self.x[0]+SIZE==1260 or
                self.x[0]+SIZE in range(1260-4*SIZE, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]==SIZE or self.y[0]==SIZE*2 or self.y[0]==SIZE*3 or self.y[0]==780-2*SIZE or 
                self.y[0]==780-3*SIZE or self.y[0]==780-4*SIZE) and (self.x[0]+SIZE==1260 or self.x[0]+SIZE==1260-SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE>1260-SIZE:
                self.x[0]=0

            else:
                self.x[0]+=SIZE
            
        self.draw()

    def walk4(self):
        self.last_border()
        self.border_block=pygame.image.load('Resourses\\border_block4.jpg').convert()
        
        for j in range(0, 780, SIZE):
            if  j==SIZE*2:
                for k in range(1260-7*SIZE, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

            if j==SIZE*10:
                for k in range(0, 7*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                
        for k in range(0, 1260, SIZE):
            if k==SIZE*6:
                for j in range(0, 8*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

            if k==1260-SIZE*7:
                for j in range(780-8*SIZE, 780, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
            
        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if self.y[0]-SIZE==SIZE*2 and self.x[0] in range(1260-7*SIZE, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]-SIZE==SIZE*10 and self.x[0] in range(0, 7*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==SIZE*6 and self.y[0]-SIZE in range(0, 8*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==1260-SIZE*7 and self.y[0]-SIZE in range(780-8*SIZE, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]-SIZE<0:
                self.y[0]=780-SIZE
                        
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if self.y[0]+SIZE==SIZE*2 and self.x[0] in range(1260-7*SIZE, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]+SIZE==SIZE*10 and self.x[0] in range(0, 7*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==SIZE*6 and (self.y[0]+SIZE in range(0, 8*SIZE, SIZE) or self.y[0]+SIZE==780):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==1260-SIZE*7 and self.y[0]+SIZE in range(780-8*SIZE, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]+SIZE>780-SIZE:
                self.y[0]=0
            
            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':
            if self.y[0]==SIZE*2 and self.x[0]-SIZE in range(1260-7*SIZE, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]==SIZE*10 and self.x[0]-SIZE in range(0, 7*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE==SIZE*6 and self.y[0] in range(0, 8*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE==1260-SIZE*7 and self.y[0] in range(780-8*SIZE, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE<0:
                self.x[0]=1260-SIZE

            else:
                self.x[0]-=SIZE
            
        elif self.direction=='right':
            if self.y[0]==SIZE*2 and self.x[0]+SIZE in range(1260-7*SIZE, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]==SIZE*10 and (self.x[0]+SIZE in range(0, 7*SIZE, SIZE) or self.x[0]+SIZE==1260):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE==SIZE*6 and self.y[0] in range(0, 8*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE==1260-SIZE*7 and self.y[0] in range(780-8*SIZE, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE>1260-SIZE:
                self.x[0]=0
            
            else:
                self.x[0]+=SIZE
            
        self.draw()

    def walk5(self):
        self.last_border()
        self.border_block=pygame.image.load('Resourses\\border_block5.png').convert()
        
        for j in range(0, 780, SIZE):
            if j==SIZE*3  or j==SIZE*9:
                for k in range(5*SIZE, 1260-6*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
            
            if j==0 or j==780-SIZE:
                for k in range(0, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k,  j))
        
        for k in range(0, 1260, SIZE):
            if k==0  or k==1260-SIZE:
                for j in range(0, 5*SIZE, SIZE):
                    self.parent_screen.blit(self.border_block, (k,  j))
                for j in range(8*SIZE, 780, SIZE):
                    self.parent_screen.blit(self.border_block, (k,  j))

        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if (self.y[0]-SIZE==SIZE*3  or self.y[0]-SIZE==SIZE*9) and self.x[0] in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]-SIZE==0 or self.y[0]-SIZE==780-SIZE) and self.x[0] in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif (self.x[0]==0  or self.x[0]==1260-SIZE) and (self.y[0]-SIZE in range(0, 5*SIZE, SIZE) or self.y[0]-SIZE in range(8*SIZE, 780, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]-SIZE<0:
                self.y[0]=780-SIZE
           
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if (self.y[0]+SIZE==SIZE*3  or self.y[0]+SIZE==SIZE*9) and self.x[0] in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif (self.y[0]+SIZE==780 or self.y[0]+SIZE==780-SIZE) and self.x[0] in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif (self.x[0]==0  or self.x[0]==1260-SIZE) and (self.y[0]+SIZE in range(0, 5*SIZE, SIZE) or 
            self.y[0]+SIZE==780 or self.y[0]+SIZE in range(8*SIZE, 780, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]+SIZE>780-SIZE:
                self.y[0]=0
            
            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':
            if (self.y[0]==SIZE*3  or self.y[0]==SIZE*9) and self.x[0]-SIZE in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"
    
            elif (self.y[0]==0 or self.y[0]==780-SIZE) and self.x[0]-SIZE in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif (self.x[0]-SIZE==0  or self.x[0]-SIZE==1260-SIZE) and (self.y[0] in range(0, 5*SIZE, SIZE) or self.y[0] in range(8*SIZE, 780, SIZE)):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE<0:
                self.x[0]=1260-SIZE

            else:
                self.x[0]-=SIZE
            
        elif self.direction=='right':
            if (self.y[0]==SIZE*3  or self.y[0]==SIZE*9) and self.x[0]+SIZE in range(5*SIZE, 1260-6*SIZE, SIZE):
                self.play_sound('crash')
                raise "Game over"
        
            elif (self.y[0]==0 or self.y[0]==780-SIZE) and self.x[0]+SIZE in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif (self.x[0]+SIZE==1260 or self.x[0]+SIZE==1260-SIZE) and (self.y[0] in range(0, 5*SIZE, SIZE) or self.y[0] in range(8*SIZE, 780, SIZE)):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]+SIZE>1260-SIZE:
                self.x[0]=0

            else:
                self.x[0]+=SIZE
            
        self.draw()

    def walk6(self):
        self.last_border()
        self.border_block=pygame.image.load('Resourses\\border_block6.jpg').convert()
        
        for j in range(0, 780, SIZE):
            if j==780-SIZE*6:
                for k in range(0, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
            
            if j==780-SIZE*9:
                for k in range(0, SIZE*9, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                for k in range(SIZE*12, 1260, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                
            if j==0:
                for k in range(0, SIZE*3, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
                for k in range(SIZE*6, 1260-SIZE*3, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))
           
        for k in range(0, 1260, SIZE):
            if k==SIZE*12:
                for j in range(780-SIZE*5, 780, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

            if k==SIZE*8:
                for j in range(SIZE, SIZE*5, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

            if k==0:
                for j in range(SIZE, SIZE*3, SIZE):
                    self.parent_screen.blit(self.border_block, (k, j))

        for i in range(self.length-1, 0, -1):                
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction=='up':
            if self.y[0]-SIZE==780-SIZE*6 and self.x[0] in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
                
            elif self.y[0]-SIZE==780-SIZE*9 and(self.x[0] in range(0, SIZE*9, SIZE) or self.x[0] in range(SIZE*12, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"
                    
            elif self.y[0]-SIZE==0 and (self.x[0] in range(0, SIZE*3, SIZE) or self.x[0] in range(SIZE*6, 1260-SIZE*3, SIZE)):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]==SIZE*12 and self.y[0]-SIZE in range(780-SIZE*5, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==SIZE*8 and self.y[0]-SIZE in range(SIZE, SIZE*5, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==0 and self.y[0]-SIZE in range(SIZE, SIZE*3, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.y[0]-SIZE<0:
                self.y[0]=780-SIZE
              
            else:
                self.y[0]-=SIZE
        
        elif self.direction=='down':
            if self.y[0]+SIZE==780-SIZE*6 and self.x[0] in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
                
            elif self.y[0]+SIZE==780-SIZE*9 and(self.x[0] in range(0, SIZE*9, SIZE) or self.x[0] in range(SIZE*12, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"
                    
            elif self.y[0]+SIZE==780 and (self.x[0] in range(0, SIZE*3, SIZE) or self.x[0] in range(SIZE*6, 1260-SIZE*3, SIZE)):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]==SIZE*12 and self.y[0]+SIZE in range(780-SIZE*5, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==SIZE*8 and self.y[0]+SIZE in range(SIZE, SIZE*5, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]==0 and self.y[0]+SIZE in range(SIZE, SIZE*3, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.y[0]+SIZE>780-SIZE:
                self.y[0]=0

            else:
                self.y[0]+=SIZE
            
        elif self.direction=='left':         
            if self.y[0]==780-SIZE*6 and self.x[0]-SIZE in range(0, 1260, SIZE):
                self.play_sound('crash')
                raise "Game over"
                
            elif self.y[0]==780-SIZE*9 and(self.x[0]-SIZE in range(0, SIZE*9, SIZE) or self.x[0]-SIZE in range(SIZE*12, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"
                    
            elif self.y[0]==0 and (self.x[0]-SIZE in range(0, SIZE*3, SIZE) or self.x[0]-SIZE in range(SIZE*6, 1260-SIZE*3, SIZE)):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]-SIZE==SIZE*12 and self.y[0] in range(780-SIZE*5, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE==SIZE*8 and self.y[0] in range(SIZE, SIZE*5, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE==0 and self.y[0] in range(SIZE, SIZE*3, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]-SIZE<0:
                self.x[0]=1260-SIZE

            else:
                self.x[0]-=SIZE
            
        elif self.direction=='right':
            if self.y[0]==780-SIZE*6 and (self.x[0]+SIZE in range(0, 1260, SIZE) or self.x[0]+SIZE==1260):
                self.play_sound('crash')
                raise "Game over"
                
            elif self.y[0]==780-SIZE*9 and(self.x[0]+SIZE in range(0, SIZE*9, SIZE) or self.x[0]+SIZE in range(SIZE*12, 1260, SIZE)):
                self.play_sound('crash')
                raise "Game over"
                    
            elif self.y[0]==0 and (self.x[0]+SIZE in range(0, SIZE*3, SIZE) or self.x[0]+SIZE in range(SIZE*6, 1260-SIZE*3, SIZE)):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]+SIZE==SIZE*12 and self.y[0] in range(780-SIZE*5, 780, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE==SIZE*8 and self.y[0] in range(SIZE, SIZE*5, SIZE):
                self.play_sound('crash')
                raise "Game over"

            elif self.x[0]+SIZE==1260 and self.y[0] in range(SIZE, SIZE*3, SIZE):
                self.play_sound('crash')
                raise "Game over"
            
            elif self.x[0]+SIZE>1260-SIZE:
                self.x[0]=0

            else:
                self.x[0]+=SIZE
            
        self.draw()


class Game:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        self.background_music()
        #Main screen of game
        self.surface=pygame.display.set_mode(SCREEN_SIZE) #(width, height)
        self.snake=Snake(self.surface, INITIAL_LENGTH, LEVEL)
        self.snake.draw()
        self.food=Food(self.surface, LEVEL)
        self.food.draw()

    def page_background(self, background_image):
        #background image in screen
        page_background_color=pygame.image.load(background_image)
        self.surface.blit(page_background_color, (0, 0))

    def show_buttons(self, level):
        color = (0, 0, 0)

        if level==3:
            color_light = (72, 72, 72)
        else:
            color_light = (255, 255, 255)

        if level==0:
            color_dark = (255, 0, 255)

        if level==1:
            color_dark = (238, 201, 0)

        elif level==2:
            color_dark = (144, 0, 0)
        
        elif level==3:
            color_dark = (255, 255, 255)

        elif level==4:
            color_dark = (13, 89, 1)

        elif level==5:
            color_dark = (0, 171, 240)

        elif level==6:
            color_dark = (72, 72, 72)

        width = self.surface.get_width()
        height = self.surface.get_height()

        smallfont = pygame.font.SysFont('comicsansms', SIZE-20)
        self.text3 = smallfont.render('  End Game' , True , color)

        mouse = pygame.mouse.get_pos()

        if 1293 <= mouse[0] <= 1293 + 225 and 60 <= mouse[1] <= 60 + 65:
            pygame.draw.rect(self.surface,color_light,[1293, 60, 225, 65])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1293, 60, 225, 65])
        self.surface.blit(self.text3, (1293, 60))

    def moving_keys(self, level):

        color = (51, 51, 56)
        color_light = (0, 0, 0)
        color_dark = (0, 114, 160)
        width = self.surface.get_width()
        height = self.surface.get_height()

        smallfont = pygame.font.SysFont('comicsansms', SIZE-30, 'bold')

        if level==0:
            self.key_up = pygame.image.load('Resourses\\key_up0.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down0.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left0.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right0.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause0.png').convert()

        if level==1:
            self.key_up = pygame.image.load('Resourses\\key_up1.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down1.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left1.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right1.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause1.png').convert()

        elif level==2:
            self.key_up = pygame.image.load('Resourses\\key_up2.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down2.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left2.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right2.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause2.png').convert()

        elif level==3:
            self.key_up = pygame.image.load('Resourses\\key_up3.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down3.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left3.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right3.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause3.png').convert()

        elif level==4:
            self.key_up = pygame.image.load('Resourses\\key_up4.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down4.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left4.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right4.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause4.png').convert()

        elif level==5:
            self.key_up = pygame.image.load('Resourses\\key_up5.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down5.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left5.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right5.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause5.png').convert()

        elif level==6:
            self.key_up = pygame.image.load('Resourses\\key_up6.png').convert()
            self.key_down = pygame.image.load('Resourses\\key_down6.png').convert()
            self.key_left = pygame.image.load('Resourses\\key_left6.png').convert()
            self.key_right = pygame.image.load('Resourses\\key_right6.png').convert()
            self.key_pause=pygame.image.load('Resourses\\key_pause6.png').convert()

        mouse = pygame.mouse.get_pos()

        if 1370 <= mouse[0] <= 1370 +70 and 510 <= mouse[1] <= 510 + 70:
            pygame.draw.rect(self.surface,color_light,[1370, 510, 70, 70])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1370, 510, 70, 70])
        self.surface.blit(self.key_up, (1370, 510))

        if 1370 <= mouse[0] <= 1370 +70 and 670 <= mouse[1] <= 670 + 70:
            pygame.draw.rect(self.surface,color_light,[1370, 670, 70, 70])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1370, 670, 70, 70])
        self.surface.blit(self.key_down, (1370, 670))

        if 1295 <= mouse[0] <= 1295 +70 and 590 <= mouse[1] <= 590 + 70:
            pygame.draw.rect(self.surface,color_light,[1290, 590, 70, 70])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1290, 590, 70, 70])
        self.surface.blit(self.key_left, (1290, 590))

        if 1450 <= mouse[0] <= 1450 +70 and 590 <= mouse[1] <= 590 +70:
            pygame.draw.rect(self.surface,color_light,[1450, 590, 70, 70])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1450, 590, 70, 70])
        self.surface.blit(self.key_right, (1450, 590))

        if 1375 <= mouse[0] <= 1375 + 60 and 595 <= mouse[1] <= 595 + 60:
            pygame.draw.rect(self.surface,color_light,[1375, 595, 60, 60])  
        else:
            pygame.draw.rect(self.surface,color_dark,[1375, 595, 60, 60])
        self.surface.blit(self.key_pause, (1375, 595))

    def display_score(self, level_high_score, level, time, roundd, extra):  
        if level==0:
            main_score=int((self.snake.length-INITIAL_LENGTH) * (1/time)*roundd +extra)
        else:
            main_score=int(((self.snake.length-INITIAL_LENGTH) * (1/time))+ ((level-1)*(10/time)*roundd)+extra)
        
        with open(level_high_score, 'r') as h_score:
            for i in h_score:
                i=i.strip()
                p=i.split(' ')
        
        high_score=int(p[0])

        if main_score>high_score:
            high_score=main_score
            with open(level_high_score, 'w') as h_score:
                h_score.write(str(high_score))

        font=pygame.font.SysFont('comicsansms', SIZE-22)

        if level==0:
            font_color = (255, 0, 255)

        elif level==1:
            font_color= (238, 201, 0)

        elif level==2:
            font_color = (144, 0, 0)

        elif level==3:
            font_color = (255, 255, 255)

        elif level==4:
            font_color = (13, 89, 1)

        elif level==5:
            font_color = (0, 171, 240)
        
        elif level==6:
            font_color = (72, 72, 72)
        
        else:
            font_color = (0, 114, 160)

        score=font.render(f"Score:", True, font_color)
        self.surface.blit(score, (1300, 160))

        score=font.render(f"{main_score}", True, font_color)
        self.surface.blit(score, (1300, 200))

        hi_score=font.render(f"High Score:", True, font_color)
        self.surface.blit(hi_score, (1300, 250))

        hi_score=font.render(f"{high_score}", True, font_color)
        self.surface.blit(hi_score, (1300, 290))

        if level!=0:
            foods=font.render(f"Remaining", True, font_color)
            self.surface.blit(foods, (1300, 365))
            foods=font.render(f"Cakes: {roundd*10-((self.snake.length-INITIAL_LENGTH)%(roundd*10))}", True, font_color)
            self.surface.blit(foods, (1300, 405))

    def show_game_over(self, level_high_score, extra_score, time, roundd, extra):
        self.page_background('Resourses\\page_game_over.jpg')

        main_score=int(((self.snake.length-INITIAL_LENGTH) * (1/time))+extra_score*roundd+ extra)
        
        with open(level_high_score, 'r') as h_score:
            for i in h_score:
                i=i.strip()
                p=i.split(' ')
        
        high_score=int(p[0])

        if main_score>high_score:
            high_score=main_score
            with open(level_high_score, 'w') as h_score:
                h_score.write(str(high_score))

        font=pygame.font.SysFont('comicsansms', SIZE+45)

        game_over=font.render(f"GAME IS OVER!!!", True, (0, 0, 0))
        self.surface.blit(game_over, (400, 130))

        font=pygame.font.SysFont('comicsansms', SIZE+15)

        game_over=font.render(f"Your Score: {main_score}", True, (0, 0, 0))
        self.surface.blit(game_over, (525, 320))

        replay=font.render(f"High Score: {high_score}", True, (0, 0, 0))
        self.surface.blit(replay, (525, 435))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self, level):
        self.snake=Snake(self.surface, INITIAL_LENGTH, level)
        self.food=Food(self.surface, level)
    
    def background_music(self):
        pygame.mixer.music.load('Resourses\\tune_of_backgrond.mp3')
        pygame.mixer.music.play(-1, 0) #-1=continuos music, 0=music from starting

    def play_sound(self, sound):
        if sound=='food':
            sound=pygame.mixer.Sound('Resourses\\tune_of_food.mp3')
        if sound=='crash':
            sound=pygame.mixer.Sound('Resourses\\tune_of_crash.mp3')
        pygame.mixer.Sound.play(sound)
        
    def play(self, level, time, roundd, extra):
        if level==0:
            self.page_background('Resourses\\page_background0.jpg')
            self.snake.walk1()

        if level==1:
            self.page_background('Resourses\\page_background1.jpg')
            self.snake.walk1()

        if level==2:
            self.page_background('Resourses\\page_background2.jpg')
            self.snake.walk2()

        if level==3:
            self.page_background('Resourses\\page_background3.jpg')
            self.snake.walk3()

        if level==4:
            self.page_background('Resourses\\page_background4.jpg')
            self.snake.walk4()

        if level==5:
            self.page_background('Resourses\\page_background5.jpg')
            self.snake.walk5()

        if level==6:
            self.page_background('Resourses\\page_background6.jpg')
            self.snake.walk6()

        self.food.draw()

        if level==0:
            self.display_score('Resourses\\classic_high_score.txt', level, time, roundd, extra)

        else:
            self.display_score('Resourses\\campaign_high_score.txt', level, time, roundd, extra)

        self.show_buttons(level)

        self.moving_keys(level)
        
        pygame.display.flip()
    
        
        #Snake collision with food
        if self.is_collison(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.play_sound('food')
            self.snake.increase_length()
            self.food.move(level)
        
        #Snake collision with itself
        for i in range(4, self.snake.length):
            if self.is_collison(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound('crash')
                raise "Game over"

    def is_collison(self, x1, y1, x2, y2):
        if x1==x2 and x1<=x2+SIZE:
            if y1==y2 and y1<=y2+SIZE:
                return True

        return False

    def show_high_score(self):
        self.page_background('Resourses\\page_score.jpg')

        with open('Resourses\\classic_high_score.txt', 'r') as classic_h_score:
            for i in classic_h_score:
                i=i.strip()
                p=i.split(' ')
        
        with open('Resourses\\campaign_high_score.txt', 'r') as campaign_h_score:
            for i in campaign_h_score:
                i=i.strip()
                q=i.split(' ')

        font=pygame.font.SysFont('comicsansms', SIZE-10)

        classic_high_score=font.render(f"CLASSIC HIGH SCORE: {p[0]}", True, (0, 171, 240))
        self.surface.blit(classic_high_score, (40, 320))

        campaign_high_score=font.render(f"CAMPAIGN HIGH SCORE: {q[0]}", True, (0, 171, 240))
        self.surface.blit(campaign_high_score, (40, 430))

        pygame.display.flip()


    def run(self):
        page1=True
        page2=False
        page3=False
        page4=False
        page5=False
        page6=False
        page7=False
        page8=False
        EXTRA=0
        ROUND=1

        while page1:

            self.page_background('Resourses\\page_menu.jpg')
            color = (0, 0, 0)
            color_light = (51, 51, 56)
            color_dark = (0, 114, 160)
            width = self.surface.get_width()
            height = self.surface.get_height()

            smallfont = pygame.font.SysFont('comicsansms', SIZE+27, 'bold')

            text1 = smallfont.render(' CLASSIC' , True , color)
            text2 = smallfont.render(' CAMPAIGN' , True , color)    
            text3 = smallfont.render(' HIGH SCORE' , True , color)

            mouse = pygame.mouse.get_pos()
                
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()

                if i.type == pygame.MOUSEBUTTONDOWN:
                    if 520 <= mouse[0] <= 520 +530 and 125 <= mouse[1] <= 125+125:
                        page1=False
                        page6=True

                    if 455 <= mouse[0] <= 455+665 and 300 <= mouse[1] <= 300+125:
                        page1=False
                        page7=True
                                          
                    if 400 <= mouse[0] <= 400+765 and 475 <= mouse[1] <= 475+125:
                        page1=False
                        page3=True

                if 520 <= mouse[0] <= 520 +510 and 125 <= mouse[1] <= 125+125:
                    pygame.draw.rect(self.surface,color_light,[520, 125, 510, 125])  
                else:
                    pygame.draw.rect(self.surface,color_dark,[520, 125, 510, 125])
                self.surface.blit(text1, (520, 125))

                if 470 <= mouse[0] <= 470+615 and 300 <= mouse[1] <= 300+125:
                    pygame.draw.rect(self.surface,color_light,[470, 300, 615, 125])  
                else:
                    pygame.draw.rect(self.surface,color_dark,[470, 300, 615, 125])
                self.surface.blit(text2, (470, 300))

                if 425 <= mouse[0] <= 425+705 and 475 <= mouse[1] <= 475+125:
                    pygame.draw.rect(self.surface,color_light,[425, 475, 705, 125])  
                else:
                    pygame.draw.rect(self.surface,color_dark,[425, 475, 705, 125])
                self.surface.blit(text3, (425, 475))

                pygame.display.update()
                pygame.display.flip()

        if page6:
            self.page_background('Resourses\\page_level.jpg')
            running=True
            while running:

                color = (0, 0, 0)
                color_light = (51, 51, 56)
                color_dark = (0, 114, 160)
                width = self.surface.get_width()
                height = self.surface.get_height()

                smallfont = pygame.font.SysFont('comicsansms', SIZE-25)
                textt = smallfont.render('  Home Page' , True , color)

                smallfont = pygame.font.SysFont('comicsansms', SIZE+10)

                textt1 = smallfont.render('  LEVEL: 1' , True , color)
                textt2 = smallfont.render('  LEVEL: 2' , True , color)
                textt3 = smallfont.render('  LEVEL: 3' , True , color)
                textt4 = smallfont.render('  LEVEL: 4' , True , color)
                textt5 = smallfont.render('  LEVEL: 5' , True , color)
                textt6 = smallfont.render('  LEVEL: 6' , True , color)
                textt7 = smallfont.render('  LEVEL: 7' , True , color)
                textt8 = smallfont.render('  LEVEL: 8' , True , color)

                mouse = pygame.mouse.get_pos()

                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit() 

                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                            running=False
                            page6=False
                            page1=True
                            self.run()
                            
                        if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 100+102:
                            TIME=1
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0
                        
                        if 855 <= mouse[0] <= 855 +370 and 100 <= mouse[1] <= 100+102:
                            TIME=.5
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0
                        
                        if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 250+102:
                            TIME=.25
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0

                        if 855 <= mouse[0] <= 855 +370 and 250 <= mouse[1] <= 250+102:
                            TIME=.2
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0

                        if 320 <= mouse[0] <= 320 +370 and 400 <= mouse[1] <= 400+102:
                            TIME=.1
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0

                        if 855 <= mouse[0] <= 855 +370 and 400 <= mouse[1] <= 400+102:
                            TIME=.05
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0

                        if 320 <= mouse[0] <= 320 +370 and 550 <= mouse[1] <= 550+102:
                            TIME=.025
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0
                        
                        if 855 <= mouse[0] <= 855 +370 and 550 <= mouse[1] <= 550+102:
                            TIME=.02
                            running=False
                            page6=False
                            page2=True
                            LEVEL=0

                    if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                        pygame.draw.rect(self.surface,color_light,[1300, 30, 215, 60])  
                    else:
                        pygame.draw.rect(self.surface,color_dark,[1300, 30, 215, 60])
                    self.surface.blit(textt, (1300, 30))

                    if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 100+102:
                        pygame.draw.rect(self.surface,color_light,[320, 100, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 100, 370, 102])
                    self.surface.blit(textt1, (320, 100))

                    if 855 <= mouse[0] <= 855 +370 and 100 <= mouse[1] <= 100+102:
                        pygame.draw.rect(self.surface,color_light,[855, 100, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 100, 370, 102])
                    self.surface.blit(textt2, (855, 100))

                    if 320 <= mouse[0] <= 320 +370 and 250 <= mouse[1] <= 250+102:
                        pygame.draw.rect(self.surface,color_light,[320, 250, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 250, 370, 102])
                    self.surface.blit(textt3, (320, 250))

                    if 855 <= mouse[0] <= 855 +370 and 250 <= mouse[1] <= 250+102:
                        pygame.draw.rect(self.surface,color_light,[855, 250, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 250, 370, 102])
                    self.surface.blit(textt4, (855, 250))

                    if 320 <= mouse[0] <= 320 +370 and 400 <= mouse[1] <= 400+102:
                        pygame.draw.rect(self.surface,color_light,[320, 400, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 400, 370, 102])
                    self.surface.blit(textt5, (320, 400))

                    if 855 <= mouse[0] <= 855 +370 and 400 <= mouse[1] <= 400+102:
                        pygame.draw.rect(self.surface,color_light,[855, 400, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 400, 370, 102])
                    self.surface.blit(textt6, (855, 400))

                    if 320 <= mouse[0] <= 320 +370 and 550 <= mouse[1] <= 550+102:
                        pygame.draw.rect(self.surface,color_light,[320, 550, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 550, 370, 102])
                    self.surface.blit(textt7, (320, 550))

                    if 855 <= mouse[0] <= 855 +370 and 550 <= mouse[1] <= 550+102:
                        pygame.draw.rect(self.surface,color_light,[855, 550, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 550, 370, 102])
                    self.surface.blit(textt8, (855, 550))

                    pygame.display.update()
                    pygame.display.flip()
                    

        if page7:
            self.page_background('Resourses\\page_level.jpg')
            running=True
            while running:

                color = (0, 0, 0)
                color_light = (51, 51, 56)
                color_dark = (0, 114, 160)
                width = self.surface.get_width()
                height = self.surface.get_height()

                smallfont = pygame.font.SysFont('comicsansms', SIZE-25)
                textt = smallfont.render(' Home Page' , True , color)

                smallfont = pygame.font.SysFont('comicsansms', SIZE+10)

                textt1 = smallfont.render('  LEVEL: 1' , True , color)
                textt2 = smallfont.render('  LEVEL: 2' , True , color)
                textt3 = smallfont.render('  LEVEL: 3' , True , color)
                textt4 = smallfont.render('  LEVEL: 4' , True , color)
                textt5 = smallfont.render('  LEVEL: 5' , True , color)
                textt6 = smallfont.render('  LEVEL: 6' , True , color)
                textt7 = smallfont.render('  LEVEL: 7' , True , color)
                textt8 = smallfont.render('  LEVEL: 8' , True , color)

                mouse = pygame.mouse.get_pos()

                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit() 

                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                            running=False
                            page6=False
                            page1=True
                            self.run()
                            
                        if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 100+102:
                            TIME=1
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1
                        
                        if 855 <= mouse[0] <= 855 +370 and 100 <= mouse[1] <= 100+102:
                            TIME=.5
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1
                        
                        if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 250+102:
                            TIME=.25
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1

                        if 855 <= mouse[0] <= 855 +370 and 250 <= mouse[1] <= 250+102:
                            TIME=.2
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1

                        if 320 <= mouse[0] <= 320 +370 and 400 <= mouse[1] <= 400+102:
                            TIME=.1
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1

                        if 855 <= mouse[0] <= 855 +370 and 400 <= mouse[1] <= 400+102:
                            TIME=.05
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1

                        if 320 <= mouse[0] <= 320 +370 and 550 <= mouse[1] <= 550+102:
                            TIME=.025
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1
                        
                        if 855 <= mouse[0] <= 855 +370 and 550 <= mouse[1] <= 550+102:
                            TIME=.02
                            running=False
                            page6=False
                            page2=True
                            LEVEL=1

                    if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                        pygame.draw.rect(self.surface,color_light,[1300, 30, 215, 60])  
                    else:
                        pygame.draw.rect(self.surface,color_dark,[1300, 30, 215, 60])
                    self.surface.blit(textt, (1300, 30))

                    if 320 <= mouse[0] <= 320 +370 and 100 <= mouse[1] <= 100+102:
                        pygame.draw.rect(self.surface,color_light,[320, 100, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 100, 370, 102])
                    self.surface.blit(textt1, (320, 100))

                    if 855 <= mouse[0] <= 855 +370 and 100 <= mouse[1] <= 100+102:
                        pygame.draw.rect(self.surface,color_light,[855, 100, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 100, 370, 102])
                    self.surface.blit(textt2, (855, 100))

                    if 320 <= mouse[0] <= 320 +370 and 250 <= mouse[1] <= 250+102:
                        pygame.draw.rect(self.surface,color_light,[320, 250, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 250, 370, 102])
                    self.surface.blit(textt3, (320, 250))

                    if 855 <= mouse[0] <= 855 +370 and 250 <= mouse[1] <= 250+102:
                        pygame.draw.rect(self.surface,color_light,[855, 250, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 250, 370, 102])
                    self.surface.blit(textt4, (855, 250))

                    if 320 <= mouse[0] <= 320 +370 and 400 <= mouse[1] <= 400+102:
                        pygame.draw.rect(self.surface,color_light,[320, 400, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 400, 370, 102])
                    self.surface.blit(textt5, (320, 400))

                    if 855 <= mouse[0] <= 855 +370 and 400 <= mouse[1] <= 400+102:
                        pygame.draw.rect(self.surface,color_light,[855, 400, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 400, 370, 102])
                    self.surface.blit(textt6, (855, 400))

                    if 320 <= mouse[0] <= 320 +370 and 550 <= mouse[1] <= 550+102:
                        pygame.draw.rect(self.surface,color_light,[320, 550, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[320, 550, 370, 102])
                    self.surface.blit(textt7, (320, 550))

                    if 855 <= mouse[0] <= 855 +370 and 550 <= mouse[1] <= 550+102:
                        pygame.draw.rect(self.surface,color_light,[855, 550, 370, 102])
                    else:
                        pygame.draw.rect(self.surface,color_dark,[855, 550, 370, 102])
                    self.surface.blit(textt8, (855, 550))

                    pygame.display.update()
                    pygame.display.flip()


        if page2:
            running=True

            if LEVEL==0:
                self.reset(0)

            if LEVEL==1:
                self.reset(1)

            while running:
                if LEVEL==1 and self.snake.length-1==ROUND*10:
                    self.reset(2)
                    LEVEL=2

                if LEVEL==2 and self.snake.length-1==ROUND*10:
                    self.reset(3)
                    LEVEL=3
                    
                if LEVEL==3 and self.snake.length-1==ROUND*10:
                    self.reset(4)
                    LEVEL=4
                        
                if LEVEL==4 and self.snake.length-1==ROUND*10:
                    self.reset(5)
                    LEVEL=5
                
                if LEVEL==5 and self.snake.length-1==ROUND*10:
                    self.reset(6)
                    LEVEL=6
                    
                if LEVEL==6 and self.snake.length-1==ROUND*10:
                    self.reset(1)
                    LEVEL=1
                    EXTRA+=int(60*(1/TIME))
                    ROUND+=1

                for i in pygame.event.get():
                    if i.type==KEYDOWN:

                        if i.key==K_UP or i.key==K_KP2:
                            self.snake.move_up()

                        if i.key==K_DOWN or i.key==K_KP_PERIOD:
                            self.snake.move_down()

                        if i.key==K_LEFT or i.key==K_KP0:
                            self.snake.move_left()

                        if i.key==K_RIGHT or i.key==K_KP_ENTER:
                            self.snake.move_right()
                            
                    if i.type == pygame.QUIT:
                        pygame.quit() 

                    mouse = pygame.mouse.get_pos()

                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if 1293 <= mouse[0] <= 1293 + 225 and 60 <= mouse[1] <= 60 + 65:
                            running=False
                            page2=False
                            page4=True
                        
                        if 1370 <= mouse[0] <= 1370 +70 and 510 <= mouse[1] <= 510 + 70:
                            self.snake.move_up()

                        if 1370 <= mouse[0] <= 1370 +70 and 670 <= mouse[1] <= 670 + 70:
                            self.snake.move_down()

                        if 1450 <= mouse[0] <= 1450 +70 and 590 <= mouse[1] <= 590 +70:
                            self.snake.move_right()

                        if 1295 <= mouse[0] <= 1295 +70 and 590 <= mouse[1] <= 590 + 70:                                      
                            self.snake.move_left()

                    
                    if (i.type == pygame.MOUSEBUTTONDOWN and (1375 <= mouse[0] <= 1375 + 60 and 595 <= mouse[1] <= 595 + 60)) or (i.type==KEYDOWN and i.key==K_SPACE):
                        pygame.mixer.music.pause()
                        running=False
                        page2=False
                        page5=True
                
                try:
                    self.play(LEVEL, TIME, ROUND, EXTRA)
                    time.sleep(TIME)

                    mouse = pygame.mouse.get_pos()

                    pygame.display.update()
                    pygame.display.flip()

                except Exception as e:
                    self.play_sound('crash')
                    page8=True

                    if page8:
                        running2=True
                        pygame.mixer.music.pause()

                        while running2:
                            mouse = pygame.mouse.get_pos()

                            for i in pygame.event.get():
                                if i.type == pygame.QUIT:
                                    pygame.quit()

                                if i.type == pygame.MOUSEBUTTONDOWN:
                                    if  0 <= mouse[0] <= 0 +1538 and 0 <= mouse[1] <= 0+800:
                                        running2=False
                                        running=False
                                        page2=False
                                        page8=False
                                        page4=True

                                if i.type==KEYDOWN:
                                    running2=False
                                    running=False
                                    page2=False
                                    page8=False
                                    page4=True
                                    
                    
                                pygame.display.update()
                                pygame.display.flip()

        
        if page3:
            self.show_high_score()
            running=True
            while running:

                color = (0, 0, 0)
                color_light = (51, 51, 56)
                color_dark = (0, 171, 240)
                width = self.surface.get_width()
                height = self.surface.get_height()

                smallfont = pygame.font.SysFont('comicsansms', SIZE-25)
                text = smallfont.render(' Home Page' , True , color)

                mouse = pygame.mouse.get_pos()

                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit() 

                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                            running=False
                            page3=False
                            page1=True
                            self.run()

                    if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                        pygame.draw.rect(self.surface,color_light,[1300, 30, 215, 60])  
                    else:
                        pygame.draw.rect(self.surface,color_dark,[1300, 30, 215, 60])
                    self.surface.blit(text, (1300, 30))

                    pygame.display.update()
                    pygame.display.flip()

        
        if page5:
            running2=True
            while running2:

                for j in pygame.event.get():
                    if j.type == pygame.QUIT:
                        pygame.quit()

                    mouse = pygame.mouse.get_pos()

                    if j.type == pygame.MOUSEBUTTONDOWN and ((1260-260) <= mouse[0] <= (1260-260) +200 and 30 <= mouse[1] <= 30+45):
                        pygame.mixer.music.unpause()
                        running2=False
                        page5=False
                        page4=True

                    if (j.type==KEYDOWN and (j.key==K_UP or j.key==K_KP2)) or  (j.type == pygame.MOUSEBUTTONDOWN and 1370 <= mouse[0] <= 1370 +70 and 510 <= mouse[1] <= 510 + 70):
                        pygame.mixer.music.unpause()
                        page5=False
                        page2=True
                        self.snake.move_up()

                    if (j.type==KEYDOWN and (j.key==K_DOWN or j.key==K_KP_PERIOD)) or (j.type == pygame.MOUSEBUTTONDOWN and 1370 <= mouse[0] <= 1370 +70 and 670 <= mouse[1] <= 670 + 70):
                        pygame.mixer.music.unpause()
                        page5=False
                        page2=True
                        self.snake.move_down()

                    if (j.type==KEYDOWN and (j.key==K_LEFT or j.key==K_KP0)) or  (j.type == pygame.MOUSEBUTTONDOWN and 1295 <= mouse[0] <= 1295 +70 and 590 <= mouse[1] <= 590 + 70):
                        pygame.mixer.music.unpause()
                        page5=False
                        page2=True
                        self.snake.move_left()

                    if (j.type==KEYDOWN and (j.key==K_RIGHT or j.key==K_KP_ENTER)) or (j.type == pygame.MOUSEBUTTONDOWN and 1450 <= mouse[0] <= 1450 +70 and 590 <= mouse[1] <= 590 +70):
                        pygame.mixer.music.unpause()
                        page5=False
                        page2=True
                        self.snake.move_right()

                    if (j.type == pygame.MOUSEBUTTONDOWN and (1375 <= mouse[0] <= 1375 + 60 and 595 <= mouse[1] <= 595 + 60)) or (j.type==KEYDOWN and j.key==K_SPACE):
                        pygame.mixer.music.unpause()
                        page5=False
                        page2=True

                    if page2:
                        running=True
                        while running:     

                            if LEVEL==1 and self.snake.length-1==ROUND*10:
                                self.reset(2)
                                LEVEL=2

                            if LEVEL==2 and self.snake.length-1==ROUND*10:
                                self.reset(3)
                                LEVEL=3
                                
                            if LEVEL==3 and self.snake.length-1==ROUND*10:
                                self.reset(4)
                                LEVEL=4
                                    
                            if LEVEL==4 and self.snake.length-1==ROUND*10:
                                self.reset(5)
                                LEVEL=5
                            
                            if LEVEL==5 and self.snake.length-1==ROUND*10:
                                self.reset(6)
                                LEVEL=6
                                
                            if LEVEL==6 and self.snake.length-1==ROUND*10:
                                self.reset(1)
                                LEVEL=1
                                EXTRA+=int(60*(1/TIME))
                                ROUND+=1
                                
                            for i in pygame.event.get():
                                if i.type==KEYDOWN:

                                    if i.key==K_UP or i.key==K_KP2:
                                        self.snake.move_up()

                                    if i.key==K_DOWN or i.key==K_KP_PERIOD:
                                        self.snake.move_down()

                                    if i.key==K_LEFT or i.key==K_KP0:
                                        self.snake.move_left()

                                    if i.key==K_RIGHT or i.key==K_KP_ENTER:
                                        self.snake.move_right()

                                if i.type == pygame.QUIT:
                                    pygame.quit()

                                mouse = pygame.mouse.get_pos()

                                if i.type == pygame.MOUSEBUTTONDOWN:

                                    if 1293 <= mouse[0] <= 1293 + 225 and 60 <= mouse[1] <= 60 + 65:
                                        running=False
                                        running2=False
                                        page2=False
                                        page5=False
                                        page4=True        

                                    if 1370 <= mouse[0] <= 1370 +70 and 510 <= mouse[1] <= 510 + 70:
                                        self.snake.move_up()

                                    if 1370 <= mouse[0] <= 1370 +70 and 670 <= mouse[1] <= 670 + 70:
                                        self.snake.move_down()

                                    if 1450 <= mouse[0] <= 1450 +70 and 590 <= mouse[1] <= 590 +70:
                                        self.snake.move_right()

                                    if 1295 <= mouse[0] <= 1295 +70 and 590 <= mouse[1] <= 590 + 70:                                      
                                        self.snake.move_left()

                                if (i.type == pygame.MOUSEBUTTONDOWN and (1375 <= mouse[0] <= 1375 + 60 and 595 <= mouse[1] <= 595 + 60)) or (i.type==KEYDOWN and i.key==K_SPACE):
                                    pygame.mixer.music.pause()
                                    running=False
                                    page2=False
                                
                            try:
                                self.play(LEVEL, TIME, ROUND, EXTRA)
                                time.sleep(TIME)

                                mouse = pygame.mouse.get_pos()

                                pygame.display.update()
                                pygame.display.flip()

                            except Exception as e:
                                self.play_sound('crash')
                                page8=True

                                if page8:
                                    running3=True
                                    pygame.mixer.music.pause()

                                    while running3:
                                        mouse = pygame.mouse.get_pos()

                                        for i in pygame.event.get():
                                            if i.type == pygame.QUIT:
                                                pygame.quit()

                                            if i.type == pygame.MOUSEBUTTONDOWN:

                                                if  0 <= mouse[0] <= 0 +1538 and 0 <= mouse[1] <= 0+800:
                                                    running=False
                                                    running2=False
                                                    running3=False
                                                    page2=False
                                                    page5=False
                                                    page8=False
                                                    page4=True

                                            if i.type==KEYDOWN:
                                                running=False
                                                running2=False
                                                running3=False
                                                page2=False
                                                page5=False
                                                page8=False
                                                page4=True                                                  
                                
                                            pygame.display.update()
                                            pygame.display.flip()

    
        if page4:
            running=True
            pygame.mixer.music.pause()

            if LEVEL==0:
                self.show_game_over('Resourses\\classic_high_score.txt', 0, TIME, ROUND, EXTRA)

            else:
                self.show_game_over('Resourses\\campaign_high_score.txt', int((LEVEL-1)*(10/TIME)), TIME, ROUND, EXTRA)
                            
            self.reset(LEVEL)

            while running:

                color = (144, 0, 0)
                color_light = (51, 51, 56)
                color_dark = (0, 0, 0)
                width = self.surface.get_width()
                height = self.surface.get_height()
                
                smallfont = pygame.font.SysFont('comicsansms', SIZE-25)
                text = smallfont.render(' Home Page' , True , color)

                mouse = pygame.mouse.get_pos()

                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit()

                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                            pygame.mixer.music.unpause()
                            running=False
                            page3=False
                            page1=True
                            self.run()

                    if  1300 <= mouse[0] <= 1300 +215 and 30 <= mouse[1] <= 30+60:
                        pygame.draw.rect(self.surface,color_light,[1300, 30, 215, 60])  
                    else:
                        pygame.draw.rect(self.surface,color_dark,[1300, 30, 215, 60])
                    self.surface.blit(text, (1300, 30))

                    pygame.display.update()
                    pygame.display.flip()
        
        
if __name__=='__main__':

    pygame.display.set_caption('SnaCaKe- A Snake and Cake Game')
    
    Icon=pygame.image.load('Resourses\\SnaCaKeImage.png')
    pygame.display.set_icon(Icon)

    game=Game()
    game.run()