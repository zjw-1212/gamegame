import pygame
import os
import random
from pygame.locals import *
from sys import exit

# 定义 Icon 类
class Icon:
    def __init__(self, *image_paths):
        self.images = []
        for path in image_paths:
            # 构建完整的文件路径
            full_path = os.path.join('images', path)  # 确保路径正确
            if os.path.exists(full_path):
                self.images.append(pygame.image.load(full_path))
            else:
                print(f"File not found: {full_path}")
        self.rects = [img.get_rect() for img in self.images]
        self.rects = [rect.move(0, 0) for rect in self.rects]  # 重置rect的位置

# 定义 Point 类
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 游戏开始界面
def intro(screen, font):
    intro_image_path = 'images\\tile5.jpg'
    intro_image = pygame.image.load(intro_image_path)
    intro_image = pygame.transform.scale(intro_image, (400, 760))
    screen.blit(intro_image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if 150 < x < 250 and 400 < y < 450:  # 假设这是开始游戏按钮的位置
                    return "start"
                elif 150 < x < 250 and 450 < y < 500:  # 假设这是商店按钮的位置
                    return "store"

        draw_buttons(screen, font)
        pygame.display.update()

# 绘制按钮
def draw_buttons(screen, font):
    start_game_rect = pygame.Rect(150, 400, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), start_game_rect)
    text = font.render('Start Game', True, (0, 0, 0))
    text_rect = text.get_rect(center=start_game_rect.center)
    screen.blit(text, text_rect)

    store_rect = pygame.Rect(150, 450, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), store_rect)
    text = font.render('Store', True, (0, 0, 0))
    text_rect = text.get_rect(center=store_rect.center)
    screen.blit(text, text_rect)

# 商店界面
def store(screen, font):
    store_image_path = 'images\\win.jpg'
    store_image = pygame.image.load(store_image_path)
    store_image = pygame.transform.scale(store_image, (400, 760))
    screen.blit(store_image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if 150 < x < 250 and 400 < y < 450:  # 假设这是购买额外时间按钮的位置
                    return "buy_time"
                elif 150 < x < 250 and 450 < y < 500:  # 假设这是返回主菜单按钮的位置
                    return "main_menu"

        draw_store_buttons(screen, font)
        pygame.display.update()

# 绘制商店按钮
def draw_store_buttons(screen, font):
    buy_time_rect = pygame.Rect(150, 400, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), buy_time_rect)
    text = font.render('Buy Time', True, (0, 0, 0))
    text_rect = text.get_rect(center=buy_time_rect.center)
    screen.blit(text, text_rect)

    return_menu_rect = pygame.Rect(150, 450, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), return_menu_rect)
    text = font.render('Return', True, (0, 0, 0))
    text_rect = text.get_rect(center=return_menu_rect.center)
    screen.blit(text, text_rect)

# 游戏结束界面
def game_over(screen, font):
    game_over_image_path = 'images\\game_over.jpg'
    game_over_image = pygame.image.load(game_over_image_path)
    game_over_image = pygame.transform.scale(game_over_image, (400, 760))
    screen.blit(game_over_image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if 150 < x < 250 and 400 < y < 450:  # 假设这是重新开始按钮的位置
                    return "restart"
                elif 150 < x < 250 and 450 < y < 500:  # 假设这是退出按钮的位置
                    pygame.quit()
                    exit()

        draw_game_over_buttons(screen, font)
        pygame.display.update()

# 绘制游戏结束按钮
def draw_game_over_buttons(screen, font):
    restart_rect = pygame.Rect(150, 400, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), restart_rect)
    text = font.render('Restart', True, (0, 0, 0))
    text_rect = text.get_rect(center=restart_rect.center)
    screen.blit(text, text_rect)

    quit_rect = pygame.Rect(150, 450, 100, 50)
    pygame.draw.rect(screen, (255, 255, 255), quit_rect)
    text = font.render('Quit', True, (0, 0, 0))
    text_rect = text.get_rect(center=quit_rect.center)
    screen.blit(text, text_rect)
