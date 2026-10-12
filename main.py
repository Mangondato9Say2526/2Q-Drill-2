# Finding Surnames
from pyscript import display, document

def name_finder(e):
    document.getElementById('result').innerHTML = ''
    first_name = document.getElementById('firstname').value.lower().strip()
    last_name = document.getElementById('lastname').value.lower().strip()
    varsity_members = ['Elise Lim', 'Misha Manalo', 'Adrianna Allas', 'Ashley Mangondato', 'Bonnie Nubla']
    full_name = first_name + last_name
    student_checker = full_name in varsity_members

    display_message = (f'Congratulations!, {full_name} you are now part of the Varsity Team!', f'{full_name}')
    display(display_message[student_checker], target='result')