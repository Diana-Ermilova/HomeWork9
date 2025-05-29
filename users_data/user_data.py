import dataclasses
import os.path
from  datetime import date


@dataclasses.dataclass
class User():
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_date: date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Diana',
            last_name='Ermilova',
            email='testmail.01@gmail.com',
            gender='Other',
            phone_number='8800123121',
            birth_date=date.fromisoformat('1996-09-18'),
            subjects='Physics',
            hobbies='Sports',
            picture='20762.jpg',
            address='London, county of Surrey, Privet Drive 4',
            state='Haryana',
            city='Panipat')


print (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imgs', '20762.jpg')))