**Quick Recipe Chatbot**

**Overview**
The Quick Recipe Chatbot is a web-based application that helps users quickly find recipes based on the ingredients they have available. The chatbot takes user input in the form of ingredients or dish names and provides a list of recipes with preparation steps. The chatbot’s intuitive interface makes it easy for users to interact and receive recipe suggestions in real-time.

This project uses Python with Flask for the backend, handling the logic for fetching recipe data and serving it to users. The frontend is built using HTML, CSS, and JavaScript to deliver a responsive, clean, and user-friendly chat interface.

**Features**
Ingredient-Based Recipe Search: Users can input ingredients, and the chatbot provides recipes that match those ingredients.
Interactive Chat Interface: The chatbot allows users to interact with it in a conversational manner, offering a seamless and engaging experience.
Recipe Suggestions with Steps: Each recipe includes a list of ingredients and step-by-step instructions.
Responsive Design: The interface is designed to be mobile-friendly, ensuring accessibility on all devices.
Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Hosting: The application can be hosted on platforms like Heroku or any other cloud service supporting Flask apps.
**Installation**
To run this project locally, follow the steps below:

Clone the repository:

bash

git clone https://github.com/yourusername/Quick_Recipe_chatbot.git
cd Quick_Recipe_chatbot
Install required dependencies: Create a virtual environment and activate it (optional but recommended).

bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies from requirements.txt:

bash

pip install -r requirements.txt
Run the Flask app:

bash

python chatbot.py
Access the app: Open your browser and visit http://127.0.0.1:5000/ to use the chatbot.

**Files in this Repository**
chatbot.py: The backend Flask application that handles the chatbot logic and recipe fetching.
index.html: The main HTML page that contains the user interface for the chatbot.
procfile.txt: The file required for deployment on platforms like Heroku, specifying the command to run the Flask app.
requirements.txt: A list of Python dependencies for the project.
runtime.txt: Specifies the Python version to be used when deploying the app.
