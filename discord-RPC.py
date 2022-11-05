import time
import datetime
import os

# discord sdk moment
import discordsdk as sdk


def main():
    APPLICATION_ID = int(input("Application ID: "))

    app = sdk.Discord(APPLICATION_ID, sdk.CreateFlags.default)

    activity_manager = app.get_activity_manager()

    # set variables for discord rich presence
    activity = sdk.Activity()
    # set variables for discord rich presence
    # if a variable is blank, it will not be displayed



    ############################################################

    activity.state = input("Activity State: ")

    try:        # when set to try/except, you can put in empty values (it will ignore the errors)
        activity.party.size.current_size = int(input("Party Current Size: "))
    except:
        pass
    try:        # same as the last comment
        activity.party.size.max_size = int(input("Party Max Size: "))
    except:
        pass

    activity.secrets.join = "activity_secret"

    activity.party.id = input("Party ID: ")
    if activity.party.id == "":     # stops the invite function from screwing up
        activity.party.id = "123"

    activity.assets.large_image = input("Large Image Name: ")

    activity.assets.small_image = input("Small Image Name: ")

    ############################################################



    print("Please wait... (estimated 3-5 seconds)")

    def callback(result):
        if result == sdk.Result.ok:
            print("Successfully set the activity!")     # tell the users that the activity has been set
        else:
            raise Exception(result)

    activity_manager.update_activity(activity, callback)
    start = time.time()

    while 1:
        app.run_callbacks()
        time.sleep(0.1)
        currenttime = time.time()
        elapsedtime = currenttime-start
        formattedtime = time.strftime("%H:%M:%S", time.gmtime(elapsedtime))

        print(f"Time Elapse: {formattedtime}", flush=True, end="\r")


if __name__ == '__main__':      # in place to catch the KeyboardInterrupt exception
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting Application...")
        time.sleep(1.5)
        print("Have a good day! :)")
        time.sleep(0.5)
        os._exit(0)     # exits application using os module