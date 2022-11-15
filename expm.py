from tkinter import messagebox
class exp:

    temp_amt_list=[]
    temp_exp_list=[]
    def __init__(self) -> None:
        pass

    @classmethod    
    def AmtExpL(cls):
        cls.temp_amt_list=[]
        for x in cls.temp_exp_list:
            cls.temp_amt_list.append(int(x[2]))
        

    def AddExp(self,name,amt):
            if not amt.isnumeric():
                messagebox.showinfo(title="ERROR",message="Pls Enter Numaric value")
            else:
                self.temp_exp_list.append([str(len(self.temp_exp_list)+1),str(name),str(amt)])
                messagebox.showinfo(title="saved",message=str(name)+str(amt))
                self.AmtExpL()
    def Exps(self):
        return self.temp_exp_list

    @classmethod
    def TotalExp(cls):
        print(cls.temp_amt_list)
        return str(len(cls.temp_amt_list))

    @classmethod
    def SumOfExp(cls):
        return str(sum(cls.temp_amt_list))
    
    def AvgOfExp(self):
        avg=int(self.SumOfExp())/int(self.TotalExp())
        return str(round(avg,2))

    def MaxOfExp(self):
        temp_ar=self.temp_amt_list
        temp_ar.sort()
        return str(temp_ar[-1])

    def MinOfExp(self):
        temp_ar=self.temp_amt_list
        temp_ar.sort()
        return str(temp_ar[0])