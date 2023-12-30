# Write programs to understand the use of Pandas for Reading and Writing Data using CSV and Textual Files, HTML Files, XML, Microsoft Excel Files.

import pandas as pd

# Reading data from CSV
csv_data = pd.read_csv('Test.csv')  
print("Data from CSV:")
print(csv_data)

# Writing data to CSV
csv_data.to_csv('08_output.csv', index=False)  # Writing to 'output.csv', excluding index



# Reading data from text file
text_data = pd.read_table('Text.txt')  
print("\nData from Text File:")
print(text_data)

# Writing data to text file
text_data.to_csv('08_output.txt', sep='\t', index=False)  # Writing to 'output.txt' with tab separator

# Reading data from HTML
# html_data = pd.read_html('https://www.example.com/table.html')  
# print("\nData from HTML:")
# print(html_data[0])  # Displaying the first table, use index accordingly

# # Writing data to HTML
# html_data[0].to_html('output.html', index=False)  # Writing to 'output.html' without index


# # Reading data from XML
# xml_data = pd.read_xml('data.xml') 
# print("\nData from XML:")
# print(xml_data)

# # Writing data to XML
# xml_data.to_xml('output.xml')  # Writing to 'output.xml'


# Reading data from Excel
# excel_data = pd.read_excel('data.xlsx') 
# print("\nData from Excel:")
# print(excel_data)

# # Writing data to Excel
# excel_data.to_excel('output.xlsx', index=False)  # Writing to 'output.xlsx' without index


