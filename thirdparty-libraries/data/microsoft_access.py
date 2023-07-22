# %%
import faker
import pyodbc

create_table_sql = """\
create table user
(
  id        autoincrement primary key,
  username  varchar(255) unique,
  nickname  varchar(255) not null,
  password  varchar(20)  not null,
  address   varchar(255),
  birthday  date,
  company   varchar(30),
  job       varchar(20),
  telephone varchar(14)
)
"""

insert_table_sql = """\
insert into user(username, nickname, password, address, birthday, company, job, telephone)
values (?, ?, ?, ?, ?, ?, ?, ?)
"""

select_public_servant_sql = """\
select *
from user
where job = '公务员'
"""


def get_windows_desktop_path():
    """
    return C:\\Windows\\techstay\\Desktop
    """
    import subprocess

    out = subprocess.run(
        "powershell -nop -c [Environment]::GetFolderPath('Desktop')".split(" "),
        capture_output=True,
    )

    if out.returncode == 0:
        return out.stdout.decode().strip()
    else:
        raise SystemError("Failed to get Windows desktop path")


# 准备模拟数据
fake = faker.Faker("zh_CN")
# 设置种子值，不设的话每次随机的都不一样
faker.Faker.seed(47)

db_file_location = rf"{get_windows_desktop_path()}\db.accdb"

connection = pyodbc.connect(
    rf"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_file_location};"
)

connection.autocommit = True


with connection.cursor() as cursor:
    cursor.execute(create_table_sql)

# %%

# 添加数据
with connection.cursor() as cursor:
    for _ in range(3000):
        cursor.execute(
            insert_table_sql,
            (
                fake.pystr(min_chars=6, max_chars=10),
                fake.name(),
                fake.password(length=10),
                fake.address(),
                fake.date_of_birth(minimum_age=0, maximum_age=120),
                fake.company(),
                fake.job(),
                fake.phone_number(),
            ),
        )

# %%
with connection.cursor() as cursor:
    # 查询一下所有公务员
    cursor.execute(select_public_servant_sql)
    results = cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], sep="\t")

# %%
