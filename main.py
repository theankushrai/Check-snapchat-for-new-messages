from imports import *

def send_notification(text):
    
    #check if there is a new chat
    if(text.find('New Chat')==-1): return

    #cleaning data
    text=emoji.replace_emoji(text,' ') #replacing all the emojis
    text=re.split("New Chat",text)
    text=text[:-1] #removing last li because its not required

    message=""
    for it in text:
        it=it.split(' ')[-2:] #name of a person
        name=' '.join(it) #join the name back
        message+=name+" sent a new message !!\n"
        
    
    notification.notify( #notification from plyer
                title="Message Reminder",
                message=message,
                app_name="Social Media Notifier",
                timeout=60  # Duration the notification stays on the screen (in seconds)
        )
def check_for_new_messages():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.minimize_window()

    # Navigate to your desired URL (e.g., Snapchat login page)
    driver.get('https://web.snapchat.com/')
    time.sleep(10)
    html_content = driver.page_source
    with open('snapchat.html', "w", encoding='utf-8') as html_file:
        html_file.write(html_content)

    # Re-open the HTML file for reading
    with open('snapchat.html', 'r', encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    text=soup.get_text()
    send_notification(text)
    driver.quit()

print("******************** Script Started ********************\n")

CHECK_EVERY_X_HOURS=int(input("Please enter the frequency (in hours) at which you would like this script to run : "))

# Load environment variables from .env file
load_dotenv()
user_data_dir = os.getenv('USER_DATA_DIR')

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Use existing user profile
chrome_options.add_argument(r"profile-directory=Default")  # You can also specify other profile directories

#ensuring max runtime is 8 hours
for _ in range(8//CHECK_EVERY_X_HOURS):
    check_for_new_messages()
    time.sleep(CHECK_EVERY_X_HOURS*60*60)

print("******************** Script Completed ********************\n")
