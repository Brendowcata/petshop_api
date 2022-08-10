from datetime import date

def pay_day_greater_or_equal_today(pay_day):
    """Check if the date initial greater than or equal to today / Verifica se a data inicial é maior ou igual que hoje"""
    return pay_day >= date.today()

def is_value_money_positive(value_money):
    """Check if the value is positive / Verifica se o valor é positivo"""
    return value_money >= 0

def is_amount_paid_positive(amount_paid):
    """Check if the value is positive / Verifica se o valor é positivo"""
    return amount_paid >= 0