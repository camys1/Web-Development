from flask import Flask
import random 

NUMBER = random.randint(0, 9)
app = Flask(__name__)

wrong_gifs = ["https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnRqejQ2NjUzZDFwY3I1eHdtcmhqYWl2MWlyb3g3M2Q2eWtzY3JxdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8HqjtoyKrnfJC/giphy.gif","https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjM0NnF1bXo4YmpscmVwMDY2ZXY3dXVmcHNsOXY1NHN4d202aHY3NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fLyfhjZr9g47fTJMuk/giphy.gif","https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTlwNzAyM2F2MG9rbWNqa3NnNzFrazJjb2Jsa25uZmd3MXgwM2ZyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6QxXEiJnnwOQPRnl0I/giphy.gif","https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGUycnA0MXFuM2E1YTRwaHJlNjJzd2N6dmFrZzdsMW1ycTZiN3NnMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4OJFCEeGzYGs0/giphy.gif","https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG16dDAya2MzZWV3MnNpenc0NnB1cjB4MHZ1dzYza3NodmhpbTlpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/42BtVfS6BxcHgIT59m/giphy.gif","https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzExNGN5NXVkenU5bWF6ejg0NXU1bW91bTBqeWk4bjcyM3Q5OGV3cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WsvZrQTJsJAyZ3hMhD/giphy.gif","https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWdwamJsY2JyOGd0Mnp2Y2w3bmV2ZmdqdjliOGVyb3d4bXBpd2d4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wV2LWS2IPouNWSj1on/giphy.gif","https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmZscjBnYXlncnZzbjZjZTJudm0xNjJ3MXkzNW43eWE5dTNiMXRzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UYc7jllncK2UOpqdjF/giphy.gif","https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmVkbjQ5OGR4bWo3ODRyeXh1OGc2ajBucGM0ejhsZmE1cWxqd2JtMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QfYDVV2XkUM8Y0npbf/giphy.gif","https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExenBlZHVoMHdjbHJmeHhveHFrMDl0bWg5djVicHptNG1uNDk0cDg1NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ss6v1kUqSKiHYdcktp/giphy.gif"]
correct_gifs = ['https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTU4eWw2ZGo0dnhob3c3cTc2M2VmeHE2cXZpN2xuN290MG51am1rNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.gif',"https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif?cid=790b7611ndhehwo26brhh7ubr6ck47d6c5ykrdst2f6gnhi6&ep=v1_gifs_search&rid=giphy.gif&ct=g",'https://media.giphy.com/media/gffcSKwGREETNo9rsy/giphy.gif?cid=790b7611ndhehwo26brhh7ubr6ck47d6c5ykrdst2f6gnhi6&ep=v1_gifs_search&rid=giphy.gif&ct=g','https://media.giphy.com/media/l0MYy7QpDDVGVfAAw/giphy.gif?cid=790b7611ndhehwo26brhh7ubr6ck47d6c5ykrdst2f6gnhi6&ep=v1_gifs_search&rid=giphy.gif&ct=g','https://media.giphy.com/media/1hMk0bfsSrG32Nhd5K/giphy.gif?cid=790b7611ndhehwo26brhh7ubr6ck47d6c5ykrdst2f6gnhi6&ep=v1_gifs_search&rid=giphy.gif&ct=g','https://media.giphy.com/media/26FPnsRww5DbqoPuM/giphy.gif?cid=790b7611ndhehwo26brhh7ubr6ck47d6c5ykrdst2f6gnhi6&ep=v1_gifs_search&rid=giphy.gif&ct=g','https://media.giphy.com/media/uVpPvvpU3nip5pBkPD/giphy.gif?cid=ecf05e470jvrqqqrfp1uqmointahjc8e6m0v971oq3iafaa2&ep=v1_gifs_search&rid=giphy.gif&ct=g','https://media.giphy.com/media/6CqtwRdMYcUsU/giphy.gif?cid=ecf05e470jvrqqqrfp1uqmointahjc8e6m0v971oq3iafaa2&ep=v1_gifs_search&rid=giphy.gif&ct=g']


@app.route('/')
def home():
    global NUMBER
    NUMBER = random.randint(0, 9)
    return '<b><h1>Guess a number between 0 and 9.</h1><b>'\
'<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">'

@app.route('/<int:number>')
def check_number(number):
    wrong_gif = random.choice(wrong_gifs)
    correct_gif = random.choice(correct_gifs)
    if number < NUMBER:
        message = f"<h1 style='color: blue;'>Too low!</h1>"\
        f"<img src='{wrong_gif}'>"
    elif number > NUMBER:
        message = f"<h1 style='color: red;'>Too high!</h1>"\
        f"<img src='{wrong_gif}'>"
    else:
        message = f"<h1 style='color: green;'>You found it! {NUMBER}</h1>"\
        f"<img src='{correct_gif}'>"
    
    restart_button = """<br><a href="/" style="text-decoration: none;">
                        <button style="background-color: #4CAF50; color: white; 
                        padding: 10px; border: none; border-radius: 5px;">Play Again</button>
                        </a>"""

    return message + restart_button


if __name__ == "__main__":
    app.run(debug=True)
