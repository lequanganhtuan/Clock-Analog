import pygame
import math
import time

# Khởi tạo màn hình
pygame.init()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Đồng hồ kim")

clock_radius = 150
hour_hand_length = 80
minute_hand_length = 120
second_hand_length = 140

clock_center = (screen_width // 2, screen_height // 2)

# Hình ảnh background cho các giai đoạn khác nhau trong ngày
morning_image = pygame.image.load("morning.png")
noon_image = pygame.image.load("noon.png")
evening_image = pygame.image.load("evening.png")
night_image = pygame.image.load("night.png")

# Khởi tạo giá trị ban đầu cho current_time
current_time = time.localtime()

# Hàm vẽ đồng hồ và background
def draw_clock():
    current_hour = current_time.tm_hour

    # Chọn hình ảnh background tương ứng với giai đoạn của ngày
    if 6 <= current_hour < 12:
        background_image = morning_image
    elif 12 <= current_hour < 18:
        background_image = noon_image
    elif 18 <= current_hour < 24:
        background_image = evening_image
    else:
        background_image = night_image

    # Vẽ background
    screen.blit(background_image, (0, 0))

    # Vẽ đồng hồ
    pygame.draw.circle(screen, (0, 0, 0), clock_center, clock_radius, 2)

    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = int(clock_center[0] + (clock_radius - 20) * math.cos(angle))
        y = int(clock_center[1] + (clock_radius - 20) * math.sin(angle))
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)

    # Vẽ kim giờ
    hour_angle = math.radians((current_time.tm_hour % 12) * 30 - 90)
    hour_hand_x = int(clock_center[0] + hour_hand_length * math.cos(hour_angle))
    hour_hand_y = int(clock_center[1] + hour_hand_length * math.sin(hour_angle))
    pygame.draw.line(screen, (255, 0, 0), clock_center, (hour_hand_x, hour_hand_y), 8)

    # Vẽ kim phút
    minute_angle = math.radians(current_time.tm_min * 6 - 90)
    minute_hand_x = int(clock_center[0] + minute_hand_length * math.cos(minute_angle))
    minute_hand_y = int(clock_center[1] + minute_hand_length * math.sin(minute_angle))
    pygame.draw.line(screen, (0, 0, 255), clock_center, (minute_hand_x, minute_hand_y), 4)

    # Vẽ kim giây
    second_angle = math.radians(current_time.tm_sec * 6 - 90)
    second_hand_x = int(clock_center[0] + second_hand_length * math.cos(second_angle))
    second_hand_y = int(clock_center[1] + second_hand_length * math.sin(second_angle))
    pygame.draw.line(screen, (0, 255, 0), clock_center, (second_hand_x, second_hand_y), 2)

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Cập nhật kích thước màn hình và các giá trị liên quan đến đồng hồ
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screen_width, screen_height = event.w, event.h
            clock_center = (screen_width // 2, screen_height // 2)
            clock_radius = min(screen_width // 2, screen_height // 2) - 10
            hour_hand_length = clock_radius * 0.5
            minute_hand_length = clock_radius * 0.75
            second_hand_length = clock_radius * 0.9

    # Cập nhật thời gian hiện tại
    current_time = time.localtime()

    draw_clock()
    pygame.display.flip()
    pygame.time.delay(100)

# Kết thúc chương trình
pygame.quit()
