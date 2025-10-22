# HVAC Customer Tracker

A Python command-line application for tracking HVAC customers and their contact information.

## Features
- Add new customers with name, phone, and address
- View all customers in the system
- Search for specific customers by name
- Data stored in CSV format for easy access and portability

## How to Use

1. **Run the program:**
```bash
   python customer_tracker.py
```

2. **Choose from the menu:**
   - **1** - Add a new customer
   - **2** - View all customers  
   - **3** - Search for a customer by name
   - **4** - Exit the program

## Requirements
- Python 3.x
- No external libraries needed (uses built-in `csv` module)

## File Structure
```
hvac-customer-tracker/
├── customer_tracker.py    # Main application code
├── customers.csv          # Customer database (auto-created on first add)
└── README.md             # This file
```

## Example Usage

### Adding a Customer
```
Customer name: John Doe
Phone: 555-1234
Address: 123 Main St
```

### Searching for a Customer
```
Enter customer name to search: John
Match found: ['John Doe', '555-1234', '123 Main St']
```

## Future Improvements
- [ ] Add service history tracking
- [ ] Add appointment scheduling feature
- [ ] Export customer reports to PDF
- [ ] Add data validation (phone format, duplicate checking)
- [ ] Add ability to edit/delete customers
- [ ] Create a GUI version

## Author
Brian Estime - Computer Engineering Student

## License
This project is open source and available for educational purposes.
