from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

game_txt = "D:\\Visual_Studio_Code_Project\\shortcut\\game.txt"
web_txt = "D:\\Visual_Studio_Code_Project\\shortcut\\web.txt"
driver_loction = "D:\\Visual_Studio_Code_Project\\shortcut\\chromedriver.exe"

def web_open_game():
    option = Options()
    option.add_argument('--no-sandbox')
    option.add_argument("--incognito")              #無痕模式
    option.add_experimental_option("detach", True)  #不自動關閉
    driver = webdriver.Chrome(driver_loction, chrome_options=option)     
    driver.get("https://" + text_Value_Pg1.get())
    shortcut_list_Pg1.delete(0, END)

def web_open_pics():
    option = Options()
    option.add_argument('--no-sandbox')
    option.add_argument("--incognito")              #無痕模式
    option.add_experimental_option("detach", True)  #不自動關閉
    driver = webdriver.Chrome(driver_loction, chrome_options=option)
    driver.get("https://" + text_Value_Pg2.get())
    shortcut_list_Pg2.delete(0, END)
    
def shortcut_list_Pg1_add():                        #新增快速導覽
    game_list.append(text_Value_Pg1.get())
    with open(game_txt, "a") as game_data:        #新增加入網址
        game_data.write("\n" + text_Value_Pg1.get())
    shortcut_list_Pg1["value"] = game_list
    messagebox.showinfo("ADD", "新增" + text_Value_Pg1.get())
    
def shortcut_list_Pg2_add():                        #新增快速導覽
    web_list.append(text_Value_Pg2.get())
    with open(web_txt, "a") as web_data:          #新增加入網址
        web_data.write("\n" + text_Value_Pg2.get())
    shortcut_list_Pg2["value"] = web_list
    messagebox.showinfo("ADD", "新增" + text_Value_Pg2.get())

#讀取game資料
def read_game_data():
    with open(game_txt, "r") as game_data:
        for data in game_data:
            game_list.append(data)
    shortcut_list_Pg1["value"] = game_list
#讀取web資料
def read_web_data():
    with open(web_txt, "r") as web_data:
        for data in web_data:
            web_list.append(data)
    shortcut_list_Pg2["value"] = web_list


windows = Tk()
windows.title("Shortcut")
windows.iconphoto(True, PhotoImage(file="D:\\Visual_Studio_Code_Project\\shortcut\\go.png"))

# style = ttk.Style()
# style.configure("BW.TLabel", background="lightyellow")

# title = ttk.Label(windows, style="BW.TLabel", text="自訂工具")
# title.grid(row=0, column=1, pady=3)

#最上層框架
top_area = Notebook(windows)

text_Value_Pg1 = StringVar()    #Game 
text_Value_Pg2 = StringVar()    #Porn pics

add_icon = PhotoImage(file="D:\\Visual_Studio_Code_Project\\shortcut\\add.png")
go_icon = PhotoImage(file="D:\\Visual_Studio_Code_Project\\shortcut\\go.png")

game_list = []
web_list = []

shortcut_Pg1 = Frame(top_area, width=300)
shortcut_list_Pg1 = Combobox(shortcut_Pg1, textvariable=text_Value_Pg1, width=30)
read_game_data()    #讀取資料
shortcut_list_Pg1.grid(row=0, column=1, pady=5)
add_list_Pg1 = Button(shortcut_Pg1, image=add_icon, width=2, command=shortcut_list_Pg1_add)
add_list_Pg1.grid(row=0, column=2, sticky=W)
game_btn = Button(shortcut_Pg1, image=go_icon, command=web_open_game)
game_btn.grid(row=1, column=2, pady=3)

shortcut_Pg2 = Frame(top_area, width=300)
shortcut_list_Pg2 = Combobox(shortcut_Pg2, textvariable=text_Value_Pg2, width=30)
read_web_data()     #讀取資料
shortcut_list_Pg2["value"] = web_list
shortcut_list_Pg2.grid(row=0, column=1, pady=5)
add_list_Pg2 = Button(shortcut_Pg2, image=add_icon, width=2, command=shortcut_list_Pg2_add)
add_list_Pg2.grid(row=0, column=2, sticky=W)
pics_btn = Button(shortcut_Pg2, image=go_icon, command=web_open_pics)
pics_btn.grid(row=1, column=2, pady=3)

top_area.add(shortcut_Pg1, text="Game")
top_area.add(shortcut_Pg2, text="Pics")
top_area.grid(row=1, column=1, padx=3, pady=3)


windows.mainloop()
