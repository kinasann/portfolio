import tkinter
import pyperclip , os
from tkinter import colorchooser

scr_file = os.path.abspath(__file__) 
os.chdir(os.path.dirname(scr_file))

def btn_click(btn_ev):
    global menu_btn , size
    menu_btn = btn_ev.widget.cget("text")
    if win_close == 1:
        win.destroy()
    if menu_btn == "ウインドウ作成":
        size ="1000x600+145+53"
        entry_win_size.delete(0,tkinter.END)
        display()
        window_size()
    elif menu_btn == "色":
        colorcheck()
    elif menu_btn == "ヘルプ" :
        left_help()
    elif menu_btn != "閉じる" :
        a = entry_place.get()
        if a != "":
            b = a.replace("x"," ")
            c = b.replace("+"," ")
            win_list = c.split(" ")
            if len(win_list) == 2:
                win_list.append("145")
                win_list.append("53")
            elif len(win_list) ==3:
                win_list[2]= "145"
                win_list.append("53")
            elif len(win_list) == 4:
                pass
            else:
                win_list = ["1000","600","100","80"]
                
            if menu_btn == "縦軸(x)":
                tate = int(win_list[3])-num_y_line_h
                win_list[3] = str(tate)
            elif menu_btn == "横軸(y)":
                yoko = int(win_list[2])-num_x_line_h
                win_list[2] = str(yoko)
            else:
                tate = int(win_list[3])-num_y_line_h
                win_list[3] = str(tate)
                yoko = int(win_list[2])-num_x_line_h
                win_list[2] = str(yoko)
            size = ",".join(win_list)
            size = size.replace(",","x",1)
            size = size.replace(",","+")
        else: size ="1000x600+145+53"
        display()
        left_place()

def display():
    """左ウインドウの作成"""
    global win
    win = tkinter.Toplevel()
    win.focus_set() 
    global win_close
    win_close = win.winfo_exists()
    win.geometry(size)
    global frame
    win.maxsize(width=MW, height=MH)
    frame = tkinter.Frame(win,width=MW,height=MH, bg="#ffffaa")
    frame.pack(fill="both") 
    

def window_size():
    """ウインドウ作成"""
    win.title("tkinter tool  --- geometry   ウインドウ作成   横幅 x 縦幅 + 左横から位置 + 上から位置 ")
    global size , gazou
    size = win.geometry()
    gazou = tkinter.PhotoImage(file="geometry.png")
    gazou = gazou.subsample(1)
    label_geo = tkinter.Label(frame,image=gazou, bg="#ffffaa",height=MH)
    label_geo.pack(fill="both",ipady=30)
    
   
def  get_geometry():
    """ウインドウ作成取得"""
    if win_close == 1:
        size = win.geometry()
        if len(entry_win_size.get()) > 1:
            entry_win_size.delete(0,tkinter.END)
        entry_win_size.insert(0, size)


def colorcheck():
    if win_close == 1:
        win.destroy()
    color = colorchooser.askcolor()
    
    if color != (None, None):
        if len(entry_cord.get()) > 1:
            entry_cord.delete(0,tkinter.END)

        global color_rgb , color_cord
        color_cord = color[1]
        entry_cord.insert(0,color_cord)
        btn_color.config(state=tkinter.NORMAL)
        label_color = tkinter.Label(frame_color, font=("MSゴシック","25"), 
                                    anchor=tkinter.N, text="■", fg=color_cord)
        label_color.grid(row = 0, column = 3)


def size_copy():
    """ウインドウの大きさをコピー"""
    pyperclip.copy(entry_win_size.get())
        
def cord_copy():
    """ウインドウの大きさをコピー"""
    pyperclip.copy(entry_cord.get())    

def key_down(e):
    global key, line
    key = e.keysym
    if key == "space":
        line.config(bg="#f9f9f9")


def key_up(e):
    global key, line
    key == ""
    line.config(bg="snow")                  


