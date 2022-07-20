# 2afac131fa094f029a64adc6cecceca7
from tkinter import *
import requests
import json

root = Tk()
root.geometry("500x600")
root.overrideredirect(True)

newsupdate = Label(root, text = "BBC News Update", font = ("Helvetica", 20, 'bold'))
newsupdate.place(relx = 0.5, rely = 0.05, anchor = CENTER)

news1 = Label(root, font = ("Times", 15, 'bold') ,wraplength = 500, justify = CENTER)
news1.place(relx = 0.3, rely = 0.15, anchor = CENTER)

news_desc1 = Label(root, font = ("Times", 15), wraplength = 500, justify = CENTER)
news_desc1.place(relx = 0.3, rely = 0.2, anchor = CENTER)

news2 = Label(root, font = ("Times", 15, 'bold') ,wraplength = 500, justify = CENTER)
news2.place(relx = 0.3, rely = 0.3, anchor = CENTER)

news_desc2 = Label(root, font = ("Times", 15), wraplength = 500, justify = CENTER)
news_desc2.place(relx = 0.3, rely = 0.4, anchor = CENTER)

news3 = Label(root, font = ("Times", 15, 'bold') ,wraplength = 500, justify = CENTER)
news3.place(relx = 0.3, rely = 0.5, anchor = CENTER)

news_desc3 = Label(root, font = ("Times", 15), wraplength = 500, justify = CENTER)
news_desc3.place(relx = 0.3, rely = 0.6, anchor = CENTER)

news4 = Label(root, font = ("Times", 15, 'bold') ,wraplength = 500, justify = CENTER)
news4.place(relx = 0.3, rely = 0.7, anchor = CENTER)

news_desc4 = Label(root, font = ("Times", 15), wraplength = 500, justify = CENTER)
news_desc4.place(relx = 0.3, rely = 0.8, anchor = CENTER)

news5 = Label(root, font = ("Times", 15, 'bold') ,wraplength = 500, justify = CENTER)
news5.place(relx = 0.3, rely = 0.9, anchor = CENTER)

news_desc5 = Label(root, font = ("Times", 15), wraplength = 500, justify = CENTER)
news_desc5.place(relx = 0.3, rely = 0.10, anchor = CENTER)

api_request = requests.get(" https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=2afac131fa094f029a64adc6cecceca7")
open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page["articles"][0]["title"]
desc1 = open_bbc_page["articles"][0]["description"]

title2 = open_bbc_page["articles"][1]["title"]
desc2 = open_bbc_page["articles"][1]["description"]

title3 = open_bbc_page["articles"][2]["title"]
desc3 = open_bbc_page["articles"][2]["description"]

title4 = open_bbc_page["articles"][3]["title"]
desc4 = open_bbc_page["articles"][3]["description"]

title5 = open_bbc_page["articles"][4]["title"]
desc5 = open_bbc_page["articles"][4]["description"]

news1['text'] = "Title 1 : " + title1
news_desc1['text'] = "Description : " + desc1

news2['text'] = "Title 2 : " + title2
news_desc2['text'] = "Description : " + desc2

news3['text'] = "Title 3 : " + title3
news_desc3['text'] = "Description : " + desc3

news4['text'] = "Title 4 : " + title4
news_desc4['text'] = "Description : " + desc4

news5['text'] = "Title 5 : " + title5
news_desc5['text'] = "Description : " + desc5

root.mainloop()