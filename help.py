import sqlite3
import pandas as pd



class  Inventory:

    def __init__(self):
      self.test=pd.read_excel('test.xlsx')
      self.db=sqlite3.connect('Stock.db')
      self.cursor=self.db.cursor()

      


      
# ________________purchaseing Menu________________



    def type(self):
        a=self.test["Type"].unique().tolist()
        a.insert(0,'Select')

        return a

    def commpany(self):
       a=self.test["Companys"].unique().tolist()
       a.insert(0,'Select')
       return a
    
    def purchase_entry(self,val1,val2,val3,val4,val5,val6):
       self.cursor.execute("INSERT INTO Mobile (Date,Type,Company,Model,IMS,Pur_Price) VALUES(?,?,?,?,?,?)",(val1, val2, val3, val4, val5,val6))
       self.db.commit()
       return 'Done'

    



# Repair Menu

    def home_menu():
        
        select=['Home','Purchasing','Repair','Sale']

        return select
    
    def repair_feching(self,val1):
       
        data=self.cursor.execute("SELECT * FROM Mobile WHERE IMS=?",(val1,))
        data=pd.DataFrame(data.fetchall(),columns=['Date','Type','Company','Model','IMEI','Price'])
        self.db.commit()
        return data
    

    def repair_submit(self,val1,val2,val3):
       
        self.cursor.execute("INSERT INTO Repair (Repair_Price,Des,IMEI) VALUES(?,?,?)",(val1, val2, val3))
        self.db.commit()
        return 'Done'
    


# ______Sale Menu________________



    def select_imei(self):
        sale_data=pd.read_sql_query("Select * from Repair",con=self.db)
        sale_imei_l=sale_data['IMEI'].unique().tolist()
        sale_imei_l.insert(0,'Select')
        
       
        return sale_imei_l






    def sale_imei(self,val1):
        data=self.db
        df=pd.read_sql_query('SELECT * FROM Repair INNER JOIN Mobile on Repair.IMEI = Mobile.IMS',con=data)
        df_ims=df[df['IMS']==str(val1)]
        df_price=df_ims['Repair_Price'] + df_ims['Pur_Price']
        cost_p=df_price
        cost_p=cost_p[0]
        return cost_p





    def sale_submit(self,val1,val2,val3,val4):
        self.cursor.execute("INSERT INTO Sale (Date,IMEI,Plateform,Sale_price) VALUES(?,?,?,?)",(val1,val2, val3, val4,))
        self.db.commit()
        return 'Done'

        
        
    




     
















