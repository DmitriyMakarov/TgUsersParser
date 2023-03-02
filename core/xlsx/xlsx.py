import xlsxwriter
import os

headers = {
    'id': 'id', 'bot': 'bot', 'premium': 'premium', 'access_hash': 'access_hash', 'first_name': 'first_name', 'last_name': 'last_name',
                'username': 'username', 'phone': 'phone', 'status': 'status',
}


def do(chat_id, data_time, group_name, users):
    files_path = '../../res/db/files/'
    if os.path.exists(files_path + chat_id) is not True:
        os.mkdir(files_path + chat_id)
    file_name = f'../../res/db/files/{chat_id}/{group_name}_{data_time}.xls'
    with xlsxwriter.Workbook(file_name) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_key = list(headers.keys())
        for index, user in enumerate(users.values()):
            row = map(lambda field_id: user.get(field_id, ''), header_key)
            worksheet.write_row(row=index + 1, col=0, data=row)