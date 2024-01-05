import streamlit as st
from helper import add_data_in_excel

def default_fields(name_of_item = True):
    if name_of_item:
        item_name = st.text_input("Name of Item")
        item_quantity = st.text_input("Quantity of Item")
        item_amount = st.text_input("Amount of Item")
        item_shop_name = st.selectbox("Shop name", ['MashaAllah(Shakori)', 'Imran Kryana Store', 'Ahsan Kryana Store', 'Gujjar Milk Shop', 'Other'])
        if item_shop_name == 'Other':
            item_shop_name = st.text_input("Enter Shop Name")
        item_description = st.text_area("Description", placeholder="optional")
        return item_name , item_quantity, item_amount, item_shop_name, item_description
    else:
        item_quantity = st.text_input("Quantity of Item")
        item_amount = st.text_input("Amount of Item")
        item_shop_name = st.selectbox("Shop name", ['MashaAllah(Shakori)', 'Imran Kryana Store', 'Ahsan Kryana Store', 'Gujjar Milk Shop', 'Other'])
        if item_shop_name == 'Other':
            item_shop_name = st.text_input("Enter Shop Name")
        item_description = st.text_area("Description", placeholder="optional")
        return  item_quantity, item_amount, item_shop_name, item_description

# main header
st.header("Budget Management System")
st.subheader("Add Record")

# expense type
expense_type = st.selectbox("Select Expense Type", ['Daily Expenses', 'Weekly Expenses', 'Monthly Expenses', 'Extra Expenses', 'Vehicle Expenses'])
# item
if expense_type == 'Daily Expenses':
    category = st.selectbox("Select Category", ['Milk', 'Vegetable/Fruits', 'Groceries'])
    if category == 'Milk':
        item_name = category
        item_quantity, item_amount, item_shop_name, item_description = default_fields(False) 
    else:
        item_name, item_quantity, item_amount, item_shop_name, item_description = default_fields() 
    # READY
elif expense_type == 'Weekly Expenses':
    category = st.selectbox("Select Category", ['Vegetable/Fruits', 'Groceries', 'Others'])
    if category == 'Others':
        category = st.text_input("Name of Category")
    item_name, item_quantity, item_amount, item_shop_name, item_description = default_fields()
elif expense_type == 'Monthly Expenses':
    category = st.selectbox("Select Category", ['Vegetable/Fruits', 'Groceries', 'Fees', 'Utility Bills', 'Others'])
    over_all_entry = st.toggle('Are you wanna add overall amount?')
    if over_all_entry:
        if category == 'Others':
            category = st.text_input("Name of Category")
        item_name = category
        item_amount = st.text_input(f"Amount of {item_name}")
        item_description = st.text_area("Description", placeholder="optional") 
        # READY (Quantity Missing)
    else:
        if category == 'Others':
            category = st.text_input("Name of Category")
            item_name, item_quantity, item_amount, item_description = default_fields()
        # elif category == 'Fees':
        #     # type of fee = item_name
        #     pass
        elif category == 'Utility Bills':
            item_name = st.selectbox("Type of bill", ['Electricity', 'Gas', 'WASA', 'Internet', 'Others'])
            if item_name == 'Others':
                item_name = st.text_input("Type of Bill")
            item_quantity, item_amount, item_shop_name, item_description = default_fields(False)
            # READY
        else:
            item_name, item_quantity, item_amount, item_shop_name, item_description = default_fields()
            # READY
else:
    category = st.selectbox("Select Category", ['Medicine', 'Others'])
    if category == 'Others':
        category = st.text_input("Category")
    item_name, item_quantity, item_amount, item_shop_name, item_description = default_fields()
    # READY

if st.button("Save Record"):
    if add_data_in_excel(expense_type, category, item_name, item_quantity, item_amount, item_shop_name, item_description) == 'success':
        st.success(f"Record for '{item_name}' has been Saved Successfully!")
