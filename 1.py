from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    db_sess = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module 1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)

    user = User()
    user.surname = 'Bons'
    user.name = "Billy"
    user.position = 'map_owner'
    user.speciality = 'captain'
    user.address = 'ship'
    db_sess.add(user)

    user = User()
    user.surname = 'Jim'
    user.name = "Hawkins"
    user.age = 20
    user.position = 'shipboy'
    user.speciality = 'student'
    db_sess.add(user)

    user = User()
    user.surname = 'Jhon'
    user.name = "Silver"
    user.age = 40
    user.position = 'spy'
    user.speciality = 'pirate'
    user.address = 'pirateship'
    user.email = 'find_treasure_map@pirate.org'
    user.hashed_password = 'ToP_SeCrEt'
    db_sess.add(user)

    db_sess.commit()


if __name__ == '__main__':
    main()
