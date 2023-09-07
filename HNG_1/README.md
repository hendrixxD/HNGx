# HNG-Internship-Task1
## Create and host and endpoint

Create and host an endpoint using any programming language of your choice.
The endpoint should take two GET request query parameters and return specific information in JSON format.
Requirements
The information required includes:
 - Slack name
 - Current day of the week
 - Current UTC time (with validation of +/-2)
 - Track
 - The GitHub URL of the file being run
 - The GitHub URL of the full source code.
 - A  Status Code of Success

 **JSON**
 ```
 {
   "slack_name": "example_name",
   "current_day": "Monday",
   "utc_time": "2023-08-21T15:04:05Z",
   "track": "backend",
   "github_file_url": []("https://github.com/username/repo/blob/main/file_name.ext"),
   "github_repo_url": []("https://github.com/username/repo"),
   “status_code”: 200
 }
```
 
 ### Acceptance Criteria
 1. Endpoint Creation: Provide a publicly accessible endpoint.
 2. GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.
       E.g.: [](http://example.com/api?slack_name=example_name&track=backend).
 3. Slack Name: The response should include the slack_name passed as a GET request query parameter.
 4. Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).
 5. Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.
 6. Track: The response should display the track of the you signed up for (Backend). This will be based on the track GET parameter passed to the endpoint.
 7. GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.
 8. GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.
 9. Status Code: Return *200* as Integer.
 10. JSON Format: The endpoint's response should adhere to the specified JSON format.
 11. Testing: Before submission:
 12. Ensure the endpoint is accessible.
 13. Check the returned JSON against the defined format.
 14. Validate the correctness of each data point in the JSON response.
