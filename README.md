# Ethereum Explorer Web App

This is a Django + Python-based web application that allows users to fetch the current balance and five recent transactions associated with a given Ethereum address.
## Installation

To run the Ethereum Explorer web app locally, follow these steps:

1. Clone the repository:

   ```
   git clone  $ https://github.com/devumang096/Ethereum-App.git
   ```

2. Navigate to the project directory:

   ```
   cd Ethereum-App
   ```

3. Create and activate a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Set up the Ethereum Explorer app:

   - Open the `ethereum_app/settings.py` file.
   - Update the `SECRET_KEY` with your own secret key.
   - Make sure the `DEBUG` setting is set to `True` for local development.

6. Apply database migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```
![App](https://github.com/devumang096/Ethereum-App/blob/master/img.jpg?raw=true)
8. Open your web browser and visit `http://localhost:8000` to access the Ethereum Explorer web app.

## Usage

1. On the Ethereum Explorer home page, you will see a text field and a "Fetch" button.
2. Enter the Ethereum address you want to explore in the text field.
3. Click the "Fetch" button.
4. The current balance and five most recent transactions associated with the provided Ethereum address will be displayed.



## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.



## Credits

The Ethereum Explorer web app was developed by Umang Devanshu as a project.
