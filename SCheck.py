STATES = ["Standby",
          "Refill",
          "Menu",
          "Order",
          "p1",
          "Quantity",
          "Check",
          "Confirm",
          "Cart",
          "pay",
          "payF",
          "payW",
          "ClearCart",
          "Reduce",
          "Eject"]


def done(state):
    if state == 0:
        print("Accepted")
    else:
        print("Not Accepted")


def halt():
    print("program halted, Not Accepted")


def check():
    cur_state = 0
    inp_str = input()
    for inp in inp_str:
        if STATES[cur_state] == "Standby":
            if inp == "a":
                cur_state = STATES.index("Menu")
            elif inp == "b":
                cur_state = STATES.index("Refill")
            else:
                halt()
                break

        elif STATES[cur_state] == "Refill":
            if inp == "a":
                cur_state = STATES.index("Standby")
            else:
                halt()
                break

        elif STATES[cur_state] == "Menu":
            if inp == "a":
                cur_state = STATES.index("Order")
            else:
                halt()
                break

        elif STATES[cur_state] == "Order":
            if inp == "a" or inp == "b" or inp == "c" or inp == "d" or inp == "e":
                cur_state = STATES.index("p1")
            else:
                halt()
                break

        elif STATES[cur_state] == "p1":
            if inp == "a" or inp == "b" or inp == "c" or inp == "d" or inp == "e":
                cur_state = STATES.index("Quantity")
            else:
                halt()
                break

        elif STATES[cur_state] == "Quantity":
            if inp == "a":
                cur_state = STATES.index("Check")
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
            else:
                halt()
                break

        elif STATES[cur_state] == "ClearCart":
            if inp == "f":
                cur_state = STATES.index("Menu")
            else:
                halt()
                break

        elif STATES[cur_state] == "Check":
            if inp == "a":
                cur_state = STATES.index("Cart")
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
            elif inp == "0":
                done(cur_state)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Cart":
            if inp == "a":
                cur_state = STATES.index("pay")
            elif inp == "b":
                cur_state = STATES.index("Order")
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
            else:
                halt()
                break

        elif STATES[cur_state] == "pay":
            if inp == "a":
                cur_state = STATES.index("payW")
            elif inp == "e":
                cur_state = STATES.index("payF")
            else:
                halt()
                break

        elif STATES[cur_state] == "payF":
            if inp == "d":
                cur_state = STATES.index("ClearCart")
            else:
                halt()
                break

        elif STATES[cur_state] == "payW":
            if inp == "a":
                cur_state = STATES.index("Eject")
            else:
                halt()
                break

        elif STATES[cur_state] == "Eject":
            if inp == "a":
                cur_state = STATES.index("Standby")
            else:
                halt()
                break

    done(cur_state)