def left_place():
    """place配置"""

    win.wm_attributes("-transparentcolor", "snow")      # 透過処理

    if menu_btn == "縦軸(x)" or menu_btn == "横軸(y)" or menu_btn ==  "方眼(x,y)":
        win.title("tkinter tool  --- placeルーラー   \
            単位：10  緑線：50単位  赤線：100単位 (太線：1000)  大きさ変更時はスペースキーを押しながらドラッグ推奨")
    global key
    key = ""
    win.bind("<KeyPress>", key_down)
    win.bind("<KeyRelease>", key_up)    
    
    #* 数字の作成
    for i in range(1000):
        pl = i *10 
        if i % 10 == 0 : 
            if pl != 0:
                num = tkinter.Label(frame,text=pl, bg="#ffffaa")
                if menu_btn == "縦軸(x)" :
                    num.place(x=pl-10)

                elif menu_btn == "横軸(y)" :
                    num.place(y=pl-10 )
                elif menu_btn ==  "方眼(x,y)" :
                    num.place(y=pl+10)
                    num2 = tkinter.Label(frame,text=pl, bg="#ffffaa")
                    num2.place(x=pl+10)    
    global line                
    line = tkinter.Canvas(win, width=MW , height=MH, bg="snow")
 
    
    if menu_btn == "縦軸(x)":
        line.place(y=num_y_line_h )
    elif menu_btn == "横軸(y)":
        line.place(x=num_x_line_h)
    else:
        line.place(x=num_x_line_h, y=num_y_line_h)    
        
    for i in range(1000):
        pl = i *10 
        w = 1  
        if i% 10 == 0: 
            c = "#ff0000"
            if i% 100 == 0:
                w = 3
        elif i% 5 == 0:
            c = "green"
        else: 
            c = "#0000ff"
        if menu_btn == "縦軸(x)":
            line.create_line( pl, 0, pl, MH , fill=c, width=w)
        elif menu_btn == "横軸(y)":
            line.create_line( 0, pl, MW ,pl, fill=c, width=w) 
        else:
            line.create_line( pl, 0, pl, MH , fill=c, width=w)
            line.create_line( 0, pl, MW ,pl, fill=c, width=w) 

win_close = 0   # 左ウインドウがあるか
win_size = 0    # サイズ確認ウインドウがあるか
num_x_line_h = 22     # place 配置  数字 の 横の列 の高さ
num_y_line_h = 21     # place 配置  数字 の 縦の列 の高さ

#* help
def left_help():
    global size
    size ="1000x640+145+30"
    display()
    win.title("tkinter tool  --- ヘルプ  使い方説明")
    win.resizable(False,False)
    
    
    help_dict = {" ★閉じる★ " : ["tkinter toolで開いた左側のウインドウを閉じることが可能"],
    " ★ウインドウ作成★ " : ["左側に新しいウインドウを作成  ドラッグすることで大きさや位置を変更可能",
        "確認ボタン → ウインドウサイズや位置をテキストボックスに表示(placeルーラーも可能)", \
        "コピーボタン → テキストボックス内全てをコピー(範囲指定不可)"] ,
    " ★place位置★ " : ["初期サイズ(テキストラン未記入)：「1000x600+145+53」", 
                     "確認したいウインドウサイズをテキストボックスに記入すると、ウインドウサイズに端を合わせたplaceルーラーが表示", 
                     "ドラッグしてウインドウ移動、サイズ変更(スペース押しながら推奨)可能",
                     "確認がしやすいよう透過処理をしているため、動かす際は色がついている部分をクリック",
                     "スペースキーを押すことでルーラーの背景色に変化するため、大きさ変更がしやすくなる",
                     "１目盛10単位 緑線→50単位 赤線→100単位(太線1000", 
                     "※ 以下の場合、初期値の「1000x600+145+53」に変更", " ・「500x100-5+10」など「-」の値がある　  \
                    ・「fghjk」など規定以外の数値", "※ 「600x100」など位置を判定する数値がなかった場合",
                     " →初期値の「+100+80」位置で表示"],                         
    " ★「ウインドウ作成」機能と「place位置」機能の合わせ技★ " : 
        ["place位置ウインドウを好きな大きさにして、geometry欄の確認ボタンを押すと", "place位置ウインドウサイズがテキストボックスへ "],
    " ★color★ " : ["「色」ボタンを押すと、カラーチェッカーを呼び出します。", "使いたい色を選択して、OK を押すと、テキストボックスに代入"]
    }

    for k,l in help_dict.items():
        geo_help_frame = tkinter.LabelFrame(frame, text=k, bg="#ffffaa",font=(2) ,width=200 ,height=MH)
        geo_help_frame.pack(pady=5, padx=10, ipady=3, ipadx=10, anchor=tkinter.W, fill="both")
        for v in range(len(l)):
            geo_help_text = tkinter.Label(geo_help_frame,text=l[v],bg="#ffffaa", justify="left")
            geo_help_text.pack(anchor=tkinter.W, pady=2)     
       
