import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def endpoint(request):
    """The endpoint takes two GET request query parameters
        and return specific information in JSON format.
    """
    # Get the GET parameters slack_name and track
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    
    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get the current UTC time with validation of +/-2 minutes
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Construct GitHub URLs
    github_repo_url = "https://github.com/hendrixxD/HNGx/tree/main"
    github_file_url = f"{github_repo_url}/blob/main/HNG_1/README.md"
                        
    
    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": "200"
    }

    return JsonResponse(response_data)