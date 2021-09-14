db = {
    'user': 'admin',
    'password': 'test387295',
    'host': 'python-backend-test.ckabupwj6ebu.ap-northeast-2.rds.amazonaws.com',
    'port': 3306,
    'database': 'miniter'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
JWT_SECRET_KEY = 'SOME_SUPER_SECRET_KEY'

config = {
    'DB_URL': f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8",
    'JWT_SECRET_KEY': 'SOME_SUPER_SECRET_KEY'
}

test_db = {
    'user': 'test',
    'password': 'test123',
    'host': 'localhost',
    'port': 13306,
    'database': 'test_db'
}

test_config = {
    'DB_URL': f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
    'JWT_SECRET_KEY': 'SOME_SUPER_SECRET_KEY'
}
