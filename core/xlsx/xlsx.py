import xlsxwriter


headers = {
    'id': 'id', 'bot': 'bot', 'premium': 'premium', 'access_hash': 'access_hash', 'first_name': 'first_name', 'last_name': 'last_name',
                'username': 'username', 'phone': 'phone', 'status': 'status',
}

users = [
    {'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player1', 'bank': 0.06},
    {'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player2', 'bank': 4.0},
    {'dailyWinners': 1, 'dailyFree': 2, 'user': 'Player3', 'bank': 3.1},
    {'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player4', 'bank': 0.32}
]

def do_xlsx(file_path: str, headers: dict, items: list):
    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)


def do(users):
    for user in users.values():
        print(user)
do_xlsx("my xslx file.xlsx", headers, users)