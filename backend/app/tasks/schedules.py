from tasks.celery_config import celery_app

celery_app.conf.beat_schedule = {
    "daily-8am-notification": {
        "task": "app.tasks.schedules.send_morning_report",
        "schedule": 8.0,  # Ou via crontab
    },
}


@celery_app.task
def send_morning_report():
    print("Envoi automatique des rapports à 8h !")
