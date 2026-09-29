# Farm Water Manager

A simple Python-based console application designed to manage irrigation usage for farmers. This project records water consumption, motor usage, calculates bills, estimated profit, manages configurable rates, provides backup and restore functionality.

## 1. Project Description

Farm Water Manager provides a simple console-based solution where the operator can:

1. Add farmer and field information.
2. Record water usage in litres.
3. Record motor usage in hours.
4. Calculate individual bills.
5. Calculate total billing.
6. Estimate farmer profit.
7. Change water, motor, and crop-income rates.
8. Generate a random reward percentage.
9. Create data backups.
10. Restore previously saved data.
11. Store data between program runs.

## 2. Features

### 2.1 Farmer Management

1. Add a new farmer.
2. Store farmer name, field, crop, water usage, and motor hours.
3. Update an existing farmer's usage.
4. Identify a farmer using name and field.
5. View all registered farmers.

### 2.2 Bill Calculation

The application calculates the bill based on water usage and motor usage.

1. Water usage is multiplied by the water rate.
2. Motor usage is multiplied by the motor rate.
3. Both amounts are combined to calculate the total bill.

### 2.3 Profit Calculation

The application estimates farmer profit based on crop income and the calculated bill.

1. Calculate estimated income from water usage and crop income rate.
2. Calculate the farmer's bill.
3. Subtract the bill from the estimated income.

### 2.4 Reward System

1. The application generates a random reward percentage between 5% and 30%.
2. A reward of 25% or more is treated as a jackpot.

### 2.5 Configurable Prices

The operator can change:

1. Water rate.
2. Motor rate.
3. Crop income rate.

The updated rates are stored for future use.

### 2.6 Data Storage

1. Farmer records are stored in a file.
2. Price settings are stored in JSON format.
3. Data can be loaded again when the application starts.

### 2.7 Backup and Restore

The project supports:

1. Creating a backup of farmer data.
2. Restoring the main data.
3. Restoring data from the backup.

### 2.8 Testing

The tests check important parts of the application, including:

1. Data models.
2. Farmer registry.
3. Bill calculations.
4. Profit calculations.
5. Data storage.
6. Reward functionality.

## 3. Technologies and Python Modules Used

Python 3.8+         | Main programming language             
`dataclasses`       | Creating structured data models       
`pathlib`           | Working with file and directory paths 
`csv`               | Reading and writing farmer records    
`json`              | Storing price and settings data       
`os`                | File operations                       
`random`            | Generating random rewards             
`unittest`          | Testing application functionality     


## 4. How to Run

### 4.1 Prerequisites

Python 3.8 should be installed on your system.

Check the installed Python version:

```bash
python --version
```

### 4.2 Clone the Repository

```bash
git clone https://github.com/vivekraj-2108/Vityarthi_Project.git
```

Open the project folder:

```bash
cd Vityarthi_Project
```

### 4.3 Run the Application

```bash
python main.py
```

## 5. Application Menu

1 Add
2 View
3 Bill
4 Profit
5 Reward
6 Price
7 Backup
8 Restore
9 Exit


### 5.1 Add

Used to add a new farmer or update an existing farmer.

The application takes:

1. Farmer name.
2. Field name.
3. Crop name.
4. Water usage.
5. Motor hours.

### 5.2 View

Displays the registered farmers and their recorded information.

### 5.3 Bill

Calculates the bill based on water usage and motor usage.

### 5.4 Profit

Calculates the estimated profit for farmers.

### 5.5 Reward

Generates a random reward percentage.

### 5.6 Price

Allows the operator to update:

1. Water rate.
2. Motor rate.
3. Crop income rate.

### 5.7 Backup

Creates a backup of the current farmer data.

### 5.8 Restore

Restores previously saved farmer data.

## 6. How to Run Tests

Run the tests using:

```bash
python -m unittest -v
```

## 7. Learning Outcomes

The main things I learned are:

1. Writing Python programs using functions.
2. Applying Object-Oriented Programming concepts.
3. Working with files and stored data.
4. Using CSV and JSON.
5. Handling user input and validation.
6. Handling exceptions.
7. Creating backups and restoring data.
8. Writing and running unit tests.
9. Working with Python's standard library.
10. Building a complete console-based application.
