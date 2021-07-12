#Must import the package
import pygame
import random
import os

#Make call this line in order for pygame to start running
os.path.abspath("C:\\Users\\gamec\\Desktop\\ECE 150\\Foodwars\\manaspc.ttf")
pygame.init()
screen_width = 600;
screen_height = 800;
#Setting the dimensions of the screen
window = pygame.display.set_mode((screen_width,screen_height))

#Setting the title of the game
pygame.display.set_caption("Foodwars")

#Importing sprites into List
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
chicken = pygame.image.load('chicken.png')
sushi = pygame.image.load('sushi.png')
fries = pygame.image.load('fries.png')
pepper = pygame.image.load('pepper.png')
bg_intro = pygame.image.load('foodwar.png')


#Importing Sound
eatingSound = pygame.mixer.Sound('bitingsound.wav')
eatingSound.set_volume(0)

#Clock
clock = pygame.time.Clock()
white = (255,255,255)
#Player
class Player(object):
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.sprint_speed = 10
        self.sprint = False
        self.walkCount = 0
        self.left = False
        self.right = False
        #self.hitbox = (self.x+20, self.y+11, 20, 30)

    def draw(self,window):
        if (self.walkCount + 1 >= 27):
            self.walkCount = 0
            
        if self.left:
            window.blit(walkLeft[self.walkCount//3], (self.x,self.y) )
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//3], (self.x,self.y) )
            self.walkCount += 1
        else:
            window.blit(char,(self.x,self.y) )
        self.hitbox = (self.x+20, self.y+11, 20, 30)
        #pygame.draw.rect(window, (255,0,0), (self.hitbox),2)
        #print(str(self.x)+","+str(self.hitbox[1]))   
            
class Food(object):
    def __init__(self,x,y,width,height):
        global score
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.num = random.randint(1,3)
        self.hitbox = (self.x+13, self.y+7, 80, 80)
        self.type = ""
        self.food_counter = random.randint(1,20)
        self.other = random.randint(1,20)
        self.pepperx = random.randint(97,504)
    def draw(self,window):
        
            
        if(self.num == 1):
            self.type = "sushi"
            window.blit(chicken, (self.x,self.y) )
                
        elif(self.num == 2):
            self.type = "chicken"
            window.blit(sushi, (self.x,self.y) )
                
        elif(self.num == 3):
            self.type = "fries"
            window.blit(fries, (self.x,self.y) )

            
        if(self.food_counter == self.other):
            self.type = "pepper"
            window.blit(pepper, (self.pepperx,self.y) )

        #self.hitbox = (self.x+13, self.y+7, 80, 80)
        #pygame.draw.rect(window, (255,0,0),self.hitbox,2)
        #print("food:"+str(self.x)+","+str(self.y))
        
    def hit(self,combo_counter):
        add_value = 0
        if (self.type == "sushi"):
            add_value = 100*combo_counter
        elif (self.type == "chicken"):
            add_value = 200*combo_counter
        elif (self.type == "fries"):
            add_value = 300*combo_counter
        elif(self.type == "pepper"):
            game_outro()
            #print("pepper)
        return add_value
    
#Drawing Game
def redrawGameWindow():
    
    window.blit(bg,(0,0))
    guy.draw(window)
    
    #Score
    text = font.render('Score: ' + str(score), 1, (0,0,0) )
    text1 = font.render('Score: ' + str(score), 1, (255,255,255) )
    window.blit(text, (210, 510) )
    window.blit(text1, (208, 508) )

    #COMBO
    combo = font.render('Combo x' + str(combo_counter), 1, (0,0,0) )
    combo1 = font.render('Combo x' + str(combo_counter), 1, (255,255,255) )
    window.blit(combo, (215, 475) )
    window.blit(combo1, (213, 473) )

    for food in food_list:
        food.draw(window)
        
    pygame.display.update()

#Start the Game

def game_intro():
    #Copyright Music lol
    shokugeki = pygame.mixer.music.load('orange.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    #-------------------------------------------------------------------------------#
    intro_font = pygame.font.Font('manaspc.ttf', 60)
    body_font = pygame.font.Font('manaspc.ttf', 30)
    intro_msg2 = body_font.render('Press Any Button To Continue', 1, (0,0,0) )
    intro_msg3 = body_font.render('Press Any Button To Continue', 1, (255,255,255) )
    #-------------------------------------------------------------------------------#

    copy = intro_msg2.copy()
    copy1 = intro_msg3.copy()
        
    alpha = 255
    alpha_surf1 = pygame.Surface(copy1.get_size(), pygame.SRCALPHA)
    alpha_surf = pygame.Surface(copy.get_size(), pygame.SRCALPHA)
    #-------------------------------------------------------------------------------#
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg_intro,(0,0))
        intro_font = pygame.font.Font('manaspc.ttf', 60)
        intro_msg = intro_font.render('Foodwars' , 1, (0,0,0) )
        intro_msg1 = intro_font.render('Foodwars', 1, (255,255,255) )

        
        window.blit(intro_msg, (160, 100) )
        window.blit(intro_msg1, (155, 96) )
        #window.blit(intro_msg2, (28, 750) )
        #window.blit(intro_msg3, (23, 746) )

        #Create Fading Text in and Out

        

        if alpha > 0:
            alpha = max(alpha-4,0)
            alpha_surf.fill((255,255,255, alpha))
            alpha_surf1.fill((255,255,255, alpha))

            copy.blit(alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            copy1.blit(alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        user_press = pygame.key.get_pressed()
        window.blit(copy, (28,750) )
        window.blit(copy1, (23,746) )

        if(event.type == pygame.KEYDOWN):
            break;
        
        pygame.display.update()
        
        clock.tick(10)

def game_outro():
#Copyright Music lol
    shokugeki = pygame.mixer.music.load('orange.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    #-------------------------------------------------------------------------------#
    intro_font = pygame.font.Font('manaspc.ttf', 60)
    body_font = pygame.font.Font('manaspc.ttf', 30)
    intro_msg2 = body_font.render('LOL GG NOOB U SUCK', 1, (0,0,0) )
    intro_msg3 = body_font.render('LOL GG NOOB U SUCK', 1, (255,255,255) )
    #-------------------------------------------------------------------------------#

    copy = intro_msg2.copy()
    copy1 = intro_msg3.copy()
            
    alpha = 255
    alpha_surf1 = pygame.Surface(copy1.get_size(), pygame.SRCALPHA)
    alpha_surf = pygame.Surface(copy.get_size(), pygame.SRCALPHA)
    #-------------------------------------------------------------------------------#
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg_intro,(0,0))
        intro_font = pygame.font.Font('manaspc.ttf', 60)
        #intro_msg = intro_font.render('Foodwars' , 1, (0,0,0) )
        #intro_msg1 = intro_font.render('Foodwars', 1, (255,255,255) )

            
        #window.blit(intro_msg, (160, 100) )
        #window.blit(intro_msg1, (155, 96) )
            #window.blit(intro_msg2, (28, 750) )
            #window.blit(intro_msg3, (23, 746) )

            #Create Fading Text in and Out

            

        if alpha > 0:
            alpha = max(alpha-4,0)
            alpha_surf.fill((255,255,255, alpha))
            alpha_surf1.fill((255,255,255, alpha))

            copy.blit(alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            copy1.blit(alpha_surf, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        user_press = pygame.key.get_pressed()
        window.blit(copy, (28,750) )
        window.blit(copy1, (23,746) )

        if(event.type == pygame.KEYDOWN):
            break;
            
        pygame.display.update()
            
        clock.tick(10)
   
#Main
score = 0
font = pygame.font.Font('manaspc.ttf', 30)
start = pygame.time.get_ticks()
guy = Player(275,725, 64 ,64)
food_list = []
combo_counter = 0
eatingSound.set_volume(0.2)
run = True

game_intro()
copy = pygame.mixer.music.load('omegalul.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
while run:
    #Takes 60 fps
    clock.tick(60)
    now = pygame.time.get_ticks() 
    if now-start>400:
        start = now
        x_food = random.randint(97,504)
        food_char = Food(x_food,1, 96, 96)
        food_list.append(food_char)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    for food in food_list:
        if guy.y-80 < food.y:
            if guy.x - 80 < food.x and food.x < guy.x + 30: 
                food_list.pop(food_list.index(food))
                eatingSound.play()
                combo_counter += 1
                score += food_char.hit(combo_counter)
        if food.y < 800 and food.y > 0:
            food.y += food.vel
        
        else:
            food_list.pop(food_list.index(food))
            #print("hello")
            combo_counter = 0
    user_press = pygame.key.get_pressed()
    
    if(guy.sprint):
        
        if user_press[pygame.K_a] and (guy.x>guy.sprint):
            guy.x -= guy.sprint_speed
            guy.left = True
            guy.right = False
            guy.sprint = False
        elif user_press[pygame.K_d] and (guy.x< screen_width - guy.width - guy.sprint_speed):
            guy.x += guy.sprint_speed
            guy.right = True
            guy.left = False
            guy.sprint = False
        else:
            guy.right = False
            guy.Left = False
            guy.walkCount = 0;
    else:
        
        if user_press[pygame.K_a] and (guy.x>guy.vel):
            guy.x -= guy.vel
            guy.left = True
            guy.right = False
        if user_press[pygame.K_d] and (guy.x< screen_width - guy.width - guy.vel):
            guy.x += guy.vel
            guy.left = False
            guy.right = True
        if user_press[pygame.K_SPACE]:
            guy.sprint = True
        
        
    redrawGameWindow()
    #if user_press[pygame.K_UP] and (char_pos_y>vel):
        #char_pos_y -= vel
    #if user_press[pygame.K_DOWN] and (char_pos_y< screen_height - char_height - vel):
        #char_pos_y += vel
pygame.quit()