# 主函数
def main():
    pygame.init()
    windows_width = 400
    windows_height = 760
    icoSize = 48
    whiteColor = (255, 255, 255)
    fpsClock = pygame.time.Clock()
    playSurface = pygame.display.set_mode((windows_width, windows_height))
    pygame.display.set_caption("Sheep Game")
    defaultFont = pygame.font.get_default_font()
    font = pygame.font.SysFont(defaultFont, 24)

    # 加载图标
    icons = Icon(
        'tile1.jpg', 'tile2.jpg', 'tile3.jpg', 'tile4.jpg', 'tile5.jpg',
        'tile6.jpg', 'tile7.jpg', 'tile8.jpg', 'tile9.jpg', '1.jpg',
        '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg',
        '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg',
        '12.jpg', '13.jpg', 'game_over.jpg', 'win.jpg', 'tile10.jpg'
    )
    for i in range(len(icons.images)):
        icons.images[i] = pygame.transform.scale(icons.images[i], (icoSize, icoSize))

    # 游戏开始界面
    choice = intro(playSurface, font)
    if choice == "store":
        store_choice = store(playSurface, font)
        if store_choice == "buy_time":
            # 这里可以添加购买额外时间的逻辑
            print("Time purchased")
        elif store_choice == "main_menu":
            main()  # 重新开始主函数
    elif choice == "start":
        # 游戏逻辑
        data = [[0 for i in range(5)] for j in range(5)]  # 修改为5x5的网格
        dropped_icons = []  # 存储下落的图案
        appearances = {i: 0 for i in range(1, 26)}  # 更新范围以包括25个图标

        # 初始化图案
        for r in range(5):
            for c in range(5):
                data[r][c] = random.randint(1, 25)  # 假设有25个图标
                appearances[data[r][c]] += 1

        score = 0
        countdown = 60  # 倒计时时间，单位秒
        startTime = pygame.time.get_ticks()

        offsetX = (windows_width - (4 * (icoSize + 10) + 48)) / 2
        offsetY = (windows_height - (4 * (icoSize + 10) + 48)) / 2

        while True:
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - startTime) // 1000
            remaining_time = countdown - time_elapsed
            if remaining_time < 0:
                game_over_result = game_over(playSurface, font)
                if game_over_result == "restart":
                    main()  # 重启主函数以重新开始游戏
                break

            pygame.display.update()
            playSurface.fill(whiteColor)
            
            color = (255, 0, 0)
            s = "Mission: " + str(len(appearances) - 4)
            text = font.render(s, True, color)
            playSurface.blit(text, (5, 45))
 
            color = (0, 255, 0)
            text = font.render("Score: " + str(score), True, color)
            playSurface.blit(text, (5, 65))

            text = font.render("Time: " + str(remaining_time), True, (0, 0, 255))
            playSurface.blit(text, (5, 85))

            for r in range(5):
                for c in range(5):
                    if data[r][c]:
                        playSurface.blit(icons.images[data[r][c] - 1], (offsetX + c * (icoSize + 10), offsetY + r * (icoSize + 10)))
        
            for i in range(len(dropped_icons)):
                if dropped_icons[i]:
                    playSurface.blit(icons.images[dropped_icons[i] - 1], (26 + i * 50, 620))

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    for r in range(5):
                        for c in range(5):
                            x1 = offsetX + c * (icoSize + 10)
                            y1 = offsetY + r * (icoSize + 10)
                            if x > x1 and x < x1 + icoSize and y > y1 and y < y1 + icoSize:
                                if data[r][c] != 0:
                                    dropped_icons.append(data[r][c])
                                    data[r][c] = 0
                                    # 检查是否有三个相同的图案可以消除
                                    if dropped_icons.count(dropped_icons[-1]) >= 3:
                                        for j in range(len(dropped_icons) - 1, -1, -1):
                                            if dropped_icons[j] == dropped_icons[-1]:
                                                dropped_icons.pop(j)
                                                score += 1
                                    # 将下方图案上移
                                    for layer in range(r, 4):
                                        if data[layer + 1][c] == 0:
                                            data[layer][c] = data[layer + 1][c]
                                            data[layer + 1][c] = 0
                                    break

            if len(dropped_icons) >= 8:
                game_over_result = game_over(playSurface, font)
                if game_over_result == "restart":
                    main()  # 重启主函数以重新开始游戏
                break

            fpsClock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()