import time
# importing the variables
from editables import APPLICATION_ID, activity_state, activity_party_size, activity_party_max_size, activity_secrets_join, activity_party_id, activity_large_image, activity_large_text, activity_small_image, activity_small_text

# discord sdk moment
import discordsdk as sdk

app = sdk.Discord(APPLICATION_ID, sdk.CreateFlags.default)

activity_manager = app.get_activity_manager()

# set variables for discord rich presence
activity = sdk.Activity()
# set variables for discord rich presence
# if a variable is blank, it will not be displayed
if activity_state != "":
    activity.state = activity_state


try:
    if activity_party_size != "":
        activity.party.size.current_size = activity_party_size
except:
    pass
try:
    if activity_party_max_size != "":
        activity.party.size.max_size = activity_party_max_size
except:
    pass

if activity_secrets_join != "":
    activity.secrets.join = activity_secrets_join
if activity_party_id != "":
    activity.party.id = activity_party_id
else:
    activity.party.id = "123"


if activity_large_image != "":
    activity.assets.large_image = activity_large_image
if activity_large_text != "":
    activity.assets.large_text = activity_large_text
if activity_small_image != "":
    activity.assets.small_image = activity_small_image
if activity_small_text != "":
    activity.assets.small_text = activity_small_text




def callback(result):
    if result == sdk.Result.ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)

activity_manager.update_activity(activity, callback)

while 1:
    app.run_callbacks()
    time.sleep(1)