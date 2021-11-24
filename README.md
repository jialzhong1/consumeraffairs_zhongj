Consumer Affairs The Eye Test Project

Jay Zhong (jialzhong@gmail.com)

I divided this project into 2 steps:

Step 1:

Create an endpoint where applications can request to update the The Eye's Event database by providing it with a list of JSON objects.  This is where the Event objects are created and to check and notify errors.

update_eye_data : This is the view that the applications will request and I am assuming that the those applications will off load their payload at specific times in order not overwhelm the database.  Just in case though, I made creating the Events atomic if there is somehow a concurrent request to this view.  If there are any errors present, the created Event models will be marked in their "has_errors" and a log will be recorded of those errors in real time. 

check_event_error:  This is a helper function that checks each event object and ensures that the categories and names are valid by checking the pair against a dictionary.  This validator can be much more extensive, but currently it's just a categories/name and timestamp check.  It returns a dictionary of the errors as well as the entire event for reporting.

Step 2:

Create another endpoint where the Event objects will be read and returned as JSON.

get_event_info:  The view that accepts session_id, category, start_time, and/or end_time to filter the Event objects and provides a JSON response.
