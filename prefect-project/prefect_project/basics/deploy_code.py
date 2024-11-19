import time
from prefect import task, flow

@task
def greet_user(name: str):
    return f"Hello, {name}!\n"    

@task
def provide_status_update(name: str):
    return f"{name}, your current status is: Active\n"

@task   
def fetch_account_balance(name: str):
    return f"{name}, your account balance is: $1,234.56\n"

@flow
def main_flow(user_name:str="Mor"):
    # Tasks run one after the other (synchronous execution)
    greeting_task = greet_user(user_name)
    status_task = provide_status_update(user_name)
    balance_task = fetch_account_balance(user_name)

    # Combine results sequentially
    final_message = greeting_task + status_task + balance_task
    return final_message


if __name__ == "__main__":
    main.from_source(
        source="https://github.com/zzstoatzz/yt.git",
        entrypoint="new-prefect-project/main.py:main",
    ).deploy(name="My First Deployment", work_pool_name="docker-work")
