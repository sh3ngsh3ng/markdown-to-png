import pandas as pd
import matplotlib.pyplot as plt
import io

# Sample Markdown table
markdown_table = """
| Year | Country A | Country B | Country C | Country D |
|------|-----------|-----------|-----------|-----------|
| 2016 | 60%       | 50%       | 45%       | 30%       |
| 2017 | 65%       | 55%       | 50%       | 35%       |
| 2018 | 70%       | 60%       | 55%       | 40%       |
| 2019 | 75%       | 65%       | 60%       | 45%       |
| 2020 | 80%       | 70%       | 65%       | 50%       |
"""

# Preprocess Markdown table to extract rows and columns
rows = [row.strip() for row in markdown_table.strip().split("\n") if row.strip()]
data = [row.split("|")[1:-1] for row in rows[1:]]  # Skip the header row
columns = [col.strip() for col in rows[0].split("|")[1:-1]]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Clean up column names and data
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Style the table
styled_table = df.style \
    .set_properties(**{'text-align': 'center'}) \
    .set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#f2f2f2')]
    }])

# Save the styled table as an image
fig, ax = plt.subplots(figsize=(6, 3))
ax.axis('off')
ax.table(cellText=styled_table.data.values, colLabels=styled_table.columns, loc='center')

plt.savefig('styled_table.png', bbox_inches='tight', pad_inches=0.05)
plt.close()

print("Image saved as styled_table.png")
