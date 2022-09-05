from pyscript import Element

principal_in = Element("principal")
rate_in = Element("rate")
months_in = Element("months")
payment_amount = Element("payment-amount")

def calculate_payment(principal: float, interest_rate: float, months: int):
    R = 1 + (interest_rate / 100 / 12)
    return principal * (R ** months) * ((1 - R) / (1 - R ** months))

def is_valid(input: Element):
    val = input.element.value
    try:
        n = float(val)
        if n > 0:
            # remove any style overrides
            input.element.style = ""
            return True
    except ValueError:
        # fall through if conversion failed
        pass
    input.element.style = "background-color:lightpink"
    return False

def calculate_btn_click_handler(evt):
    valid_state = (is_valid(principal_in), is_valid(rate_in), is_valid(months_in))
    if all(valid_state):
        P = float(principal_in.element.value)
        r = float(rate_in.element.value)
        m = int(months_in.element.value)
        amount = calculate_payment(P, r, m)
        payment_amount.element.innerText = f"{amount:,.2f}"
    else:
        payment_amount.element.innerText = "Invalid Input"
