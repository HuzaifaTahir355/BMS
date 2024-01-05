import streamlit as st
from helper import get_total_amount, get_available_column_data, get_daily_amount

# st.header("Budget Management System")
st.subheader("Budget Management System")
st.write(f"Total Amount Spend from 01-01-2024 till now is Rs/_{get_total_amount()}")


col1, col2 = st.columns(2)
with col1:
    st.subheader("Filters")
    date = st.selectbox("Select Desired Date", get_available_column_data())
    expense_type = st.selectbox("Select Expense Type", get_available_column_data('Expense_type'), index=None)
    category = st.selectbox("Select Category", get_available_column_data('Category'), index=None)
    item_name = st.selectbox("Select Item_name", get_available_column_data('Item_name'), index=None)
    shop_name = st.selectbox("Select Shop_name", get_available_column_data('Shop_name'), index=None)
with col2:
    st.subheader("Data")
    st.write("\n")
    st.write(f"Total Amount Spend on {date} is Rs/_{get_daily_amount(date)}")
    if expense_type:
        st.write(expense_type)
    if category:
        st.write(category)
    if item_name:
        st.write(item_name)
    if shop_name:
        st.write(shop_name)





# "Date"
# "Expense_type"
# "Category"
# "Item_name"
# "Item_quantity"
# "Item_amount"
# "Shop_name"
# "Item_description"