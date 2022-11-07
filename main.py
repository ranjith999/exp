from tkinter import *
from tkinter import messagebox
from tkinter import ttk



Tableheading=("Sno","Exp_name","exp_amt")
TableData=[]


root=Tk()
root.configure(background="#C689C6")
root.geometry("700x200")
root.title('PYTHON 1 Assigment')
root.resizable(0,1)

def save():
    name=input_1.get()
    
    amt=input_2.get()
    if not amt.isnumeric():
        messagebox.showinfo(title="ERROR",message="Pls Enter Numaric value")
    else:
        TableData.append([str(len(TableData)+1),str(name),str(amt)])
        messagebox.showinfo(title="saved",message=str(name)+str(amt))
    renderview()
    dashboard()

def renderview():   
       
    tree = ttk.Treeview(root, columns=("S.NO", "Exp name", "Exp Amt"), show='headings', height=5)
    tree.heading('S.NO', text='S.NO')
    tree.heading('Exp name', text='Exp name')
    tree.heading('Exp Amt', text='Exp Amt')
    # Insert the data in Treeview widget

    for x in TableData:
        tree.insert('', 'end', text="1", values=x)

    tree.grid(row=3,column=1,columnspan =6)

def dashboard(): 
    temp_amt_list=[]
    for x in TableData:
        temp_amt_list.append(int(x[2]))
    count=len(TableData)
    sum_1=sum(temp_amt_list)
    avg=sum_1/count
    temp_amt_list.sort()
    min_1=temp_amt_list[0]
    max_1=temp_amt_list[-1]
    

    mylabel_01['text']='Total Exp : '+str(count)
    
    
    mylabel_02['text']='Sum Total Exp : '+str(sum_1)
    mylabel_03['text']='Avg Exp : '+str(avg)
    mylabel_04['text']='Max Exp : '+str(max_1)
    mylabel_05['text']='Min Exp : '+str(min_1)
    
        






mylabel_01=Label(root,text="COUNT" ,height=5,width=20,background="#9ED5C5")
mylabel_01.grid(row=1,column=1)
mylabel_02=Label(root,text="Sum",height=5,width=20,background="#9ED5C5")
mylabel_02.grid(row=1,column=2)
mylabel_03=Label(root,text="Avg",height=5,width=20,background="#9ED5C5")
mylabel_03.grid(row=1,column=3)
mylabel_04=Label(root,text="Max",height=5,width=20,background="#9ED5C5")
mylabel_04.grid(row=1,column=4)
mylabel_05=Label(root,text="Min",height=5,width=20,background="#9ED5C5")
mylabel_1=Label(root,text="Exp Name").grid(row=2,column=1)
mylabel_05.grid(row=1,column=5)
input_1=Entry()
input_1.grid(row=2,column=2)
mylabel_2=Label(root,text="Exp Amt").grid(row=2,column=3)
input_2=Entry()
input_2.grid(row=2,column=4)
btn1=Button(text="save",command=save).grid(row=2,column=5)



# mylabel.pack()

root.mainloop()