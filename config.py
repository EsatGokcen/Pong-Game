
#Collision

def wall_collision(ball, height, width):
    if ball.y < 0 or ball.y > height - ball.radius * 2: #bounce of ceiling / floor
        ball.bounce()
    if ball.x < 0 or ball.x > width - ball.radius * 2: #bounce of sides
        ball.bounce()

def player_collision(ball, player_1, player_2):
    if ball.x < player_1.x + player_1.width and ball.x > player_1.x:
        if ball.y < player_1.y + player_1.height and ball.y > player_1.y:
            ball.bounce()
    if ball.x < player_2.x + player_2.width and ball.x > player_2.x:
        if ball.y < player_2.y + player_2.height and ball.y > player_2.y:
            ball.bounce()

# Score 

def score_count(ball, width):
    if ball.x - ball.radius <= 0:  # Right player scores
        return 'right'
    elif ball.x + ball.radius >= width:  # Left player scores
        return 'left'
    return None