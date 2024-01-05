import streamlit as st
from helper import get_data_from_excel, delete_records


# main header
st.header("Budget Management System")
st.subheader("Display All Records")



editing = st.toggle('Are You Want to Delete Record?')

if editing:
    st.data_editor(get_data_from_excel(), key="my_key", num_rows="dynamic")
    if st.button("Save Record"):
        list_of_deleted_index = st.session_state["my_key"]["deleted_rows"]
        if list_of_deleted_index:
            st.success(delete_records(list_of_deleted_index))
        else:
            st.info("Please Delete selected item from the right top of table first then Press the button")
else:
    st.dataframe(get_data_from_excel(), use_container_width=True)