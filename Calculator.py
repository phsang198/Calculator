from tkinter import *
from tkinter.font import Font

# Tạo cửa sổ chính
wd = Tk()
wd.geometry('320x320')
wd.title('Máy tính')
fts = Font(family='Tohoma', size=12)

# Biến toàn cục
drnum = 8
py = 5
bieuthuc = ''
change = True
cursor_pos = 0
history = []  # Lưu lại các phép tính đã thực hiện
current_index = -1  # Chỉ số hiện tại của lịch sử
cursor_blink_id = None

# Thiết lập màn hình hiển thị
mh = Label(wd, bg='#4279A5', fg='#FFFFFF', width=320, height=3, font=fts)
mh.pack(side=TOP)
fr = Frame(wd)
fr.pack()

# Hàm tải lịch sử từ file
def load_history():
    global history, current_index
    try:
        with open('calculations.txt', 'r') as file:
            history = file.readlines()
        history = [entry.strip() for entry in history if entry.strip()]  # Loại bỏ dòng trống và dấu cách
        if history:
            current_index = len(history) - 1
    except FileNotFoundError:
        history = []
        current_index = -1

# Hàm cập nhật hiệu ứng nhấp nháy cho con trỏ
def update_cursor_blink():
    global bieuthuc, cursor_pos,change, cursor_blink_id
    if change :
        cursor_text = bieuthuc[:cursor_pos] + '|' + bieuthuc[cursor_pos:]
        change = False
    else:
        cursor_text = bieuthuc[:cursor_pos] + ''+ bieuthuc[cursor_pos:]
        change = True
    mh.config(text=cursor_text)
    if cursor_blink_id:
        wd.after_cancel(cursor_blink_id)
    cursor_blink_id = wd.after(800, update_cursor_blink)  # Cập nhật sau mỗi 500ms

# Cập nhật màn hình hiển thị
def update_display():
    global bieuthuc, cursor_pos
    display_text = bieuthuc[:cursor_pos] + '|' + bieuthuc[cursor_pos:]
    mh.config(text=display_text)
    update_cursor_blink() 

# Hàm tạo biểu thức dạng chuỗi
def xyly(num):
    global bieuthuc, cursor_pos
    bieuthuc = bieuthuc[:cursor_pos] + str(num) + bieuthuc[cursor_pos:]
    cursor_pos += len(str(num))
    update_display()

# Hàm tính toán
def TinhToan():
    global bieuthuc, history, current_index,cursor_pos
    try:
        ketqua = eval(bieuthuc)
        mh.config(text=ketqua)
        history.append(bieuthuc)
        with open('calculations.txt', 'a') as file:
            file.write(bieuthuc + '\n')
        bieuthuc = str(ketqua)
        current_index = len(history) - 1
        cursor_pos = len(bieuthuc)
    except Exception as e:
        mh.config(text='Error')
        bieuthuc = ''
        cursor_pos = 0

# Hàm xóa biểu thức
def Xoa():
    global bieuthuc, cursor_pos
    bieuthuc = ''
    cursor_pos = 0
    update_display()

# Hàm xóa một ký tự cuối cùng của biểu thức
def DelChar():
    global bieuthuc, cursor_pos
    if cursor_pos > 0:
        bieuthuc = bieuthuc[:cursor_pos-1] + bieuthuc[cursor_pos:]
        cursor_pos -= 1
    update_display()

# Hàm xóa tất cả biểu thức trên màn hình
def ClearAll():
    global bieuthuc, cursor_pos
    bieuthuc = ''
    cursor_pos = 0
    update_display()

# Hàm xóa lịch sử và file
def ClearHistory():
    global history, current_index, bieuthuc, cursor_pos
    history = []
    current_index = -1
    bieuthuc = ''
    cursor_pos = 0
    mh.config(text='')
    with open('calculations.txt', 'w') as file:
        file.write('')

# Hàm hiển thị phép tính trước đó
def Prev():
    global current_index, bieuthuc, cursor_pos
    if current_index > 0:
        current_index -= 1
        bieuthuc = history[current_index]
        cursor_pos = len(bieuthuc)
        update_display()

# Hàm hiển thị phép tính tiếp theo
def Next():
    global current_index, bieuthuc, cursor_pos
    if current_index < len(history) - 1:
        current_index += 1
        bieuthuc = history[current_index]
        cursor_pos = len(bieuthuc)
        update_display()

