import sqlalchemy

print(f'SQLAlchemy版本:{sqlalchemy.__version__}')

# 连接数据库
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

# 建立映射表
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(64))
    nickname = Column(String(128))
    password = Column(String(32))

    def __repr__(self):
        return f'User(id={self.id}, name={self.username}, nickname={self.nickname}, password={self.password})'


print('-------------创建所有表------------------')
Base.metadata.create_all(engine)

print('-------------创建Session------------------')
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

print('-------------添加对象------------------')
user1 = User(username='yitian', nickname='易天', password='123456')
session.add(user1)

print(session.query(User).filter_by(username='yitian').first())

session.add_all([
    User(username='zhang3', nickname='张三', password='123456'),
    User(username='li4', nickname='李四', password='123456'),
    User(username='lily', nickname='李丽', password='00000000'),
    User(username='fakeuser', nickname='假的', password='fffffffack')
])
session.commit()

print('-------------更新对象------------------')
user1.password = '12345678'
print(session.dirty)  # 现在Session变脏了

print(session.query(User).filter_by(username='yitian').first())
session.rollback()
print('-------------回滚之后------------------')
print(session.query(User).filter_by(username='yitian').first())

print('-------------删除对象------------------')
fakeuser = session.query(User).filter_by(username='fakeuser').first()
print('删除前的fake用户:{0}'.format(session.query(User).filter_by(username='fakeuser').count()))
session.delete(fakeuser)
print('删除后的fake用户:{0}'.format(session.query(User).filter_by(username='fakeuser').count()))

print('-------------查询对象------------------')
instance = session.query(User).all()[0]
print(instance)
print(type(instance))

userInfoTuple = session.query(User.id, User.username, User.nickname, User.password).all()[0]
id1, username1, nickname1, password1 = userInfoTuple
print(userInfoTuple)
print(type(userInfoTuple))

print('-------------自定义属性名------------------')
userInfoTuple = session.query(User.username.label('name'), User.nickname).all()[0]
print(userInfoTuple.name, userInfoTuple.nickname)

print('-------------查询别名------------------')
from sqlalchemy.orm import aliased

user_alias = aliased(User, name='user_alias')
user = session.query(user_alias, user_alias.username).all()[0]
print(user)

print('-------------切片查询------------------')
print([u for u in session.query(User).order_by(User.id)[2:4]])

print('-------------过滤查询------------------')
print('-------------filter_by------------------')
for name, in session.query(User.username) \
        .filter_by(username='zhang3'):
    print(name)

print('-------------filter------------------')
for user in session.query(User). \
        filter(User.username == 'zhang3'):
    print(user)

from sqlalchemy import text

print('-------------原生SQL查询------------------')
print('-------------SQL查询------------------')
user1 = session.query(User). \
    filter(text("username='zhang3'")).one()
print(user1)

print('-------------绑定参数------------------')
for user in session.query(User). \
        filter(text("username like :name")). \
        params(name='zhang3'):
    print(user)

print('-------------完整SQL语句------------------')
for user in session.query(User). \
        from_statement(text("SELECT * from users where username like :name")). \
        params(name='%i%'):
    print(user)
