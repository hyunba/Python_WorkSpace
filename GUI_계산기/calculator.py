import tkinter as tk

res_value = 0
oper = {'+' : 1, '-' : 2, '/' : 3, '*' : 4, 'C' : 5, '=' : 6} # 문자를 숫자로 치환을 함 why? 기호를 if문으로 구현하기 위해서
stor_value = 0
pre_oper = 0


def number_click(value):
    # print('숫자', value)
    global res_value
    res_value = (res_value * 10) + value
    str_value.set(res_value) # set을 통해 변수의 값이 자동으로 전역변수에 업데이트 되는 부분

def clear():
    global res_value, oper, stor_value, pre_oper

    stor_value = 0
    res_value = 0
    pre_oper = 0
    str_value.set(res_value)

def operator_click(value):
    print('기호', value)
    global res_value, oper, stor_value, pre_oper # 클릭을 사용하기위해 전역변수를 가져옴
    op = oper[value]
    if op == 5: # 'C'
        clear()

    elif res_value == 0:
        pre_oper = 0

    elif pre_oper == 0: # 새로운 기호가 눌렸을 때
        pre_oper = op
        stor_value = res_value # 현재 값을 저장
        res_value = 0 # 새로 값을 입력하기 위해 0으로 만들어줌
        str_value.set(res_value)

    elif op == 6: # '='
        if pre_oper == 1: # 1은 '+'
            res_value = stor_value + res_value # 이전의 값인 stor 값과 현재의 값 res를 더함
        if pre_oper == 2:
            res_value = stor_value - res_value
        if pre_oper == 3:
            res_value = stor_value / res_value
        if pre_oper == 4:
            res_value = stor_value * res_value
        str_value.set(str(res_value))
        res_value = 0 # 변수는 항상 초기화 안그러면 결과 값에 이어서 숫자가 붙어서 나오게됨
        stor_value = 0
        pre_oper = 0
    else:
        clear() # 그 외의 오류가 날 경우


def button_click(value):
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

win = tk.Tk()
win.title('계산기')

str_value = tk.StringVar()
str_value.set(str(res_value))
dis = tk.Entry(win, textvariable = str_value, justify = 'right')
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 80, ipady = 30)

calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):

        bt = tk.Button(win, 
            text = item, 
            width = 10, 
            height = 5,
            bg = 'skyblue',
            fg = 'black',
            command = lambda cmd = item: button_click(cmd)
            )
        bt.grid(column = k, row = (i+1))

win.mainloop()
# 단순 버전

# tk.Button(win, text = '1', width = 10, height = 5).grid(column = 0, row = 1)
# tk.Button(win, text = '2', width = 10, height = 5).grid(column = 1, row = 1)
# tk.Button(win, text = '3', width = 10, height = 5).grid(column = 2, row = 1)
# tk.Button(win, text = '4', width = 10, height = 5).grid(column = 3, row = 1)

# tk.Button(win, text = '5', width = 10, height = 5).grid(column = 0, row = 2)
# tk.Button(win, text = '6', width = 10, height = 5).grid(column = 1, row = 2)
# tk.Button(win, text = '7', width = 10, height = 5).grid(column = 2, row = 2)
# tk.Button(win, text = '8', width = 10, height = 5).grid(column = 3, row = 2)

# tk.Button(win, text = '9', width = 10, height = 5).grid(column = 0, row = 3)
# tk.Button(win, text = '0', width = 10, height = 5).grid(column = 1, row = 3)
# tk.Button(win, text = '+', width = 10, height = 5).grid(column = 2, row = 3)
# tk.Button(win, text = '-', width = 10, height = 5).grid(column = 3, row = 3)

# tk.Button(win, text = '/', width = 10, height = 5).grid(column = 0, row = 4)
# tk.Button(win, text = '*', width = 10, height = 5).grid(column = 1, row = 4)
# tk.Button(win, text = 'C', width = 10, height = 5).grid(column = 2, row = 4)
# tk.Button(win, text = '=', width = 10, height = 5).grid(column = 3, row = 4)
