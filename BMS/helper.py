import pandas as pd
import os
from datetime import datetime

# ======================== CRUD =======================
def initialize_excel_file(fileName = "Budget.csv"):
    df  = pd.DataFrame({"Date":[],
                        "Expense_type": [],
                        "Category":[],
                        "Item_name":[],
                        "Item_quantity":[],
                        "Item_amount":[],
                        "Shop_name":[],
                        "Item_description":[]})
    df.to_csv(fileName)
    return fileName

def get_excel_file_name():
    available_files = os.listdir(os.getcwd())
    for file in available_files:
        if file.endswith("Budget.csv"):
            return file
    return initialize_excel_file()

def get_data_from_excel():
    csv_data = pd.read_csv(get_excel_file_name())
    try:
        csv_data = csv_data.drop(['Unnamed: 0'], axis=1)
    except:
        pass
    return csv_data

def add_data_in_excel(expense_type,
                        category,
                        item_name,
                        item_quantity,
                        item_amount,
                        shop_name,
                        item_description,
                        date_time = datetime.today()):
    
    file_name = get_excel_file_name()
    # Load data from the CSV file
    existing_data = get_data_from_excel()
    # Seperate Date and Time
    date = date_time.date()
    # time = date_time.time()
    # Create a new DataFrame with the new data
    new_data = pd.DataFrame({
        "Date":[date],
        "Expense_type": [expense_type],
        "Category":[category],
        "Item_name":[item_name],
        "Item_quantity":[item_quantity],
        "Item_amount":[item_amount],
        "Shop_name":[shop_name],
        "Item_description":[item_description]
        })
    # Concatenate the existing data and new data
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    # Save the updated DataFrame to the CSV file
    combined_data.to_csv(file_name, index=False)
    return "success"

# remaining
def update_record(vehicle_type, vehicle_number, vehicle_service, user_inputs):
    data_from_db = get_data_from_excel()
    mask = (
        (data_from_db['Vehicle_type'] == vehicle_type) &
        (data_from_db['Vehicle_number'] == vehicle_number) &
        (data_from_db['Vehicle_service'] == vehicle_service)
    )
    data_from_db.loc[mask, user_inputs.keys()] = list(user_inputs.values())
    data_from_db.to_csv(get_excel_file_name(), index=False)

# remaining
def delete_records(list_of_deleted_index):
    try:
        data_from_db = get_data_from_excel()
        data_from_db = data_from_db.drop(list_of_deleted_index)
        data_from_db.to_csv(get_excel_file_name(), index=False)
        return "Record Deleted Successfully"
    except:
        return "Something went wrong!"
    
# ========================= Filters =========================
def get_available_column_data(column_name = 'Date'):
    data_from_db = get_data_from_excel()
    return list(data_from_db[column_name].unique())

def  get_expense_type():
    data_from_db = get_data_from_excel()
    return data_from_db['expense_type'].unique().tolist()

def get_vehicle_service(Vehicle_type, Vehicle_number, return_list = True):
    data_from_db = get_data_from_excel()
    type_filter = data_from_db[data_from_db['Vehicle_type'] == Vehicle_type]
    number_filter = type_filter[type_filter['Vehicle_number'] == Vehicle_number]
    if return_list:
        return number_filter['Vehicle_service'].unique().tolist()
    return type_filter[type_filter['Vehicle_number'] == Vehicle_number]

def get_respective_columns(Vehicle_type, Vehicle_number, Vehicle_service):
    data_from_db = get_data_from_excel()
    type_filter = data_from_db[data_from_db['Vehicle_type'] == Vehicle_type]
    number_filter = type_filter[type_filter['Vehicle_number'] == Vehicle_number]
    service_filter = number_filter[number_filter['Vehicle_service'] == Vehicle_service]
    return service_filter, service_filter.columns.tolist()

# =========================
def add_list_items(list_of_numbers):
    added_value = 0
    for i in list_of_numbers:
        added_value = i + added_value
    return added_value

def get_total_amount():
    data_from_db = get_data_from_excel()
    return add_list_items(data_from_db['Item_amount'])

def get_daily_amount(date):
    data_from_db = get_data_from_excel()
    return add_list_items(data_from_db[data_from_db['Date'] == date]['Item_amount'])







def get_max_min_from_list(list_of_values):
    return max(list_of_values), min(list_of_values)

def bike_riding_calculation(max_reading, min_reading):
    max_reading = str(max_reading) 
    min_reading = str(min_reading)
    if len(max_reading) > 5:
        max_reading = max_reading[:5]
    if len(min_reading) > 5:
        min_reading = min_reading[:5]
    return int(max_reading) - int(min_reading)

def get_average(list_of_numbers):
    return add_list_items(list_of_numbers) / len(list_of_numbers)
    
def  total_petrol_in_liters(data_of_same_vehicle_number):
    # Add all times litre petrol
    return add_list_items(list(data_of_same_vehicle_number['Litre']))

def ideal_travel(data_of_same_vehicle_number):
    return int(get_average(list(data_of_same_vehicle_number['Vehicle_service_average'])) * total_petrol_in_liters(data_of_same_vehicle_number))

def remaining_distance_in_km(data_of_same_vehicle_number, bike_traveled_in_km):
    return ideal_travel(data_of_same_vehicle_number) - bike_traveled_in_km

def consumed_petrol(data_of_same_vehicle_number):
    return None

def  remaining_petrol_in_liters(data_of_same_vehicle_number):
    return total_petrol_in_liters(data_of_same_vehicle_number)