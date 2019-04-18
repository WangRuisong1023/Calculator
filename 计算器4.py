# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:32:56 2019

@author:Ruisong Wang

E-mail:wangruisong56@foxmail.com
"""

import tkinter as tk
from decimal import Decimal
#import math

win = tk.Tk()
win.geometry("400x640")
win.title("计算器")
win.resizable(width = False,height = False)
#创建text
see = tk.Frame(win)
see.place(width = 400, height = 140 )

scroll_r = tk.Scrollbar(see,orient=tk.VERTICAL)
scroll_b = tk.Scrollbar(see,orient=tk.HORIZONTAL)
text = tk.Text(see,bg='#5F9F9F',font=('宋体',20),height=10, yscrollcommand=scroll_r.set,xscrollcommand=scroll_b.set, wrap='none')
scroll = text

scroll_r.config(command=text.yview)
scroll_b.config(command=text.xview)

scroll_r.pack(fill="y", expand=0, side=tk.RIGHT, anchor=tk.N)
scroll_b.pack(fill="x", expand=0, side=tk.TOP, anchor=tk.N)
text.pack(fill="x", expand=1, side=tk.LEFT)


#计算结果
result = tk.StringVar()
result.set(0)
#计算过程
result2 = tk.StringVar()
result2.set('')
#展示1
label1 = tk.Label(win,font=('宋体',28),bg='#5F9F9F',bd='19',fg='black',anchor='se',textvariable=result2)
label1.place(width=400,height=60,y=140)
#展示2
label2 = tk.Label(win,font=('宋体',28),bg='#5F9F9F',bd='9',fg='black',anchor='se',textvariable=result)
label2.place(width=400,height=60,y=200)
#数字按钮
btn7 = tk.Button(win,text='7',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('7'))
btn7.place(x=0,y=400,width=100,height=60)
btn8 = tk.Button(win,text='8',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('8'))
btn8.place(x=100,y=400,width=100,height=60)
btn9 = tk.Button(win,text='9',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('9'))
btn9.place(x=200,y=400,width=100,height=60)

btn4 = tk.Button(win,text='4',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('4'))
btn4.place(x=0,y=460,width=100,height=60)
btn5 = tk.Button(win,text='5',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('5'))
btn5.place(x=100,y=460,width=100,height=60)
btn6 =tk.Button(win,text='6',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('6'))
btn6.place(x=200,y=460,width=100,height=60)

btn1 = tk.Button(win,text='1',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('1'))
btn1.place(x= 0,y= 520,width=100,height=60)
btn2 = tk.Button(win,text='2',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('2'))
btn2.place(x=100,y=520,width=100,height=60)
btn3 = tk.Button(win,text='3',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('3'))
btn3.place(x=200,y=520,width=100,height=60)
btn0 = tk.Button(win,text='0',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('0'))
btn0.place(x=100,y=330,width=100,height=70)

#符号
btn_point = tk.Button(win,text='.',font=('宋体',28),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('.'))
btn_point.place(x=200,y=580,width=100,height=60)
btn_left = tk.Button(win,text='(',font=('微软雅黑',25),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press('('))
btn_left.place(x=0,y=580,width=100,height=60)
btn_left = tk.Button(win,text=')',font=('微软雅黑',25),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:press(')'))
btn_left.place(x=100,y=580,width=100,height=60)
btn_notes = tk.Button(win,text='☰',font=('微软雅黑',15),bg='#5F9F9F',fg='#2F4F2F',bd='2',command=lambda:pressSee())
btn_notes.place(x=100,y=260,width=200,height=70)  
clear = tk.Button(win, text="∷", font=('宋体',20),bg='#5F9F9F',fg='#2F4F2F',bd='2',command=lambda:clearText_1())
clear.place(x=300 ,y=260,width=100, height=70)  
clear_2 = tk.Button(win, text="∷", font=('宋体',20),bg='#5F9F9F',fg='#2F4F2F',bd='2',command=lambda:scroll.delete(0.0, tk.END))
clear_2.place(x=0 ,y=260,width=100, height=70)
btn_c = tk.Button(win,text='C',font=('微软雅黑',25),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:pressCom('C'))
btn_c.place(x=0,y=330,width=100,height=70)
btn_er = tk.Button(win,text='☜',font=('微软雅黑',25),bg='#5F9F9F',fg='#871F78',bd='2',command=lambda:pressCom('E'))
btn_er.place(x=200,y=330,width=100,height=70)
btn_plus = tk.Button(win,text='+',font=('微软雅黑',25),bg='#8B008B',fg='white',bd='2',command=lambda:pressCom('+'))
btn_plus.place(x=300,y=520,width=100,height=60)   
btn_sub = tk.Button(win,text='-',font=('微软雅黑',25),bg='#8B008B',fg='white',bd='2',command=lambda:pressCom('-'))
btn_sub.place(x=300,y=460,width=100,height=60) 
btn_mult = tk.Button(win,text='×',font=('微软雅黑',25),bg='#8B008B',fg='white',bd='2',command=lambda:pressCom('*'))
btn_mult.place(x=300,y=400,width=100,height=60) 
btn_div = tk.Button(win,text='÷',font=('微软雅黑',25),bg='#8B008B',fg='white',bd='2',command=lambda:pressCom('/'))
btn_div.place(x=300,y=330,width=100,height=70)  
btn_equal = tk.Button(win,text='=',font=('微软雅黑',25),bg='#8B008B',fg='white',bd='2',command=lambda:pressEqu())
btn_equal.place(x=300,y=580,width=100,height=60) 

#po_w = tk.Button(win,text='Xⁿ',font=('微软雅黑',18),bg='#8B008B',fg='white',bd='2',command=lambda:pressCom('^'))
#po_w.place(x=0,y=295,width=100,height=35)
#sqr = tk.Button(win,text='√',font=('微软雅黑',18),bg='#8B008B',fg='white',bd='2',command=lambda:sqr())
#sqr.place(x=100,y=295,width=100,height=35)
#sin = tk.Button(win,text='sin',font=('微软雅黑',18),bg='#8B008B',fg='white',bd='2',command=lambda:sin())
#sin.place(x=200,y=295,width=100,height=35)
#log = tk.Button(win,text='log',font=('微软雅黑',18),bg='#8B008B',fg='white',bd='2',command=lambda:log('log'))
#log.place(x=300,y=295,width=100,height=35)
 
win.mainloop()

#操作函数
dd=0
lists = []   
see = []                     
isPressSign = False                  
isPressNum = False
#数字函数
def press(num):                 
    global lists                   
    global isPressSign
    if isPressSign == False:
        pass
    else:                            
        result.set(0)
        isPressSign = False

    #判断界面的数字是否为0
    oldnum = result.get()             
    if oldnum =='0':               
        result.set(num)
    else:                            
        newnum = oldnum + num
        result.set(newnum)          

#运算函数
def pressCom(sign):
    global lists
    global isPressSign
#    global dd
    
    num = result.get()              #获取界面数字
    lists.append(num)               #保存界面获取的数字到列表中
    result.set(sign)
    lists.append(sign)              #讲按下的运算符号保存到列表中
    isPressSign = True

    if sign =='C':                
        lists.clear()
        result.set(0)
    if sign =='E':                 #如果按下的是退格，则选取当前数字第一位到倒数第二位
        a = num[0:-1]
        lists.clear()
        result.set(a)
#    if sign =='^':
#        lists.remove(-1)
#        b = lists[-1]
#        c = lists[-1]
#        dd = math.pow(b,c)
        
#获取运算结果函数  
def pressEqu():
    global lists
    global isPressSign
#    global dd
    
    curnum = result.get()           #设置当前数字变量，并获取添加到列表
    lists.append(curnum)
    computrStr = ''.join(lists)     #讲列表内容用join命令将字符串链接起来
    try:
#        if(dd == 0):
#            pass
#        else:
#            computrStr = str(dd)
            
        endNum = eval(computrStr)       #用eval命令运算字符串中的内容
        d = Decimal(str(endNum)).quantize(Decimal('0.00'))
        strr = computrStr+'='+str(d)+'\n'
        file = open("D:\\编软练习\\Python练习\\计算器\\123.txt",'a+')
        s=str(strr.replace('"','').replace("'",''))
        file.write(s)
        file.close()
        print("保存成功")
        result.set(d)              #讲运算结果显示到屏幕1
        result2.set(computrStr)         #将运算过程显示到屏幕2
        lists.clear()                   #清空列表内容
    except:
        result.set('错误')
        
def pressSee():
    filename = 'D:\\编软练习\\Python练习\\计算器\\123.txt'
    with open(filename) as f:
        for each_line in f:
            text.insert(tk.INSERT,each_line) 
def clearText_1():
    f = open("D:\\编软练习\\Python练习\\计算器\\123.txt",'r+')
    f.truncate()
    f.close()
    print("删除成功")

#def sqr():
#    global d
#    result.set('√')
#    d=math.sqrt(d)
#    return d
    