from .models import User, Contact

from django.contrib.auth.hashers import make_password


def create_users():

    sample_data = [
        {
            'username':'suraj',
            'name':'Suraj Mishra',
            'number':'9198974643',
            'email':'isurajmisra@gmail.com',
        },
    {
        'username':'sachin',
    'name':'Sachin Mishra',
    'number':'9415600701',
    'email':'',
    },
    {
        'username':'manish',
    'name':'Manish Mishra',
    'number':'9128928922',
    'email':'',
    },
    {
        'username':'aditya',
    'name':'Aditya Mishra',
    'number':'91283929292',
    'email':'',
    },
    {
        'username':'sagar',
    'name':'Sagar Verma',
    'number':'8005027272',
    'email':'',
    },
    {
        'username':'nitin',
    'name':'Nitin Singh',
    'number':'72828282829',
    'email':'',
    },
    ]

    User.objects.bulk_create([
        User(
            username=data['username'],
            name=data['name'],
            number=data['number'],
            email=data['email'],
            password=make_password('123')
        ) for data in sample_data
    ])
    print("created Sample User")


def create_contacts():
        sample_data = [
            {

                'name': 'Suraj Mishra',
                'number': '9198974643',

            },
            {

                'name': 'Sachin Mishra',
                'number': '9415600701',

            },
            {

                'name': 'Manish Mishra',
                'number': '9128928922',

            },
            {

                'name': 'Aditya Mishra',
                'number': '91283929292',

            },
            {

                'name': 'Sagar Verma',
                'number': '8005027272',

            },
            {

                'name': 'Nitin Singh',
                'number': '72828282829',

            },
        ]
        user_list = User.objects.all()

        Contact.objects.bulk_create([
            Contact(
                name=data['name'],
                number=data['number'],
                user=user_list.first()
            )for data in sample_data[1:3]
        ])
        Contact.objects.bulk_create([
            Contact(
                name=data['name'],
                number=data['number'],
                user=user_list.last()
            ) for data in sample_data[:4]
        ])
        print("Contacts Created.")
