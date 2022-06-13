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


def done(state, string):
    if state == 0:
        print("Accepted %s" % string)
    else:
        print("Not Accepted %s" % string)


def halt():
    print("program halted")


def main():
    cur_state = 0
    print("please enter 0 to stop the input")
    inp_so_far = ""
    while True:
        if STATES[cur_state] == "Standby":
            inp = input("[a]. Menu\n [b]. refill vendor")
            if inp == "a":
                cur_state = STATES.index("Menu")
                inp_so_far = inp_so_far + inp
            elif inp == "b":
                cur_state = STATES.index("refill")
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Refill":
            inp = input("[a]. Refill Done")
            if inp == "a":
                cur_state = STATES.index("Standby")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Menu":
            inp = input("[a]. Order")
            if inp == "a":
                cur_state = STATES.index("Order")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Order":
            inp = input("[aa]. Product 1\n[bb]. Product 2\n[cc]. Product 3\n[dd]. Product 4\n[ee]. Product 5\n")
            if inp == "aa" or inp == "bb" or inp == "cc" or inp == "dd" or inp == "ee":
                cur_state = STATES.index("Quantity")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Quantity":
            inp = input("[a]. Check\n [d]. Cancel")
            if inp == "a":
                cur_state = STATES.index("Check")
                inp_so_far = inp_so_far + inp
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "ClearCart":
            inp = input("[f]. Return to Menu")
            if inp == "f":
                cur_state = STATES.index("Menu")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Check":
            inp = input("[a]. Proceed\n[d]. Cancel")
            if inp == "a":
                cur_state = STATES.index("Confirm")
                inp_so_far = inp_so_far + inp
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Confirm":
            inp = input("[a]. Confirm\n[b]. Add Product\n[d]. Cancel")
            if inp == "a":
                cur_state = STATES.index("Cart")
                inp_so_far = inp_so_far + inp
            elif inp == "b":
                cur_state = STATES.index("Order")
                inp_so_far = inp_so_far + inp
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "Cart":
            inp = input("[a]. Pay\n[b]. Add Product\n[d]. Cancel")
            if inp == "a":
                cur_state = STATES.index("pay")
                inp_so_far = inp_so_far + inp
            elif inp == "b":
                cur_state = STATES.index("Order")
                inp_so_far = inp_so_far + inp
            elif inp == "d":
                cur_state = STATES.index("ClearCart")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "pay":
            inp = input("[a]. Payment Successful\n[e]. Payment Failed")
            if inp == "a":
                cur_state = STATES.index("payW")
                inp_so_far = inp_so_far + inp
            elif inp == "e":
                cur_state = STATES.index("payF")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "payF":
            inp = input("Payment failed.\n [d]. Cancel Order")
            if inp == "d":
                cur_state = STATES.index("ClearCart")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break

        elif STATES[cur_state] == "payW":
            inp = input("[aaa]. Eject Product")
            if inp == "aaa":
                cur_state = STATES.index("Standby")
                inp_so_far = inp_so_far + inp
            elif inp == "0":
                done(cur_state, inp_so_far)
                break
            else:
                halt()
                break


if __name__ == "__main__":
    main()
