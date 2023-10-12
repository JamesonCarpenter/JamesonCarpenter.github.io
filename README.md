# CMSC447_Individual_Jameson_Carpenter
Prerequisites
  1. Python and pip must be installed on your host computer.
      - I used the windows installer (64-bit) from python's website, pip is included: https://www.python.org/downloads/release/python-3120/
  2. Create a virtual environment with pip.
     - Pip should have it available already, just use command: **python -m pip install --user virtualenv**
      - **Make sure you are create the virtual environment in the same folder as where the rest of the code is.**
     - Now run: **virtualenv env_name**
        - Pick any name for env_name but don't forget
     - Now run: **env_name\Scripts\activate**
        - This is for windows, and will start the virtual environment.
  3. While in virtual environment, install requirements.
     - Now that we are in the virtual environment, run this command: **pip install -r requirements.txt**
      - This will ensure Flask and psycopg2 are installed which are neccessary for running this program.
  4. Run the program.
     - From the virtual environment, while in the same directory as where "app_final.py" is; execute this command: **python app_final.py**
     - This command will create the create the webpage, locally hosted to your computer.
    - Now just enter the url that the terminal says into a web browser, for myself the domain is "http://127.0.0.1:5000".
  5. Interact with the UI!
     - All setup should be done and now my assignment is visible.

Frontend Usage
  - All frontend is done with HTML some CSS.

Backend Usage
  - Backend was made using Python and PostgreSQL. PostgreSQL is the only thing not stored natively to the github, it is online and accessible to anyone if they have the connection.
  - I learned in the later stages of development that PostgreSQL must be stored somewhere online in order for someone other than myself to access it. I'm using an ElephantSQL database to allow that.

If there any other questions about running this program, please contact me at jcarpen2@umbc.edu. I will attempt to respond to any inquiries in a timely manner.
