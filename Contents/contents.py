# Define the content structure using a nested dictionary
content = {
    "📊 Main Content: Business Data Analysis": {
        "🔍 Sub Content": {
            "1. Excel": {
                "1a. Excel Basic": {},
                "1b. Data Visualization": {},
                "1c. Data Analytics": {},
                "1d. Power Query": {},
                "1e. Project": {}
            },
            "2. SQL": {
                "2a. SQL Basics": {},
                "2b. SQL Data Analysis": {},
                "2c. SQL and Power BI": {},
                "2d. Project": {}
            },
            "3. Python": {
                "3a. Python Basics (100 Days)": {},
                "3b. Data Analysis with Python": {},
                "3c. Data Visualization with Python": {},
                "3d. Python Project": {}
            },
            "4. Excel Automation with SQL": {},
            "5. Excel Automation with Python": {}
        }
    }
}

# Function to print items with appropriate indentation
def print_items(items, indent=0):
    for item, sub_items in items.items():
        # Print item with indentation
        print(" " * indent + item)
        if sub_items:
            # Recursively print sub-items with increased indentation
            print_items(sub_items, indent + 4)

# Print the content hierarchy with emojis 🎓📚
print_items(content)

# Add emojis to show enthusiasm 🚀🎉
print("🌟 Enjoy exploring the exciting course content! 🌟")

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Section for Excel 📊

# Function to demonstrate Excel topics
def excel_section():
    print("📊 Excel Section:")
    # Your code for Excel content here

# Call the Excel section function
excel_section()

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Section for SQL 🔍

# Function to demonstrate SQL topics
def sql_section():
    print("🔍 SQL Section:")
    # Your code for SQL content here

# Call the SQL section function
sql_section()

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Section for Python 🐍

# Function to demonstrate Python topics
def python_section():
    print("🐍 Python Section:")
    # Your code for Python content here

# Call the Python section function
python_section()

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Section for Excel Automation with SQL 💼

# Function to demonstrate Excel Automation with SQL topics
def excel_sql_automation_section():
    print("💼 Excel Automation with SQL Section:")
    # Your code for Excel Automation with SQL content here

# Call the Excel Automation with SQL section function
excel_sql_automation_section()

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Section for Excel Automation with Python 🤖

# Function to demonstrate Excel Automation with Python topics
def excel_python_automation_section():
    print("🤖 Excel Automation with Python Section:")
    # Your code for Excel Automation with Python content here

# Call the Excel Automation with Python section function
excel_python_automation_section()

# Visual separation for better readability
print("\n" + "="*40 + "\n")

# Add final message
print("🌟 That's all! Enjoy your learning journey! 🌟")
