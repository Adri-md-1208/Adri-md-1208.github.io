from dotenv import dotenv_values

secrets = dotenv_values("/home/adrian/GitHub/Adri-md-1208.github.io/.env")

db_user: str = secrets["DB_USER"]
db_password: str = secrets["DB_PASSWORD"]
db_host: str = secrets["DB_HOST"]
db_port: str = secrets["DB_PORT"]
db_name: str = secrets["DB_NAME"]
