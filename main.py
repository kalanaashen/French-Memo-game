from tkinter import *
from words import *
import pandas
#-----words to learn________#

'''data_2=pandas.read_csv("words_to_learn.csv")
words_to_learn=data_2.to_dict(orient="records")'''

#------french words------------#

data_1 = pandas.read_csv("french_words.csv")
French_words = data_1.to_dict(orient="records")


postion=""
new_data={
    "French":[],
    "English":[]
}

#------common function--------------#
def algo1(): #words in french
    global choice, time_pause
    choice = random.choice(French_words)
    window.after_cancel(time_pause)
    french_choice = choice["French"]
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(text_1, text="French", fill="black")
    canvas.itemconfig(text_2, text=french_choice, fill="black")
    time_pause = window.after(3000, english_word)

'''def algo2(): #words to learn function
    global choice, time_pause
    choice = random.choice(words_to_learn)
    window.after_cancel(time_pause)
    french_choice = choice["French"]
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(text_1, text="French", fill="black")
    canvas.itemconfig(text_2, text=french_choice,fill="black")
    time_pause = window.after(3000, english_word)'''




#-------front card side---------#
def right_b():
    global choice, time_pause
    try:
        data_2 = pandas.read_csv("words_to_learn.csv")
        words_to_learn = data_2.to_dict(orient="records")
        choice = random.choice(words_to_learn)
        window.after_cancel(time_pause)
        french_choice = choice["French"]
        print("learn part working right")
        canvas.itemconfig(canvas_image, image=old_image)
        canvas.itemconfig(text_1, text="French", fill="black")
        canvas.itemconfig(text_2, text=french_choice, fill="black")
        time_pause = window.after(3000, english_word)
        print("hutto")
        words_to_learn.remove(choice)
        df2= pandas.DataFrame(words_to_learn)
        df2.to_csv("words_to_learn.csv", index=False)
    except:
        algo1()
        print("this is word list ")
        French_words.remove(choice)
        df1 = pandas.DataFrame(French_words)
        df1.to_csv("french_words.csv", index=False)

def wrong_b():
    global choice, time_pause
    try:
        data_2 = pandas.read_csv("words_to_learn.csv")
        words_to_learn = data_2.to_dict(orient="records")
        print("learn part working wrong part")

        choice = random.choice(words_to_learn)
        window.after_cancel(time_pause)
        french_choice = choice["French"]
        canvas.itemconfig(canvas_image, image=old_image)
        canvas.itemconfig(text_1, text="French", fill="black")
        canvas.itemconfig(text_2, text=french_choice, fill="black")
        time_pause = window.after(3000, english_word)

    except:
        algo1()
    new_data["French"].append(choice["French"])
    new_data["English"].append(choice["English"])
    df = pandas.DataFrame(new_data)
    print(df)
    df.to_csv("words_to_learn.csv", index=False)


#---------adding to a dictonray------#


#----deleting from the words--------#


def english_word():
    global choice
    english_choice = choice["English"]
    canvas.itemconfig(text_1, text="English", fill="white")
    canvas.itemconfig(text_2, text=english_choice, fill="white")
    canvas.itemconfig(canvas_image,image=new_image)







#-----------------------app interface---------------------------#
window = Tk()
window.title("Flash Card App")
window.config( padx=50, pady=50,bg="#B1DDC6")
canvas = Canvas(highlightthickness=0,width=800,height=526,bg="#B1DDC6")

time_pause=window.after(3000,english_word)

old_image = PhotoImage(file="card_front.png")
new_image= PhotoImage(file="card_back.png")
canvas_image=canvas.create_image(400, 263, image=old_image)
text_1 = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 50, "italic"))
text_2 = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0,columnspan=2)
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=1,command=right_b)
right_button.grid(row=1,column=0)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=1, command=wrong_b)
wrong_button.grid(row=1,column=1)


algo1()

window.mainloop()
