import streamlit as st
import datetime
from help import Inventory as helpers
import matplotlib.pyplot as plt



st.set_page_config(page_title='Repairwave.electronic',page_icon='���',layout='wide')


# Object notation
user_seleted=st.sidebar.selectbox('Select Options',helpers.home_menu())



# _______________Home Menu ________

if user_seleted=='Data_Entry':

    tab1,tab2,tab3,tab4=st.tabs(['Purchasing','Repair','Sale','Services'])

    # ---------------Purchasing Menu-----------------

    with tab1:
        st.header('Purchasing Entry')
        col1 ,col2=st.columns(2)
        
    
    with col1:
        date=st.date_input('Select Date',datetime.date.today())

        with tab1:

            with st.form('M.T',clear_on_submit=True):
                col1,col2,col3,col4,col5=st.columns(5,gap='medium')
                with col1:
                    select_type=st.selectbox('Select Type',['Select','Mobile','Tablet'])
                with col2:
                    company=st.selectbox('Company',helpers().commpany())
                with col3:
                    model_name=st.text_input('Model name')
                with col4:
                    imei=st.text_input('IMEI or SN')
                with col5:
                    price=st.number_input('Price',)
                
                st.form_submit_button('Submit',type='primary')
                if company =='Select' or select_type=='Select' or len(model_name)==0 or len(imei)==0 or price<=0:
                    st.error('Please fill all the fields', icon="🛒")      
                    
                else:
                    try:
                        helpers().purchase_entry(date,select_type,company,model_name,imei,price)
                        st.success('Submited !', icon="✅")
                    except Exception as e:
                        st.error('This IMEI & SN Already Submit', icon="🔒")


# ----------------Repair Menu-----------------
    
    with tab2:
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
                price=st.number_input('Price',)
            with col2:
                des=st.text_input('Description')
            with col1:
                imei=st.text_input('IMEI or Serial Number',data_imei,disabled=True)
            with col4:
            
                st.form_submit_button('Submit',type='primary')
                if price<=0 or des=='' :
                    st.error('Please fill all the fields',)
                else:
                    try:
                        helpers().repair_submit(price,des,imei)
                        st.success('Submited!', icon="✅")
                    except Exception as e:
                        st.error('This IMEI & SN Already Submit', icon="🔒")

# --------------SALE MENU-----------------

    with tab3:
        with st.form('sale_form_submit',clear_on_submit=True):

            col1,col2,col3,col4,col5,col6=st.columns(6)
        with col1:
            sale_date=st.date_input('Select Date',datetime.date.today())

        with col2:
            sale_imei=st.selectbox('Enter IMEI or SN',helpers().select_imei())


        with col3:
            plat_form=st.selectbox('Select Platform',['Select','Facebook','ebay','Other'])
        with col4:
            sale_price=st.number_input('Sale Price',)
        with col5:
            delievry=st.number_input('Delivery Cost',)

        with col6:
            st.form_submit_button('Submit',type='primary')


            if sale_imei == 'Select' or  plat_form=='Select' or sale_price <= 0 :
                st.error('Please fill all the fields',)
            else:
            
                try:
                    helpers().sale_submit(sale_date,sale_imei,plat_form,sale_price,delievry)
                    st.success('Submitted!')
        
                except Exception as e:
                    st.error('This IMEI & SN Already Submit')


# ------------------------Services Menu-----------------


    with tab4:
        with st.form('Services',clear_on_submit=True):
            col1,col2,col3,col4= st.columns(4)
            with col1:
                service_date=st.date_input('Date',datetime.date.today())
            with col2:
                service_dec=st.text_input('Deatils')
            with col3:
                service_price=st.number_input('Service Price',)
            with col4:
            
                st.form_submit_button('Saved',type='primary')

                if len(service_dec)==0 or service_price<=0:
                    st.error('Please fill all the fields')
                else:
                    try:
                        helpers().services_submit(service_date,service_dec,service_price)
                        st.success('Submitted!')
                    except Exception as e:
                        st.error('Error Occured')



            




# ---------------Montring Menu-----------------

elif user_seleted=='Monitoring':
    st.header('Wellcome To Repairwave.electronic')
    
    tab1,tab2=st.tabs(['Monitoring','Mobile & Tablet'])
    t_sale,t_profit,t_cost,t_delivery=helpers().morniting()
    
    with tab1:
        st.title('Monitoring')
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.text_input('Total Sales',value=t_sale,disabled=True)
        with col2:
            st.text_input('Total Profit',value=t_profit,disabled=True)
        with col3:
            st.text_input('Toatl Cost',value=t_cost,disabled=True)

        with col4:
            st.text_input('Delivery',value=t_delivery,disabled=True)

        col1,col2=st.columns(2)

        with col1:

            labels = 'Total Sales', 'Total Profit', 'Toatl Cost'
            sizes = [t_sale,t_profit,t_cost,]
            
            fig1, ax1 = plt.subplots()
            plt.figure(figsize=(2, 2))
            
            ax1.pie(sizes,labels=labels, autopct='%1.1f%%',shadow=True,)
            st.pyplot(fig1,clear_figure=True,)

        

        
    
    with tab2:
       col1,col2,col3= st.columns(3)
       with st.form('items checked',clear_on_submit=True):
    
            with col1:
             available_items=st.text_input('Enter IMEI or SN')
        

            st.form_submit_button('Submit',type='primary')
            if len(available_items)==0:
                st.error('Please fill the fields', icon="🛒")
            else:
                try:
                    data=helpers().available_items(available_items)
                    st.dataframe(data,use_container_width=True)
                    if len(data)==0:
                        with col2:
                            st.success('No Data Found Please check in Repair Menu', icon="🛒")
                    else:   
                        st.error('Items sold',)
                except Exception as e:
                    st.error(e, icon="🛒")
