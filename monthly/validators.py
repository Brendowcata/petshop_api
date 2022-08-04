from datetime import date

def date_initial_smaller_date_final(date_initial, date_final):
    """Check if the date initial less than date final / Verifica se o tempo inicial é menor que o tempo final"""
    return date_initial < date_final

def date_initial_greater_today(date_initial):
    """Check if the date initial greater than or equal to today / Verifica se a data inicial é maior ou igual que hoje"""
    return date_initial >= date.today()

def value_money_isPositive(value_money):
    """Check if the value is positive / Verifica se o valor é positivo"""
    return value_money >= 0

def amount_paid_isPositive(amount_paid):
    """Check if the value is positive / Verifica se o valor é positivo"""
    return amount_paid >= 0
