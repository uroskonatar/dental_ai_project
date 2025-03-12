from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta

# Path to the credentials file
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# Authenticate with Google Calendar API
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=creds)

# Replace these with the actual Google Calendar emails for each doctor
DOCTOR_CALENDARS = {
    "Dr. Ninoslav Konatar": "uroskonatar37@gmail.com",
    "Dr. Natalija Konatar": "uroskonatar37@gmail.com",
    "Dr. Tijana Miljenovic": "uroskonatar37@gmail.com"
}

def get_available_slots(doctor_name, days_ahead=7):
    """Fetches available appointment slots for a doctor from Google Calendar."""
    
    print(f"Fetching availability for {doctor_name}...")  # Debugging

    calendar_id = DOCTOR_CALENDARS.get(doctor_name)
    if not calendar_id:
        return {"error": f"No calendar found for {doctor_name}"}

    now = datetime.now(tz=timezone.utc).isoformat()
    future = (datetime.now(tz=timezone.utc) + timedelta(days=days_ahead)).isoformat()


    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        timeMax=future,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    booked_slots = [event["start"].get("dateTime", event["start"].get("date")) for event in events_result.get("items", [])]

    return {"doctor": doctor_name, "booked_slots": booked_slots}

print("Script is running...")  # Debugging message
print(get_available_slots("Dr. Ninoslav Konatar"))  # Make sure a doctor exists


