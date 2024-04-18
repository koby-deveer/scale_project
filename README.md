# Industrial Scale Data Management System

This repository contains the software for managing and processing weigh-in and weigh-out data from industrial scales used in logistics or manufacturing settings. The system automates the capture, processing, and logging of scale data, enhancing accuracy, efficiency, and traceability in industrial operations.

## Key Components

### Scale Communication
- Manages serial communication with an industrial scale.
- Ensures accurate and efficient data reception.

### Data Processing
- Analyzes and processes raw data to differentiate between weigh-in and weigh-out events.
- Extracts and formats relevant information for storage and printing.

### Database Operations
- Stores processed data in a SQL database, facilitating easy management and retrieval.

### Printer Connectivity
- Enables sending formatted data directly to a printer for record-keeping.

### Logging System
- Implements informational and error logging for system monitoring and troubleshooting.

## System Operations

- **Initialization**: Establishes a connection to the scale and initializes data streams.
- **Data Handling**: Continuously reads data from the scale, processing it according to predefined criteria.
- **Logging and Storage**: Captures and logs data and errors into separate log files. Stores data in a MySQL database.

## Technologies Used

- **Python**: For overall programming due to its support for serial communication, data processing, and database operations.
- **MySQL**: Used for robust data management capabilities.
- **Serial Communication**: Handles real-time data transmission between the scale and the system.
- **Logging**: Utilizes Python’s built-in `logging` library.

## Objectives and Benefits

- **Automation**: Reduces manual entry errors, increasing operational efficiency.
- **Accuracy**: Ensures precise data capture, critical for weight measurements.
- **Traceability**: Enhances tracking capabilities and compliance with regulations.
- **Maintainability**: Designed for ease of maintenance and future upgrades.

## Installation

```bash
git clone https://github.com/yourusername/industrial-scale-management.git
cd industrial-scale-management
pip install -r requirements.txt
```

## Usage

Run the main program:

```python
python main.py
```

Ensure you configure your system's serial ports and database credentials before running the application.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
