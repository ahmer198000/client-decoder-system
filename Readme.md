Project Setup Instructions

1. Install the Required Packages

First, set up your virtual environment and install the required dependencies.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

2. Running the Script to Add Decoders

To add decoders to the database, you can run the add_decoders.py script.

# Run the script to insert decoders into the database
python add_decoders.py

3. Database Migrations

To handle database migrations, follow these steps:

1. Generate a Migration:

   flask db migrate -m "Migration message"

2. Apply the Migration (Upgrade):

   flask db upgrade

4. Running the Flask Application

To run the Flask application locally, use the following command:

flask run

By default, the app will be accessible at http://127.0.0.1:5000/.

Additional Flask Commands

- Run the Flask Shell (for manual database queries and interactions):

   flask shell

- Reset the Database (if needed, for a fresh start):

   flask db downgrade
   flask db upgrade
