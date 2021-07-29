# Let's get some practice using tuples.
from collections import namedtuple


def main():
    interns = [
        {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"},
        {"id": 2, "email": "kdiben1@tinypic.com", "name": "Kennan", "gender": "M"},
        {"id": 3, "email": "kmummery2@wikimedia.org", "name": "Keven", "gender": "M"},
        {"id": 4, "email": "gmartinson3@illinois.edu", "name": "Gannie", "gender": "M"},
        {"id": 5, "email": "adaine5@samsung.com", "name": "Antonietta", "gender": "F"},
    ]

    # === **Scoll down to challenege 1 ** ===
    intern_tuples = create_intern_tuples(interns)
    # ==== Challenge 2: Reading Tuple Data ====
    # Once your tuples are created, print out the following requests from HR :

    # Naming variables for better reading and cleaner code.
    id = 0
    email = 1
    name = 2
    gender = 3
    #   - Mitzi's name
    print(intern_tuples[0][name])
    #   - Kennan's ID
    print(intern_tuples[1][id])
    #   - Keven's email
    print(intern_tuples[2][email])
    #   - Gannie's name
    print(intern_tuples[3][name])
    #   - Antonietta's Gender
    print(intern_tuples[4][gender])
    # === **Scroll down to challenge 3** ===
    intern_named_tuples = create_named_tuples(interns)

    # === Challenge 4 ===
    # Once your **named tuples** are created, print out the following requests from HR into the console:
    #
    # Mitzi's name
    print(intern_named_tuples[0].name)
    # Kennan's ID
    print(intern_named_tuples[1].id)
    # Keven's email
    print(intern_named_tuples[2].email)
    # Gannie's name
    print(intern_named_tuples[3].name)
    # Antonietta's Gender
    print(intern_named_tuples[4].gender)


# ==== Challenge 1: Creating Tuples ====
# HR needs some information on the new interns put into a database.
# Given an id, email, first name, and gender. Create an tuple for each person in the company list:
#
# Example format of an intern dict: {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"}
def create_intern_tuples(interns_list):
    interns = []
    for intern in interns_list:
        interns.append(tuple(intern.values()))

    return interns


# ==== Challenge 3: Named Tuples ====
# Pickig out data from a tuple can be cumbersome, esp when we have lots of fields in our data.
# However we can make things easier using a **named tuple**. Named tuples allow us to
# assign names to the values in our tuples.
#
# example
# color = namedtuple("Color", "r g b")
#
#                   [r] [g] [b]
# my_color = color(255, 128, 78)
# print(my_color.r)
# print(my_color.g)
# print(my_color.b)
#
# reusing the data that HR gave us, create named tuples
# Example format of an intern dict: {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"}
def create_named_tuples(interns_list):
    interns = []
    Intern = namedtuple('Intern', ['id', 'email', 'name', 'gender'])
    for intern in interns_list:
        new_tuple = Intern(intern.get('id'), intern.get('email'), intern.get('name'), intern.get('gender'))
        interns.append(new_tuple)

    return interns

if __name__ == "__main__":
    # call your main function
    main()
    pass
