import google.auth
from googleapiclient.discovery import build

# Configurar a autenticação
credentials, project = google.auth.default()
calendar_api_version = 'v3'

# Inicializar o objeto service
service = build('calendar', calendar_api_version, credentials=credentials)

event = {
    'summary': 'Google I/O 2023',
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'Uma oportunidade de saber mais sobre os produtos para desenvolvedores do Google.',
    'start': {
        'dateTime': '2023-07-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2023-07-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
    ],
    'attendees': [
        {'email': 'danielsouzanovo@gmail.com'},
        {'email': 'danielsouzanovo@gmail.com'},
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
        ],
    },
}

# Criar o evento no calendário
event = service.events().insert(calendarId='danielsouzanovo@gmail.com', body=event).execute()
print('Evento criado: %s' % (event.get('htmlLink')))
