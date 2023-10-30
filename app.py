import streamlit as st
import datetime
from help import Inventory as helpers
import numpy as np



st.set_page_config(page_title='Repairwave.electronic',page_icon='���',layout='wide')


# Object notation
user_seleted=st.sidebar.selectbox('Select Options',helpers.home_menu())



# _______________Home Menu ________

if user_seleted=='Home':
    st.header('Wellcome')
    col1,col2=st.columns(2)
    with col1:
        st.bar_chart(data=None)


    st.subheader('working on KPI')

   



#________________ purchasing Menu ________________


elif user_seleted=='Purchasing':
    st.header('Purchasing Entry')
    col1 ,col2=st.columns(2)
    tab1,tab2,=st.tabs(['Mobile & Tablet','Electric'])
    
    with col1:
        date=st.date_input('Select Date',datetime.date.today())

        with tab1:

            with st.form('M.T',clear_on_submit=True):
                col1,col2,col3,col4,col5=st.columns(5,gap='medium')
                with col1:
                    select_type=st.selectbox('Select Type',['','Mobile','Tablet'])
                with col2:
                    company=st.selectbox('Company',helpers().commpany())
                with col3:
                    model_name=st.text_input('Model name')
                with col4:
                    imei=st.text_input('IMEI or SN')
                with col5:
                    price=st.number_input('Price')
                
                st.form_submit_button('Submit',type='primary')
                if company =='Select' or len(select_type)==0 or len(model_name)==0 or len(imei)==0 or price<=0.00:
                    st.error('Please fill all the fields', icon="🛒")      
                    
                else:
                    try:
                        helpers().purchase_entry(date,select_type,company,model_name,imei,price)
                        st.success('Submited !', icon="✅")
                    except Exception as e:
                        st.error('This IMEI & SN Already Submit', icon="🔒")
    

                
                
               


            
            
                
                


            




    
    
        
        



   
        
        
       
        

            
        
    
  
    
# ___________Repair Menu ________

elif user_seleted =='Repair':


    st.header('Repair Entery')



      
    
    with st.form('IMEI_check',clear_on_submit=True):

        col1 ,col2, col3=st.columns(3)
        with col1:
            st.date_input('Select Date',datetime.date.today())
        with col2 :
            check=st.text_input('Enter IMIEI or Serial Number')
        
        with col3 :
        
            sub=st.form_submit_button('Check')
            data_get=helpers().repair_feching(check)
            data_imei=data_get['IMEI'].get(0)
            
        

    st_data=st.dataframe(data_get,use_container_width=True)
    

    tab1,=st.tabs(['Mobile & Tablet'])
    with st.form('repair_submit',clear_on_submit=True):
        col1,col2,col3,col4=st.columns(4)
        with col3:
            price=st.number_input('Price')
        with col2:
            des=st.text_input('Description')
        with col1:
            imei=st.text_input('IMEI or Serial Number',data_imei,disabled=True)
        with col4:
        
            st.form_submit_button('Submit',type='primary')
            if price==0.00 or des=='' :
                st.error('Please fill all the fields',)
            else:
                try:
                    helpers().repair_submit(price,des,imei)
                    st.success('Submited!', icon="✅")
                except Exception as e:
                    st.error('This IMEI & SN Already Submit', icon="🔒")


# ______________________END______________________

        
         
       


    

    
   

# ___________Sale__________________



elif user_seleted== 'Sale':

    
        tab1=st.tabs(['Mobile & Tablet'])


        with st.form('sale_form_submit',clear_on_submit=True):

            col1,col2,col3,col4,col5,col6=st.columns(6)
        with col1:
            sale_date=st.date_input('Select Date',datetime.date.today())

        with col2:
            sale_imei=st.selectbox('IMEI or Serial Number',helpers().select_imei())
            print(sale_imei)


        with col3:
            plat_form=st.selectbox('Select Platform',['','Facebook','ebay','Other'])
        with col4:
            sale_price=st.number_input('Sale Price')

        with col5:
            st.form_submit_button('Submit',type='primary')


            if sale_imei == 'Select' or  len(plat_form)==0 or sale_price < 0.00 :
                st.error('Please fill all the fields',)
            else:
            
                try:
                    helpers().sale_submit(sale_date,sale_imei,plat_form,sale_price)
                    st.success('Submitted!')
        
                except Exception as e:
                    st.error('This IMEI & SN Already Submit')
    





























