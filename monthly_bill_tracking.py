import gspread

gs = gspread.service_account('google_api_bill.json')

spreadsheet = gs.open('Monthly Bills for 2026')

# Get a worksheet by index

monthly_bills = spreadsheet.get_worksheet(0)

# Getting the row
bill_records = monthly_bills.get_values('A5:A10')

# Getting the cell value
cell1 = monthly_bills.acell('A9').value

# update a cell in a worksheet
# monthly_bills.update(range_name='P1:Q1', values=[['Paid_May','May']])

# update a single cell with coordinates
monthly_bills.update_cell(4,4, "877-936-4778")











