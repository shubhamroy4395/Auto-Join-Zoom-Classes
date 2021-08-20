import schedule
import time
import webbrowser

# this opens up chrome with the meeting link
def open_link_chrome(link):
    webbrowser.open(link)

def ome_meeting():
    print("Opening Class")
    open_link_chrome('Your meeting link here') #enter your meeting link here


ome = schedule.every().friday.at("12:15").do(ome_meeting) #enter the day and time you want to open up your meetings
while 1:
    schedule.run_pending()
    time.sleep(1)