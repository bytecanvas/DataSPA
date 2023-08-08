# main.py
from excel_content import display_excel_content
from sql_content import display_sql_content
from python_content import display_python_content
from excel_automation_sql_content import display_excel_automation_sql_content
from excel_automation_python_content import display_excel_automation_python_content

# Display content sections
display_excel_content()
print("="*40)

display_sql_content()
print("="*40)

display_python_content()
print("="*40)

display_excel_automation_sql_content()
print("="*40)

display_excel_automation_python_content()
print("="*40)

# Add final message
print("🌟 That's all! Enjoy your learning journey! 🌟")
