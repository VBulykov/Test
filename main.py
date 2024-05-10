import json
from functions import add_record, edit_record, search_record
from typing import Any

try:
    with open('data.json', 'r') as file:
        data: dict = json.load(file)
except:
    with open('data.json', 'w') as file:
        json.dump({
            'Баланс': 0,
            'Доходы': 0,
            'Расходы': 0,
            'Записи': []
        }, file)

    with open('data.json', 'r') as file:
        data: dict = json.load(file)

print('Вы находитесь в приложении "Личный финансовый кошелек".')
action: str = ''

while action != '0':
    print(
        'Для перехода далее введите номер желаемого действия:',
        '1 - Вывод текущего баланса',
        '2 - Вывод доходов',
        '3 - Вывод расходов',
        '4 - Добавление новой записи',
        '5 - Режим изменения записей',
        '6 - Режим поиска записей',
        '0 - Выход из приложения', sep='\n'
    )
    action: str = input('Введите номер желаемого действия:')
    
    match action:
        case '1':
            data['Баланс'] = sum([record['Сумма'] for record in data['Записи']])
            print(f'Текущий баланс =', data['Баланс'])
        
        case '2':
            data['Доходы'] = sum([record['Сумма'] for record in data['Записи'] if record['Категория'] == 'Доходы'])
            print('Доходы =', data['Доходы'])
        
        case '3':
            data['Расходы'] = sum([record['Сумма'] for record in data['Записи'] if record['Категория'] == 'Расходы'])
            print('Расходы =', data['Расходы'])
        
        case '4':
            add_record(data)
            with open('data.json', 'w') as file:
                json.dump(data, file)
        
        case '5':
            if len(data['Записи']) != 0:
                print('Выберите существующую запись из списка:')
                change_record: bool = False
                
                while not change_record:
                    for i in range(len(data['Записи'])):
                        for key in data['Записи'][i].keys():
                            print(key, data['Записи'][i][key])
                        
                        print('Введите номер действия', 
                            '1 - Редактирование записи',
                            '2 - Переход к следующей записи',
                            '0 - Выход из режима редактирования', sep='\n'
                        )
                        edit_action: str = input('Номер действия: ').strip() 
                        
                        match edit_action:
                            case '1':
                                record_is_edited: bool = False
                                while not record_is_edited:
                                    edit_record(data, i)
                            
                            case '0':
                                change_record = True
                                break
                
                with open('data.json', 'w') as file:
                    json.dump(data, file)
            
            else:
                print('Нет записей.')
                            
        case '6':
            search_record(data)

        case '0':
            break
        
        case _:       
            print('Выберите действие из списка.')
    
    with open('data.json', 'w') as file:
        json.dump(data, file)

