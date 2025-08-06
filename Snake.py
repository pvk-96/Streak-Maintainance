# --- Snake game ---
# --- made by pvk-96 ---
# --- Changes are encouraged ---
import curses
import random

def main(stdscr):
    # Setup
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.timeout(100)
    win.keypad(True)

    # Initial snake and food
    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    # Initial settings
    key = curses.KEY_RIGHT
    score = 0

    while True:
        win.border(0)
        win.addstr(0, 2, f'Score: {score} ')
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Calculate new head
        head = snake[0]
        if key == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]
        elif key == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif key == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif key == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        else:
            continue

        snake.insert(0, new_head)

        # Check game over
        if (new_head in snake[1:] or
            new_head[0] in [0, sh-1] or
            new_head[1] in [0, sw-1]):
            msg = f'Game Over! Final Score: {score}'
            win.addstr(sh//2, sw//2 - len(msg)//2, msg)
            win.refresh()
            curses.napms(2000)
            break

        # Eat food
        if new_head == food:
            score += 1
            food = None
            while food is None or food in snake:
                food = [random.randint(1, sh-2), random.randint(1, sw-2)]
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(new_head[0], new_head[1], curses.ACS_CKBOARD)

curses.wrapper(main)
