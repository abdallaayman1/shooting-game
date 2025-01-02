import pygame

pygame.init()
bg = pygame.image.load("bg.jpg")
hero = pygame.image.load("hero.jpg")
screen = pygame.display.set_mode((889, 500))
pygame.display.set_caption("abzo's game")
clock = pygame.time.Clock()
move_right = [pygame.image.load("hero.jpg")]
move_left = [pygame.image.load("heroL.jpg")]
move_lefte = [pygame.image.load("enemy.png")]
move_righte = [pygame.image.load("enemyR.png")]
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,100,0)
score = 0
font_style = pygame.font.SysFont("bahnschrift", 35)


class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.moves = 0
        self.step = 7
        self.isJumping = False
        self.jump = 10
        self.pose = True
        self.hitbox = (self.x,self.y,58,88)



    def draw(self, screen):
        global moves
        for bullet in bullets:
            bullet.draw(screen)
        if not abzo.pose:
            if abzo.left:
                screen.blit(move_left[0], (abzo.x, abzo.y))
                abzo.moves += 1
                if abzo.moves == 1:
                    abzo.moves = 0
            elif abzo.right:
                screen.blit(move_right[0], (abzo.x, abzo.y))
                abzo.moves += 1
                if abzo.moves == 1:
                    abzo.moves = 0
        else:
            if abzo.right:
                screen.blit(move_right[0], (abzo.x, abzo.y))
            else:
                screen.blit(move_left[0], (abzo.x, abzo.y))
        self.hitbox = (self.x,self.y,58,88)
    
    def hit(self):
        self.isJumping=False
        self.jump=10
        self.x = self.start_x
        self.y = self.start_y
        self.moves = 0
        font1 =pygame.font.SysFont("comicsans" , 80)
        text = font1.render("-5",1,RED)
        screen.blit(text, (889//2 -1 , 500//2))
        pygame.display.update()
        i = 0
        while i < 150:
            i+=1
            pygame.time.delay(10)
            for events in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
        Enemy.height = 50
        Enemy.width = 50
        Enemy.end =889
        Enemy.x = 700
        Enemy.y = 390
        Enemy.visible = True


class enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = 0
        self.step = 3
        self.moves = 0
        self.hitbox = (self.x,self.y,67,100)
        self.health = 120
        self.visible = True


    def message(self):    
        font = pygame.font.SysFont("comicsans", 40, True)
        text = font.render("Congrats , You killed the monster", True, RED)
        screen.blit(text, (889 // 7, 500 // 5))
        
    
    def message2(self):
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render("Press Q-Quit or A-Play Again", True, RED)
        screen.blit(text, (889 // 4, 500 // 2))
        
        
    def draw(self, screen):
        if self.visible:
            self.move()
            if self.step < 0:
                screen.blit(move_lefte[0], (self.x, self.y))
                self.moves += 1
                if self.moves == 1:
                    self.moves = 0
            else:
                screen.blit(move_righte[0], (self.x, self.y))
                self.moves += 1
                if self.moves == 1:
                    self.moves = 0
            self.hitbox = (self.x,self.y,67,100)
            pygame.draw.rect(screen,RED,(self.hitbox[0],self.hitbox[1],60,10))
            pygame.draw.rect(screen,GREEN,(self.hitbox[0],self.hitbox[1],self.health/2,10))
        else :
            self.message()
            self.message2() 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:  # Press 'C' to continue
                # Reset game state here if needed
                        pass
                    elif event.key == pygame.K_q:  # Press 'Q' to quit
                        pygame.quit()
                        quit()       
            
        
    
    
    
    def hit(self):
        self.health-=1
        if self.health <= 0:
            self.visible=False
            self.hitbox=(0,0,0,0)


    def move(self):
        if self.step > 0:
            if self.x + self.step + self.width >= self.end:
               self.step *= -1
            else:
                self.x += self.step
        else:
            if self.x - self.step <= self.start:
                self.step *= -1
            else:
                self.x += self.step



class bullet:
    def __init__(self, x, y, radius, color, direction, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = direction
        self.color = color
        self.speed = speed * direction



    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)




abzo = player(0, 400, 50, 50)
Enemy = enemy(700,390,50,50,889)
bullets = []
font = pygame.font.SysFont("comicsans",35,True)


def drawgame():
    global moves
    text = font.render("Score : " + str(score),True,BLACK)
    screen.blit(bg,(0,0))
    screen.blit(text , (650,25))
    Enemy.draw(screen)
    abzo.draw(screen)    
    for Bullet in bullets:
        Bullet.draw(screen)
        
  
is_paused = False
  
  
def draw_pause_screen():
    font = pygame.font.SysFont("comicsans", 70, True)
    text = font.render("Paused", True, RED)
    screen.blit(text, (889 // 3, 500 // 5))  # Display the 'Paused' message
    
    

def message():
    font = pygame.font.SysFont("comicsans", 50, True)
    text = font.render("Press C-Continue or Q-Quit", True, RED)
    screen.blit(text, (889 // 10, 500 // 2))
    
    
while True:
    clock.tick(60)
    if abzo.x + abzo.width >= Enemy.hitbox[0] and abzo.x + abzo.width <= Enemy.hitbox[0] + Enemy.hitbox[2] + Enemy.width:
        if abzo.y + abzo.height >= Enemy.hitbox[1] and abzo.y + abzo.height <= Enemy.hitbox[1] + Enemy.hitbox[3]:
            score -= 5
            abzo.hit()
    
    if is_paused:
        draw_pause_screen()
        message()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # Press 'C' again to resume the game
                    is_paused = False
                elif event.key == pygame.K_q:  # Press 'Q' to quit the game
                    pygame.quit()
                    quit()
    else:
        # Continue with the normal game logic (same as your previous code)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if len(bullets) < 10:
                        direction = 0
                        if abzo.right:
                            direction = 1
                        else:
                            direction = -1
                        bullets.append(
                            bullet(
                                round(abzo.x + abzo.width // 2),
                                round(abzo.y + abzo.height // 2),
                                5,
                                BLACK,
                                direction,
                                10,
                            )
                        )
                elif event.key == pygame.K_p:  
                    if Enemy.visible:
                        # Press 'P' to pause the game
                        is_paused = True  # Toggle pause state
                elif event.key == pygame.K_q:  # Press 'Q' to quit the game
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_a:  # Press 'A' to restart the game
                    score = 0
                    abzo.x = abzo.start_x
                    abzo.y = abzo.start_y
                    abzo.isJumping = False
                    abzo.jump = 10
                    abzo.moves = 0
                    Enemy.height = 50
                    Enemy.width = 50
                    Enemy.end =889
                    Enemy.x = 700
                    Enemy.y = 390
                    Enemy.visible = True
                    Enemy.health = 120
                    bullets.clear()
                    abzo.pose = True
                    break  # Break out of the event loop to restart the game

        keys = pygame.key.get_pressed()
        for Bullet in bullets:
            if Bullet.x >= Enemy.hitbox[0] and Bullet.x <= Enemy.hitbox[0] + Enemy.hitbox[2]:
                if Bullet.y >= Enemy.hitbox[1] and Bullet.y <= Enemy.hitbox[1] + Enemy.hitbox[3]:
                    bullets.remove(Bullet)
                    Enemy.hit()
                    score += 1
            if Bullet.x < 889 and Bullet.x > 0:
                Bullet.x += Bullet.speed
            else:
                bullets.remove(Bullet)

        if keys[pygame.K_LEFT] and abzo.x - abzo.step >= 0:
            abzo.x -= abzo.step
            abzo.left = True
            abzo.right = False
            abzo.pose = False
        elif keys[pygame.K_RIGHT] and abzo.x + abzo.step + abzo.width <= 889:
            abzo.x += abzo.step
            abzo.right = True
            abzo.left = False
            abzo.pose = False
        else:
            abzo.pose = True
            abzo.moves = 0

        if not abzo.isJumping:
            if keys[pygame.K_SPACE]:
                abzo.isJumping = True
        else:
            if abzo.jump >= -10:
                neg = 1
                if abzo.jump < 0:
                    neg = -1
                abzo.y -= (abzo.jump**2) * 0.25 * neg
                abzo.jump -= 1
            else:
                abzo.jump = 10
                abzo.isJumping = False
        
        drawgame()  # Draw the game screen as usual
        pygame.display.update()