def check_collision(bird, pipes, screen_height, ground_height):
    if bird.y - 12 <= 0 or bird.y + 12 >= screen_height - ground_height:
        return True

    for pipe in pipes:
        if bird.x + 12 > pipe.x and bird.x - 12 < pipe.x + pipe.width:
            if bird.y - 12 < pipe.height or bird.y + 12 > pipe.height + pipe.gap:
                return True
    return False
