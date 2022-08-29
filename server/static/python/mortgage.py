from pyscript import Element

payment_amount = Element("payment-amount")

def calculate_payment(principal: float, months: int, interest_rate: float):
    R = 1 + (interest_rate / 100 / 12)
    return principal * (R ** months) * ((1 - R) / (1 - R ** months))

def calculate_btn_click_handler(evt):
    payment_amount.element.innerText = "0.00"