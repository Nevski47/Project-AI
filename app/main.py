
import json

def controlmem(member):

    if isinstance(member, dict):

        if 'id' in member:
            if isinstance(member['id'], str):
                if member['id'].strip():
                    id = True
                else:
                    id = False
            else:
                id = False
        else:
            id = False

        if 'lastName' in member:
            if isinstance(member['lastName'], str):
                if member['lastName'].strip():
                    lastName = True
                else:
                    lastName = False
            else:
                lastName = False
        else:
            lastName = False

        if 'firstName' in member:
            if isinstance(member['firstName'], str):
                if member['firstName'].strip():
                    firstName = True
                else:
                    firstName = False
            else:
                firstName = False
        else:
            firstName = False

        result = []

        if not id:
            result.append('id')
        if not firstName:
            result.append('firstName')
        if not lastName:
            result.append('lastName')
        return result
    else:
        return ['record']


file_name = 'Members.json'

with open(file_name, 'r', encoding='utf-8') as f:
    members = json.load(f)

    if 'company' in members:
        print(f'Наименование компании: {members['company']}')

        if 'employees' in members:
            quantmem = len(members['employees'])

            print(f'Количество сотрудников в компании: {quantmem}')

            correct_members = []

            for i in range(quantmem):

                now_mem = members['employees'][i]
                correct = controlmem(now_mem)

                if correct == []:
                    correct_members.append({
                        "id": now_mem["id"].strip(),
                        "firstName": now_mem["firstName"].strip(),
                        "lastName": now_mem["lastName"].strip(),
                        })
                elif correct == ['record']:
                    print('Переданное значение не корректно')
                else:
                    err_mem = "Не корректно заполнены поля:"

                    if 'lastName' in correct:
                        err_mem += " (lastName) "
                    if 'firstName' in correct:
                        err_mem += " (firstName) "
                    if 'id' in correct:
                        err_mem += " (id) "

                    print(f'{i + 1} {err_mem}')

            print(correct_members)

        else:
            print('Не найдено поле "employees" в файле JSON')
    else:
        print('Не найдено поле "company" в файле JSON')