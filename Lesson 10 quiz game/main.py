import pgzrun

WIDTH = 870
HEIGHT = 650

TITLE = "QUIZ MASTER"

marquee_box = Rect(0, 0, 880, 80)
question_box = Rect(0, 0, 650, 150)

timer_box = Rect(0, 0, 150, 150)
skip_box = Rect(0, 0, 150, 330)

answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)

marquee_box.move_ip(0, 0)
question_box.move_ip(20, 100)

timer_box.move_ip(700, 100)
skip_box.move_ip(700, 270)

answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)

score = 0
time_left = 10
is_game_over = False
question_file_name = "questions.txt"

marquee_message = ""

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

questions = []
question_count = 0
question_index = 0

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")

    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(timer_box,"red")
    screen.draw.filled_rect(skip_box,"light blue")
    screen.draw.filled_rect(question_box,"dark blue")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"grey")

    marquee_message=f"Welcome to Quiz Master... Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message,marquee_box,color = "white")
    screen.draw.textbox(str(time_left),timer_box,color = "white")
    screen.draw.textbox("SKIP",skip_box,color = "white")
    screen.draw.textbox(question[0].strip(),question_box,color = "white")

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color = "black")
        index = index + 1






































question = ["Question....","ans1","ans2","ans3","ans4","1"]
pgzrun.go()