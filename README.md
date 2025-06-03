# Number Guessing Game

This is a simple number guessing game built using Python and Tailwind CSS. The application allows users to guess a randomly generated number between 1 and 100. The user interface is designed to be visually appealing and user-friendly.

## Features

- User-friendly GUI
- Random number generation for guessing
- Feedback on user guesses (too high, too low, correct)
- Input field that clears feedback when clicked

## Project Structure

```
number-guessing-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui.py           # GUI setup and interaction logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd number-guessing-app
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Once the application is running, you can input your guess in the provided input field. Press the Enter key to submit your guess. The application will provide feedback on whether your guess is too high, too low, or correct. Clicking on the input field will clear any previous feedback.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.