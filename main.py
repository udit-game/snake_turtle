from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score_board

#set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)# line 21
screen.bgcolor("black")
screen.title("SNAKE GAMEE!")
#---------------------------------------------------------


#problem 1: create a snake body and move in snake.py
snake = Snake()
food = Food()
score = Score_board()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()


i = 1
snake.create_snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.renew(i)
        i += 1

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -307 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.Game_over()
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 15:
            game_is_on = False
            score.Game_over()


screen.exitonclick()