#* メニュー
menu = tkinter.Tk()
menu.title("tkinter Tool menu")
menu.resizable(0, 0)    # 最大化非表示
menu.geometry("150x680-0+20")

MW = menu.winfo_screenwidth()  # 左ウインドウ フレームの最大値(横)
MH = menu.winfo_screenheight()    # 左ウインドウ フレームの最大値(縦)

#* 閉じる
frame_close = tkinter.LabelFrame(menu, text= "左ウインドウを")
frame_close.pack(pady=5)

close_btn = tkinter.Button(frame_close, text= "閉じる", width=10, height=2)
close_btn.pack(pady=5, padx=5)
close_btn.bind("<ButtonPress>", btn_click)

#* win_size_btn
frame_win_size = tkinter.LabelFrame(menu, text= "geometry")
frame_win_size.pack(pady=5)

btn_win_size = tkinter.Button(frame_win_size, text= "ウインドウ作成", width=10)
btn_win_size.pack(pady=5, padx=5)
btn_win_size.bind("<ButtonPress>", btn_click)
label_win_size = tkinter.Label(frame_win_size, text="現在の左ウインドウのサイズ")
label_win_size.pack(pady=5, padx=5)
entry_win_size = tkinter.Entry(frame_win_size,width=20)
entry_win_size.insert(0, "")
entry_win_size.pack(padx=5)

size_btn = tkinter.Button(frame_win_size, text="確認",command=get_geometry)
size_btn.pack(side = tkinter.LEFT, pady=10, padx=(15,10))
entry_win_copy = tkinter.Button(frame_win_size, text="コピー", command=size_copy)
entry_win_copy.pack(side = tkinter.RIGHT, pady=10, padx=(10,15))


#* place Btn
btn_list = ["縦軸(x)", "横軸(y)", "方眼(x,y)"]
size = "1000x600+100+80"

frame_place = tkinter.LabelFrame(menu, width=10, text= "place配置")
frame_place.pack(pady=5)

label_place = tkinter.Label(frame_place, text="確認したいウインドウ")
label_place.pack(pady=1)
label_place2 = tkinter.Label(frame_place, text="例：1000x600+100+80\n横幅x縦幅+左から+上から")
label_place2.pack(pady=1)
entry_place  = tkinter.Entry(frame_place,width=18)
entry_place.pack()

for btn_num in btn_list:      #range(len(button_dict)):
        btn = tkinter.Button(frame_place, text=btn_num)
        btn.pack(pady=15, padx=15)
        btn.bind("<ButtonPress>", btn_click)
        
#* color
frame_color = tkinter.LabelFrame(menu, text= "color")
frame_color.pack(pady=5)

btn_color = tkinter.Button(frame_color, text= "色", width=10, state="normal",command=colorcheck)
btn_color.grid(row = 0, column = 0, columnspan=3, pady=5, padx=5)

label_cord = tkinter.Label(frame_color, text="カラーコード")
label_cord.grid(row = 1, column = 0)

entry_cord  = tkinter.Entry(frame_color,width=14)
entry_cord.grid(row = 2, column = 0, columnspan=3, pady=5, padx=5)
entry_cord_copy = tkinter.Button(frame_color, text="コピー", command=cord_copy)
entry_cord_copy.grid(row = 2, column = 3)

#* menu_help
frame_help = tkinter.Frame(menu, width=20)
frame_help.pack(pady=5)

btn_help = tkinter.Button(frame_help, text="ヘルプ", width=10,bg= "#bdbdbd")
btn_help.pack(padx=15)
btn_help.bind("<ButtonPress>", btn_click)
left_help()

tkinter.mainloop()