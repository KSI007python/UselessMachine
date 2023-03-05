import pygame
import math
import random

screen = pygame.display.set_mode((1400, 700))

running = True

def increment_angle(angle, rate):
    angle += rate
    if angle > 2*math.pi:
        angle -= 2*math.pi
    if angle < 0:
        angle += 2*math.pi
    return angle

class vector_line:

    def __init__(self, pos, length, angle, color, angular_velocity):
        self.pos = pos
        self.length = length
        self.angle = angle
        self.color = color
        self.angular_velocity = angular_velocity

    def show(self, move_state):
        pygame.draw.circle(screen, self.color, (self.pos[0] + 700, self.pos[1]), self.length,2)
        pygame.draw.line(screen, self.color, self.pos, (self.pos[0]+self.length*math.cos(self.angle), self.pos[1]+self.length*math.sin(self.angle)))
        if move_state == 1:
            self.angle = increment_angle(self.angle, self.angular_velocity)
        elif move_state == -1:
            self.angle = increment_angle(self.angle, -self.angular_velocity)

length = 70

line_array1 = [vector_line((350, 350), length, 0, (255, 255, 255), 0.005)]

line_array2 = [vector_line((350, 350), length, math.pi, (255, 255, 255), 0.005)]

line_array3 = [vector_line((350, 350), length, math.pi/2, (255, 255, 255), 0.005)]

line_array4 = [vector_line((350, 350), length, 3*math.pi/2, (255, 255, 255), 0.005)]

nline = 10

a = 0.005
for i in range(nline):
    a += 0.003
    x = line_array1[i-1].pos[0] + line_array1[i-1].length*math.cos(line_array1[i-1].angle)
    y = line_array1[i-1].pos[1] + line_array1[i-1].length*math.sin(line_array1[i-1].angle)
    length *= 0.8
    line_array1.append(vector_line([x, y], length, 0, random.choice([(255, 255, 255)]), a))

a = 0.005
length = 70
for i in range(nline):
    a += 0.003
    x = line_array2[i-1].pos[0] - line_array2[i-1].length*math.cos(line_array2[i-1].angle)
    y = line_array2[i-1].pos[1] - line_array2[i-1].length*math.sin(line_array2[i-1].angle)
    length *= 0.8
    line_array2.append(vector_line([x, y], length, math.pi, random.choice([(255, 255, 255)]), a))

a = 0.005
length = 70
for i in range(nline):
    a += 0.003
    x = line_array3[i-1].pos[0] - line_array3[i-1].length*math.cos(line_array2[i-1].angle)
    y = line_array3[i-1].pos[1] - line_array3[i-1].length*math.sin(line_array2[i-1].angle)
    length *= 0.8
    line_array3.append(vector_line([x, y], length, math.pi/2, random.choice([(255, 255, 255)]), a))

a = 0.005
length = 70
for i in range(nline):
    a += 0.003
    x = line_array4[i-1].pos[0] - line_array4[i-1].length*math.cos(line_array4[i-1].angle)
    y = line_array4[i-1].pos[1] - line_array4[i-1].length*math.sin(line_array4[i-1].angle)
    length *= 0.8
    line_array4.append(vector_line([x, y], length, 3*math.pi/2, random.choice([(255, 255, 255)]), a))

while running:

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    for i in line_array1:
        if keys[pygame.K_a]:
            i.show(1)
        if keys[pygame.K_d]:
            i.show(-1)
        else:
            i.show(0)
    for i in line_array2:
        if keys[pygame.K_a]:
            i.show(1)
        if keys[pygame.K_d]:
            i.show(-1)
        else:
            i.show(0)
    for i in line_array3:
        if keys[pygame.K_a]:
            i.show(1)
        if keys[pygame.K_d]:
            i.show(-1)
        else:
            i.show(0)

    for i in line_array4:
        if keys[pygame.K_a]:
            i.show(1)
        if keys[pygame.K_d]:
            i.show(-1)
        else:
            i.show(0)

    for i in range(1, nline+1):
        line_array1[i].pos[0] = line_array1[i-1].pos[0] + line_array1[i-1].length*math.cos(line_array1[i-1].angle)
        line_array1[i].pos[1] = line_array1[i-1].pos[1] + line_array1[i-1].length*math.sin(line_array1[i-1].angle)

    for i in range(1, nline+1):
        line_array2[i].pos[0] = line_array2[i-1].pos[0] + line_array2[i-1].length*math.cos(line_array2[i-1].angle)
        line_array2[i].pos[1] = line_array2[i-1].pos[1] + line_array2[i-1].length*math.sin(line_array2[i-1].angle)

    for i in range(1, nline+1):
        line_array3[i].pos[0] = line_array3[i-1].pos[0] + line_array3[i-1].length*math.cos(line_array3[i-1].angle)
        line_array3[i].pos[1] = line_array3[i-1].pos[1] + line_array3[i-1].length*math.sin(line_array3[i-1].angle)

    for i in range(1, nline+1):
        line_array4[i].pos[0] = line_array4[i-1].pos[0] + line_array4[i-1].length*math.cos(line_array4[i-1].angle)
        line_array4[i].pos[1] = line_array4[i-1].pos[1] + line_array4[i-1].length*math.sin(line_array4[i-1].angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()