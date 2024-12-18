import time

def greet_user(name: str):
    return f"Hello, {name}!\n"    

def provide_status_update(name: str):
    return f"{name}, your current status is: Active\n"
    
def fetch_account_balance(name: str):
    return f"{name}, your account balance is: $1,234.56\n"

def user_account_flow(user_name:str):
    # Tasks run one after the other (synchronous execution)
    greeting_task = greet_user(user_name)
    status_task = provide_status_update(user_name)
    balance_task = fetch_account_balance(user_name)

    # Combine results sequentially
    final_message = greeting_task + status_task + balance_task
    return final_message


if __name__ == "__main__":
    user_name = "Mor"
    final_message = user_account_flow(user_name)
    print(final_message)