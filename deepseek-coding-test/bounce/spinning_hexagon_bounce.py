import pygame
import math

# 初始化Pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("旋转六边形弹球")

# 物理参数
GRAVITY = 500       # 重力加速度 (像素/秒²)
FRICTION = 0.99     # 摩擦力系数
ELASTICITY = 0.8    # 碰撞弹性系数
ROT_SPEED = 1.5     # 六边形旋转速度 (弧度/秒)

class Ball:
    def __init__(self, x, y, radius):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.radius = radius
        self.color = (255, 0, 0)
    
    def update(self, dt):
        # 应用重力和摩擦力
        self.vel.y += GRAVITY * dt
        self.vel *= FRICTION
        self.pos += self.vel * dt

class SpinningHexagon:
    def __init__(self, center, radius):
        self.center = pygame.Vector2(center)
        self.radius = radius
        self.rotation = 0.0
        self.color = (0, 255, 0)
        self.vertices = []
    
    def update(self, dt):
        # 更新旋转角度
        self.rotation += ROT_SPEED * dt
        self.rotation %= 2 * math.pi
        
        # 计算顶点位置
        self.vertices = []
        for i in range(6):
            angle = self.rotation + i * math.pi / 3
            x = self.center.x + self.radius * math.cos(angle)
            y = self.center.y + self.radius * math.sin(angle)
            self.vertices.append(pygame.Vector2(x, y))
    
    def draw(self, surface):
        if len(self.vertices) == 6:
            pygame.draw.polygon(surface, self.color, self.vertices, 2)

def check_collision(ball, hexagon):
    for i in range(6):
        # 获取当前边
        start = hexagon.vertices[i]
        end = hexagon.vertices[(i+1)%6]
        
        # 计算边向量和法向量
        edge = end - start
        normal = pygame.Vector2(-edge.y, edge.x).normalize()
        
        # 计算球到边的向量
        ball_to_edge = ball.pos - start
        
        # 投影到边向量上
        t = ball_to_edge.dot(edge) / edge.length_squared()
        t = max(0, min(1, t))
        closest = start + t * edge
        
        # 计算距离和穿透向量
        distance_vec = ball.pos - closest
        distance = distance_vec.length()
        
        if distance < ball.radius:
            # 计算相对速度
            rel_vel = ball.vel
            
            # 只在球进入多边形时处理碰撞
            if distance_vec.dot(normal) < 0:
                normal = -normal
            
            # 计算冲量
            j = -(1 + ELASTICITY) * rel_vel.dot(normal)
            ball.vel += j * normal
            
            # 修正位置防止穿透
            penetration = ball.radius - distance
            ball.pos += normal * penetration * 1.1

def main():
    clock = pygame.time.Clock()
    running = True
    
    hexagon = SpinningHexagon((WIDTH//2, HEIGHT//2), 250)
    ball = Ball(WIDTH//2, HEIGHT//2 - 150, 15)
    
    while running:
        dt = clock.tick(60) / 1000.0
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 更新物体状态
        hexagon.update(dt)
        ball.update(dt)
        
        # 碰撞检测与响应
        check_collision(ball, hexagon)
        
        # 绘制场景
        screen.fill((0, 0, 0))
        hexagon.draw(screen)
        pygame.draw.circle(screen, ball.color, (int(ball.pos.x), int(ball.pos.y)), ball.radius)
        
        pygame.display.flip()

if __name__ == "__main__":
    main() 