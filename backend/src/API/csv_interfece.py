# Import CSV library
import csv




# Define the path to the CSV files
tools_csv_path = 'tools.csv'
tools_availability_csv_path = 'tools_availability.csv'




# Implement the function to check the availability of a tool
def csvInterface_checkAvailability(tool_sap: str, start_time: int, end_time: int) -> bool:

    # Open the tools_availability.csv file
    with open(tools_availability_csv_path, mode='r') as tools_availability_file:

        # Create a CSV reader object
        tools_availability_reader = csv.reader(tools_availability_file)

        for row in tools_availability_reader:
            if row[0] == tool_sap:
                for i in range(start_time, end_time):
                    if row[i + 1] == 'Reservado':
                        return False
                
                return True
        
        return False
    
# Implement tje function to reserve a tool
def csvInterface_reserveTool(tool_sap: str, start_time: int, end_time: int) -> bool:

    if (not csvInterface_checkAvailability(tool_sap, start_time, end_time)):
        return False

    # Open the tools_availability.csv file
    with open(tools_availability_csv_path, mode='r') as tools_availability_file:

        # Create a CSV reader object
        tools_availability_reader = csv.reader(tools_availability_file)

        # Create a list to store the rows of the CSV file
        tools_availability = list(tools_availability_reader)
    
    # Open the tools_availability.csv file in write mode
    with open(tools_availability_csv_path, mode='w', newline='') as tools_availability_file:

        # Create a CSV writer object
        tools_availability_writer = csv.writer(tools_availability_file)

        # Write the rows of the CSV file
        for row in tools_availability:
            if row[0] == tool_sap:
                for i in range(start_time, end_time):
                    row[i + 1] = 'Reservado'
            
            tools_availability_writer.writerow(row)
        
        return True

# Implement the function to release a tool
def csvInterface_releaseTool(tool_sap: str, start_time: int, end_time: int) -> bool:

    # Open the tools_availability.csv file
    with open(tools_availability_csv_path, mode='r') as tools_availability_file:

        # Create a CSV reader object
        tools_availability_reader = csv.reader(tools_availability_file)

        # Create a list to store the rows of the CSV file
        tools_availability = list(tools_availability_reader)
    
    # Open the tools_availability.csv file in write mode
    with open(tools_availability_csv_path, mode='w', newline='') as tools_availability_file:

        # Create a CSV writer object
        tools_availability_writer = csv.writer(tools_availability_file)

        # Write the rows of the CSV file
        for row in tools_availability:
            if row[0] == tool_sap:
                for i in range(start_time, end_time):
                    row[i + 1] = 'Livre'
            
            tools_availability_writer.writerow(row)
        
        return True