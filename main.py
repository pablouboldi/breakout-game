import time
from tkinter import *
from turtle import Screen
from paddle import Paddle
from ball import Ball
from texts import Scoreboard, Lives, GameOver

HEIGHT = 600
WIDTH = 800
bricks = []


def btn_pressed():
    global amnt_bricks
    amnt_bricks = int(radio_state.get())
    root.destroy()


def main():
    screen = Screen()
    screen.setup(height=HEIGHT, width=WIDTH)
    screen.bgcolor("black")
    screen.title("Breakout Game")
    screen.tracer(0)

    # Append bricks
    for i in range(amnt_bricks):
        for j in range(int(amnt_bricks / 5)):
            bricks.append(Paddle((-300 + (150 * i), 70 + (80 * j))))

    paddle = Paddle((0, -250))
    ball = Ball()
    score = Scoreboard()
    lives = Lives()
    game_over = GameOver()

    screen.listen()
    screen.onkeypress(paddle.move_right, "Right")
    screen.onkeypress(paddle.move_left, "Left")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with wall
        if ball.xcor() > 380 or ball.xcor() < -380:
            # Bounce
            ball.bounce_x()
        elif ball.ycor() > 280:
            ball.bounce_y()

        # Detect collision with bricks
        for i in range(len(bricks)):
            if ball.distance(bricks[i]) < 54 and (bricks[i].ycor() + 10 > ball.ycor() > bricks[i].ycor() - 10):
                ball.bounce_y()
                bricks[i].hideturtle()
                bricks[i] = (800, 600)  # This is so disgusting lol.
                score.score_up()
                score.update_scoreboard()

        # Detect collision with paddle.
        if ball.distance(paddle) < 54 and -220 > ball.ycor() > -250:
            # Bounce
            ball.bounce_y()

        # Detect if the paddle misses
        if ball.ycor() < -280:
            ball.miss()
            lives.live_down()
            lives.update_lives()
            if lives.lives == 0:
                game_is_on = False
                game_over.show_text()
            time.sleep(1)

        screen.update()

    screen.exitonclick()


root = Tk()
root.title("Amount of bricks")
root.geometry('350x150+800+300')
root.config(padx=10, pady=5)

# Label
label = Label(root, text='Choose the amount of bricks you want')
label.pack()

# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="5", value=5, variable=radio_state)
radiobutton2 = Radiobutton(text="10", value=10, variable=radio_state)
radiobutton3 = Radiobutton(text="15", value=15, variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# Button
btn = Button(root, text='Accept', command=btn_pressed)
btn.pack(pady=10)

root.mainloop()

main()
