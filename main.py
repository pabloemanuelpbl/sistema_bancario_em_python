from operator import itemgetter

currentAccount: dict = {                 ##conta corrente do usuario
    'depositStatement': [],
    'withdrawalStatement': [],
    'totalBalance': 0.0
}
LIMIT_OF_DAILY_WITHDRAWALS: int = 3      ##limite de saques diarios
LIMIT_PRICE_PER_WITHDRAWAL: float = 500.0    ##limite em reais por saque

def accountWithDraw(account: dict, *values) -> dict:
    value: float = values[0]
    if(len(account["withdrawalStatement"]) >= LIMIT_OF_DAILY_WITHDRAWALS): 
        message = "\n[!] The operation failed! Maximum number of withdrawals exceeded."   
        return {"performRecursion": False, "message": message}    ##apos o limite ser exedido nao existe necessidade reexecutar
    
    if(value > LIMIT_PRICE_PER_WITHDRAWAL): 
        message = "\n[!] The operation failed! The limit amount per withdrawal is R$500"
        return {"performRecursion": True, "message": message}
    
    if(value > account["totalBalance"]):
        message = "\n[!] The operation failed! Required amount is unavailable in the account"
        return {"performRecursion": True, "message": message}

    account["withdrawalStatement"].append(value)
    account["totalBalance"] -= value
    message = f"I pulled out R${value:.2f}"
    return {"performRecursion": False, "message": message}

def accountDeposit(account: dict, *values) -> dict:
    value: float = values[0]
    account["depositStatement"].append(value)
    account["totalBalance"] += value
    message = f"You have deposited: R${value:.2f}"
    return {"performRecursion": False, "message": message}

def accountView(account: dict, *values) -> dict:
    deposit, withdrawal, total = itemgetter("depositStatement", "withdrawalStatement", "totalBalance")(account)
    def convertArrayToString(array: list):
        stringResult = "\n    ".join(map(lambda x: f"R${x:.2f}" , array))
        return stringResult
        
    message = f"""
    -----------------extract------------------
    --- deposit --
    {"no deposit was made" if len(deposit) == 0 else convertArrayToString(deposit)}
   
    --- withdrawals --
    {"no withdrawals were made" if len(withdrawal) == 0 else  convertArrayToString(withdrawal)}
    
    total = R${total:.2f}

    -----------------  end  ------------------
    """
    return {"performRecursion": False, "message": message}


def selectASpecificOperation(operation: str) -> dict:
    match operation:
        case "Deposit"|"deposit"|"D"|"d":
            return {
                "run": accountDeposit,
                "status": "deposit",
                "message": "choose the amount: "
            }
        case "WithDraw"|"withDraw"|"W"|"w":
            return {
                "run": accountWithDraw,
                "status": "withDraw",
                "message": "choose the amount: "
            }
        case "Extract"|"extract"|"E"|"e":
            return {
                "run": accountView,
                "status": "view",
                "message": "see extract: "
            }
        case "Exit"|"exit"|"Quit"|"quit"|"Q"|"q":
            return {
                "run": None,
                "status": "quit",
                "message": "closing!"
            }
        case _:
            return {
                "run": None,
                "status": "invalid",
                "message": "Invalid operation! please try again"
            }


def userInput() -> None:
    initialInput = """
    [d] Deposit
    [w] To Withdraw
    [e] Extract
    [q] Exit
    \n"""
    inputComand: str = input(initialInput)
    operation: dict = selectASpecificOperation(inputComand)
    run, status, message = itemgetter("run", "status", "message")(operation)
    if(status == "quit"):
        print(message)
        return 

    if(status == "invalid"):
        print(message)
        userInput()
        return
    
    if(status == "view"):
        print(message)
        response: dict = run(currentAccount)
        print(response["message"])
        userInput()
        return
    
    def performOperations() -> None:
        try:
            value: float = float(input(message))
            if(value < 0.0):      
                print("only positive values! try again")
                performOperations()
                return
            ## caso de necessidade, a funcao ira ser reexecutada
            response: dict = run(currentAccount, value)
            print(response["message"])
            if (response["performRecursion"]): performOperations()
        except ValueError:
            print("=> ValueError: not a valid number")
            performOperations()
        except:
            print("=> error: please try again")
            performOperations()
    
    performOperations()
    userInput()     ##main looping 
    return

userInput()