from login import login
from liker import explore_liker
from dotenv import load_dotenv
from selenium_func import close_window
import os

load_dotenv()

######################
# Settings variables
######################

username = os.environ.get('USER')
password = os.environ.get('PASSWORD')

###################
# Start routine
###################

# Login step
login(username, password)

# Start liking session for n° times
explore_liker(500)

close_window()
