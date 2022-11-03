import time
#importing the variables

#discord sdk moment
import discordsdk as sdk


APPLICATION_ID = int(input("Application ID: "))

app = sdk.Discord(APPLICATION_ID, sdk.CreateFlags.default)

activity_manager = app.get_activity_manager()

#set variables for discord rich presence
activity = sdk.Activity()
#set variables for discord rich presence
#if a variable is blank, it will not be displayed

activity.state = input("Activity State: ")



activity.party.size.current_size = int(input("Party Current Size: "))

activity.party.size.max_size = int(input("Party Max Size: "))

activity.secrets.join = "activity_secret"

activity.party.id = input("Party ID: ")


activity.assets.large_image = input("Large Image Name: ")

activity.assets.small_image = input("Small Image Name: ")

print("Please wait... (estimated 3 seconds)")


def callback(result):
    if result == sdk.Result.ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)

activity_manager.update_activity(activity, callback)

while 1:
    app.run_callbacks()
    time.sleep(1)