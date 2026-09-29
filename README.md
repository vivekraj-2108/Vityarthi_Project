# Farm Water Manager

A simple Python-based console application designed to manage irrigation usage for farmers. The project records water consumption and motor usage, calculates bills and estimated profit, manages configurable rates, and provides backup and restore functionality.

The main goal of this project is to demonstrate how Python can be used to build a practical real-world application using Python fundamentals, Object-Oriented Programming, file handling, data storage, validation, and testing.

## 1. Project Description

In a shared irrigation system, multiple farmers may use the same water source and motor. Manually calculating water usage, motor charges, and crop-related income can be time-consuming and error-prone.

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

The project includes unit tests using Python's built-in `unittest` framework.

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

The project uses Python's standard library and does not require external packages.

## 4. How to Run

### 4.1 Prerequisites

Python 3.8 or newer should be installed on your system.

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

The application will start in the terminal.

## 5. Application Menu

The application provides the following options:

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

### 5.9 Exit

Saves the current data and closes the application.

## 6. How to Run Tests

The project uses Python's built-in `unittest` framework.

Run the tests using:

```bash
python -m unittest -v
```

This runs the available test cases and displays their results in the terminal.

## 7. Python Topics Learned

Through this project, I learned and applied the following Python concepts:

### 7.1 Variables and Data Types

Used different Python data types to store and process application information.

### 7.2 Conditional Statements

Used `if`, `elif`, and `else` for decision-making and validation.

### 7.3 Loops

Used loops for menu execution and input validation.

### 7.4 Functions

Created functions for different operations such as:

1. Taking user input.
2. Calculating bills.
3. Calculating profit.
4. Saving data.
5. Loading data.
6. Generating rewards.

### 7.5 Object-Oriented Programming

Used classes to represent different parts of the application, including farmers, prices, and the farmer registry.

### 7.6 Dataclasses

Used Python's `@dataclass` to create structured data objects.

### 7.7 Properties

Used `@property` for controlled access to object data.

### 7.8 Class Methods

Used `@classmethod` for creating objects from stored data.

### 7.9 Exception Handling

Used `try` and `except` to handle invalid input and file-related errors.

### 7.10 File Handling

Learned how to:

1. Read data from files.
2. Write data to files.
3. Create directories.
4. Work with file paths.
5. Create and restore backups.

### 7.11 CSV

Used the `csv` module to store and retrieve farmer records.

### 7.12 JSON

Used the `json` module to store price and configuration data.

### 7.13 Modules and Imports

Learned how to use Python modules and import required functionality between files.

### 7.14 Random Module

Used the `random` module to generate reward percentages.

### 7.15 Unit Testing

Used Python's `unittest` framework to test different parts of the application.

### 7.16 Input Validation

Implemented validation for:

1. Empty input.
2. Invalid menu choices.
3. Invalid numerical values.
4. Negative values.
5. Invalid stored data.

## 8. Learning Outcomes

Through this project, I learned how to build a complete Python application for a real-world problem.

The main things I learned are:

1. Writing Python programs using functions and classes.
2. Applying Object-Oriented Programming concepts.
3. Working with files and stored data.
4. Using CSV and JSON.
5. Handling user input and validation.
6. Handling exceptions.
7. Creating backups and restoring data.
8. Writing and running unit tests.
9. Working with Python's standard library.
10. Building a complete console-based application.
