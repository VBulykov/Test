import datetime
from typing import Dict, List

def add_record(data: Dict[str, List[Dict[str, any]]]) -> None:
    """
    Добавляет новую запись в список записей.

    Args:
        data (Dict[str, List[Dict[str, any]]]): Словарь, содержащий список записей.

    Raises:
        ValueError: Если дата введена в неверном формате.
    """
    try:
        print('Введите дату в числовом формате')
        year: int = int(input('Введите год:'))
        month: int = int(input('Введите номер месяца:'))
        day: int = int(input('Введите число:'))
        print('Введите номер категории:', '1 - Доходы', '2 - Расходы', sep='\n')
        category: int = int(input('Номер категории:'))

        if category == 1:
            category = 'Доходы'
        else:
            category = 'Расходы'

        amount: int = int(input('Введите сумму:'))
        description: str = input('Введите описание:')

        if description == '':
            description = 'Описания нет.'
        date: datetime.datetime = datetime.datetime(year, month, day)

        data['Записи'].append(
            {
                'Дата': date.strftime("%Y/%m/%d,  %H:%M:%S"),
                'Категория': category,
                'Сумма': amount,
                'Описание': description
            }
        )
    except ValueError:
        print('Дата введена в неверном формате.')

def edit_record(data: Dict[str, List[Dict[str, any]]], index: int) -> None:
    """
    Редактирует существующую запись в списке записей.

    Args:
        data (Dict[str, List[Dict[str, any]]]): Словарь, содержащий список записей.
        index (int): Индекс записи, которую нужно отредактировать.
    """
    print(
        'Введите номер действия:',
        '1 - Редактировать запись',
        '2 - Удалить запись',
        '0 - Выход из режима редактирования', sep='\n'
    )
    action: str = input('Номер действия:').strip()
    global record_is_edited
    
    match action:
        case '1':
            print(
                'Введите номер свойства которое вы желаете изменить',
                '1 - Дата',
                '2 - Категория',
                '3 - Сумма',
                '4 - Описание',
                '0 - Выход из редактирования', sep='\n'
            )
            num: str = input('Номер свойства:').strip()

            match num:
                case '1':
                    print('Введите дату в числовом формате')
                    try:
                        year: int = int(input('Введите год:'))
                        month: int = int(input('Введите номер месяца:'))
                        day: int = int(input('Введите число:'))
                        data['Записи'][index]['Дата'] = datetime.datetime(year, month, day)
                    except:
                        print('Дата введена в неверном формате.')

                case '2':
                    category: int = int(input('Введите номер категории:', '1 - Доходы', '2 - Расходы', sep='\n'))
                    if category == 1:
                        data['Записи'][index]['Категория'] = 'Доходы'
                    elif category == 2:
                        data['Записи'][index]['Категория'] = 'Расходы'

                case '3':
                    data['Записи'][index]['Сумма'] = int(input('Введите сумму:'))

                case '4':
                    data['Записи'][index]['Описание'] = input('Введите описание:')

                case '0':
                    record_is_edited = True

            print('Измененная запись:', data['Записи'][index], sep='\n')

        case '2':
            del data['Записи'][index]
            print('Запись успешно удалена.')
            record_is_edited = True

        case '0':
            record_is_edited = True

        case _:
            pass

def search_record(data: Dict[str, List[Dict[str, any]]]) -> None:
    """
    Выполняет поиск записей по заданным критериям.

    Args:
        data (Dict[str, List[Dict[str, any]]]): Словарь, содержащий список записей.
    """
    print(
        'Введите номер свойства по которому будет выполняться поиск:',
        '1 - Дата',
        '2 - Категория',
        '3 - Сумма', sep='\n'
    )
    search_key: str = input('Номер свойства:').strip()
    searched_records: List[Dict[str, any]] = []
    
    match search_key:
        case '1':
            print('Введите дату в числовом формате')
            year: int = int(input('Введите год:'))
            month: int = int(input('Введите номер месяца:'))
            day: int = int(input('Введите число:'))
            date: str = datetime.datetime(year, month, day).strftime("%Y/%m/%d, %H:%M:%S")
            for i in range(len(data['Записи'])):
                if data['Записи'][i] == date:
                    searched_records.append(data['Записи'][i])

        case '2':
            print(
                'Введите номер категории:', '1 - Доходы', '2 - Расходы', sep='\n'
            )
            category: int = int(input('Номер категории:'))
            if category == 1:
                for i in range(len(data['Записи'])):
                    if data['Записи'][i]['Категория'] == 'Доходы':
                        searched_records.append(data['Записи'][i])
            elif category == 2:
                for i in range(len(data['Записи'])):
                    if data['Записи'][i]['Категория'] == 'Расходы':
                        searched_records.append(data['Записи'][i])

        case '3':
            summa: int = int(input('Введите сумму:'))
            for i in range(len(data['Записи'])):
                if data['Записи'][i]['Сумма'] == summa:
                    searched_records.append(data['Записи'][i])

    if len(searched_records) == 0:
        print('По заданным параметрам записей нет.')

    for record in searched_records:
        print(f'Дата - {record['Дата']}')
        print(f'Категория - {record['Категория']}')
        print(f'Сумма - {record['Сумма']}')
        print(f'Описание - {record['Описание']}')