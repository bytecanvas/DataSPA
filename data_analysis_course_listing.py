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
