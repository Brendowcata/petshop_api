from datetime import date

def date_appointment_greater_today(date_initial):
    """Check if the date initial greater than or equal to today / Verifica se a data inicial é maior ou igual que hoje"""
    return date_initial >= date.today()
