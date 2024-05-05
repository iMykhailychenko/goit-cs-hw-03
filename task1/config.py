from dotenv import dotenv_values

config = dotenv_values()  # take environment variables from .env.

USER_AMOUNT = 100
TASK_STATE_MAX = 3
TASKS_PER_USER = 2

POSTGRES_DB = config["POSTGRES_DB"]
POSTGRES_HOST = "localhost" # Change if runing inside docker container
POSTGRES_USER = config["POSTGRES_USER"]
POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"]