# Hàm di chuyển con trỏ về bên trái
def MoveLeft():
    global cursor_pos
    if cursor_pos > 0:
        cursor_pos -= 1
    update_display()

# Hàm di chuyển con trỏ về bên phải
def MoveRight():
    global cursor_pos
    if cursor_pos < len(bieuthuc):
        cursor_pos += 1
    update_display()

# Hàng 1
bt7 = Button(fr, text='7', font=fts, width=drnum, pady=py, command=lambda: xyly('7'))
bt7.grid(row=1, column=1)
bt8 = Button(fr, text='8', font=fts, width=drnum, pady=py, command=lambda: xyly('8'))
bt8.grid(row=1, column=2)
bt9 = Button(fr, text='9', font=fts, width=drnum, pady=py, command=lambda: xyly('9'))
bt9.grid(row=1, column=3)
btCong = Button(fr, text='+', font=fts, width=drnum, pady=py, command=lambda: xyly('+'))
btCong.grid(row=1, column=4)

# Hàng 2
bt4 = Button(fr, text='4', font=fts, width=drnum, pady=py, command=lambda: xyly('4'))
bt4.grid(row=2, column=1)
bt5 = Button(fr, text='5', font=fts, width=drnum, pady=py, command=lambda: xyly('5'))
bt5.grid(row=2, column=2)
bt6 = Button(fr, text='6', font=fts, width=drnum, pady=py, command=lambda: xyly('6'))
bt6.grid(row=2, column=3)
btTru = Button(fr, text='-', font=fts, width=drnum, pady=py, command=lambda: xyly('-'))
btTru.grid(row=2, column=4)

# Hàng 3
bt1 = Button(fr, text='1', font=fts, width=drnum, pady=py, command=lambda: xyly('1'))
bt1.grid(row=3, column=1)
bt2 = Button(fr, text='2', font=fts, width=drnum, pady=py, command=lambda: xyly('2'))
bt2.grid(row=3, column=2)
bt3 = Button(fr, text='3', font=fts, width=drnum, pady=py, command=lambda: xyly('3'))
bt3.grid(row=3, column=3)
btNhan = Button(fr, text='*', font=fts, width=drnum, pady=py, command=lambda: xyly('*'))
btNhan.grid(row=3, column=4)

# Hàng 4
bt0 = Button(fr, text='0', font=fts, width=drnum, pady=py, command=lambda: xyly('0'))
bt0.grid(row=4, column=1)
bt00 = Button(fr, text='00', font=fts, width=drnum, pady=py, command=lambda: xyly('00'))
bt00.grid(row=4, column=2)
btDot = Button(fr, text='.', font=fts, width=drnum, pady=py, command=lambda: xyly('.'))
btDot.grid(row=4, column=3)
btChia = Button(fr, text='/', font=fts, width=drnum, pady=py, command=lambda: xyly('/'))
btChia.grid(row=4, column=4)

# Hàng 5
btLeft = Button(fr, text='<', font=fts, width=drnum, pady=py, command=MoveLeft)
btLeft.grid(row=5, column=1)
btRight = Button(fr, text='>', font=fts, width=drnum, pady=py, command=MoveRight)
btRight.grid(row=5, column=2)
btDel = Button(fr, text='Del', font=fts, width=drnum, pady=py, command=DelChar)
btDel.grid(row=5, column=3)
btBang = Button(fr, text='=', font=fts, width=drnum, pady=py, command=TinhToan)
btBang.grid(row=5, column=4)

# Hàng 6
btPrev = Button(fr, text='←', font=fts, width=drnum, pady=py, command=Prev)
btPrev.grid(row=6, column=1)
btNext = Button(fr, text='→', font=fts, width=drnum, pady=py, command=Next)
btNext.grid(row=6, column=2)
btC = Button(fr, text='C', font=fts, width=drnum, pady=py, command=ClearHistory)
btC.grid(row=6, column=3)
btAC = Button(fr, text='AC', font=fts, width=drnum, pady=py, command=ClearAll)
btAC.grid(row=6, column=4)

# Tải lịch sử khi ứng dụng bắt đầu
load_history()
# Chạy vòng lặp chính
wd.mainloop()
