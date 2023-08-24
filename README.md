# Scale Data Recording Project

This project involves reading data from a weighing scale connected to the computer's COM6 port and recording the data in an Excel workbook. The Python script utilizes the `serial` and `openpyxl` libraries for communication with the scale and manipulation of the Excel workbook, respectively. thus, automating data collection of the Haul Road Scale.



## Setup and Configuration

1. Connect the weighing scale to the computer's COM6 port.
2. Ensure that Python is installed on your system along with the required libraries (`serial`, `openpyxl`).

## Code Overview

The provided Python script performs the following tasks:

1. **Serial Port Configuration**: The script sets up a serial connection (`ConnectScale`) to the COM6 port at a baud rate of 9600 with a timeout of 100 seconds.

2. **Excel Workbook Initialization**: The script opens an Excel workbook (`Scale_Data.xlsx`) located at `C:\Users\Kody\Desktop\VALCO\Valco\Scale\Scale project\`. It accesses the active sheet (`DataSheet`) for data recording.

3. **Iterating Over Rows**: The script iterates through the rows of the Excel sheet to find the most recently filled row and extracts its index. This index will be used to determine where new data should be added.

4. **Data Retrieval and Processing Loop**: The script enters a loop that continuously reads data from the scale's COM6 port as long as the port is open. It reads the incoming data (up to 60 characters) and decodes it.

5. **Data Extraction**: If the received data length is above a certain threshold (50 characters), the script extracts relevant information such as ID, Weight, Time, and Date from the received data. These values are then processed further.

6. **Data Recording in Excel**: The extracted data (ID, Weight, Time, and Date) are added to a list (`ExData`). The script uses a loop to iterate through the list and add the data to a new row in the Excel sheet.

7. **Saving Excel Data**: After data is added to the Excel sheet, the workbook is saved to persist the changes.

8. **Buffer Management**: The script clears the input buffer of the serial connection to remove any residual data.

9. **Loop Termination**: The loop continues until the serial port is open. Once the loop terminates, the serial connection to the scale and the Excel workbook are closed.

## Usage

1. Make sure the scale is properly connected to COM6 port.
2. Run the provided Python script.
3. The script will continuously read data from the scale and record it in the Excel workbook.

Note: Adjust file paths, COM port, and other configurations as necessary for your specific setup.

## Dependencies

- Python (>=3.x)
- `serial` library (for serial communication)
- `openpyxl` library (for working with Excel files)

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: This description is based on the provided code snippet and assumes the accuracy of the code's functionality as described. Additional context or code details not included in the provided snippet could influence the actual project behavior.
