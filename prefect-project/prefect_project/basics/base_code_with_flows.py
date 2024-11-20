import time
from prefect import flow, task

@task
def greet_user(name: str):
    time.sleep(2)
    return f"Hello, {name}!\n"    

@task
def provide_status_update(name: str):
    time.sleep(3)
    return f"{name}, your current status is: Active\n"

@task   
def fetch_account_balance(name: str):
    time.sleep(5)
    return f"{name}, your account balance is: $1,234.56\n"

@flow
def user_account_flow(user_name:str):
    # Tasks run one after the other (synchronous execution)
    greeting_task = greet_user.submit(user_name)
    status_task = provide_status_update.submit(user_name)
    balance_task = fetch_account_balance.submit(user_name)

    # Combine results sequentially
    final_message = greeting_task.result() + status_task.result() + balance_task.result()
    return final_message


if __name__ == "__main__":
    user_name = "Mor"
    final_message = user_account_flow(user_name)
    print(final_message)