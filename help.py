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
        
        select=['Data_Entry','Monitoring',]

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





    def sale_submit(self,val1,val2,val3,val4,val5,):
        self.cursor.execute("INSERT INTO Sale (Date,IMEI,Plateform,Sale_price,Delivery) VALUES(?,?,?,?,?)",(val1,val2, val3, val4,val5))
        self.db.commit()
        return 'Done'

    


# ----------------Servises ------------------

    def services_submit(self,val1,val2,val3,):
        self.cursor.execute("INSERT INTO Service (Date,Dec,Price) VALUES(?,?,?)",(val1, val2, val3))
        self.db.commit()
        return 'Done'
    
        
    

# ----------------------Home ---------------------- ----------------


# iteam In Repair Mode


    def available_items(self,val1):
        data_base=self.db
        data=pd.read_sql_query("SELECT * FROM Sale ",con=data_base)
        data_b=data[data['IMEI'] ==val1]

        return data_b





# -------------Morniting--------------------------------


    def morniting(self):

        data_base=self.db
        df_mobile=pd.read_sql_query("select * from Mobile",con=data_base)
        df_repairs=pd.read_sql_query("select * from Repair",con=data_base)
        df_sales=pd.read_sql_query("select * from Sale",con=data_base)
        df_mr=df_mobile.merge(df_repairs,left_on='IMS',right_on='IMEI')
        df_m_r_s=df_mr.merge(df_sales,left_on='IMEI',right_on='IMEI')
        df_m_r_s['Profit'] =df_m_r_s['Sale_price']-(df_m_r_s['Pur_Price'] +df_m_r_s['Repair_Price']) 
        return df_m_r_s['Sale_price'].sum(), (df_m_r_s['Profit'] - (df_m_r_s['Delivery']+ df_m_r_s['Pur_Price'])).sum(),(df_m_r_s['Sale_price'].sum() - df_m_r_s['Profit'].sum()),df_m_r_s['Delivery'].sum(),




















