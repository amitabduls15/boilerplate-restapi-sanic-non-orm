# boilerplate-restapi-sanic-non-orm

Repo ini dibuat sebagai stater kit untuk membuat restapi 
dengan sanic dan koneksi database PostgreSQL tanpa ORM.

# Usage
```commandline
python main.py
```

# Configs
contoh config disimpan dalam file *example.env*, 
sebelum menjalankan *main.py*.
```bash
cp example.env .env
```
berikut adalah detail config yang tersedia.

| No  | key                 | type    | default    |
|-----|---------------------|---------|------------|
| 1   | POSTGRESQL_PORT     | integer | 5432       |
| 2   | POSTGRESQL_HOST     | string  | localhost  |
| 3   | POSTGRESQL_USER     | string  | postgres   |
| 4   | POSTGRESQL_PASSWORD | string  | hamid123   |
| 5   | POSTGRESQL_DB       | string  | smartstore |
| 6   | POSTGRESQL_MINCONN  | integer | 1          |
| 7   | POSTGRESQL_MAXCONN  | integer | 2          |
| 8   | APPS_HOST           | string  | localhost  |
| 9   | APPS_PORT           | integer | 8008       |
| 10  | APPS_NUM_WORKER     | integer | 2          |

# Need To Know

Jika ingin menambahkan config lain bisa tambahkan didalam file **.env**.
Kemudian buat file python didalam folder configs serta declare didalam file initt didalamnya.
