import psycopg2

DATABASE_URL = "postgresql://crrae:crrae_umoa@postgresql-34636-0.cloudclusters.net:34636/crrae_umoa?sslmode=require"

def load_accounts_db():
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, email, balance FROM accounts ORDER BY id"
            )
            return cursor.fetchall()

def update_account_db(account_id, name, email, balance):
    # Version de l'apprenant B
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE accounts SET balance = %s, name = %s, email = %s WHERE id = %s",  # Il change l'ordre
                (balance or 0, name, email, account_id)
            )
            conn.commit()
