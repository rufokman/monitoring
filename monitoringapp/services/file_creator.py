import datetime
import pandas as pd
from django.utils import timezone
from django.shortcuts import get_object_or_404
import xlwt
from django.http import HttpResponse
from ..models import *
import xlsxwriter




def get_update_data_not_fix():

	card_data = Card.objects.filter(status=0, delete=0)

	return card_data

def download_excel_admin(request):
	today = "KPI_pivot_{}".format(datetime.datetime.today().strftime("%d.%m.%Y"))
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(today)
	workbook = xlsxwriter.Workbook(response, {'in_memory': True})
	format = workbook.add_format()
	format.set_bg_color('#fdc433')
	ws = workbook.add_worksheet('Реестр')

	ws.set_column('A:A', 5)
	ws.set_column('B:B', 23)
	ws.set_column('C:C', 23, )
	ws.set_column('D:D', 23, )
	ws.set_column('E:E', 26, )
	ws.set_column('F:F', 11, )
	ws.set_column('G:G', 81, )
	ws.set_column('H:H', 16, )
	ws.set_column('I:I', 20, )
	ws.set_column('J:J', 20, )
	ws.set_column('K:K', 30, )
	ws.set_column('L:L', 20, )
	ws.set_column('M:M', 7, )
	ws.set_column('N:N', 17, )
	ws.set_column('O:O', 17, )
	ws.set_column('P:P', 40, )
	ws.set_column('Q:Q', 24, )
	ws.set_column('R:R', 24, )
	ws.set_column('S:S', 24, )
	columns = ['№ пп',  'Организация', 'ФИО сотрудника, в чью карту устанавливается КПЭ', 'Название должности',
			   'КПЭ / КлС2', 'Наименование КПЭ / КлС', 'Методика расчета',
			    'Нижний уровень', "Целевой уровень",
			   "Верхний уровень", "Вес", "Комментарий администратора",
			   "Прогноз 1 кв", "Прогноз 2 кв", "Прогноз 3 кв", "Прогноз 4 кв",
			   "Причина отклонения", "Предпринимаемые меры", "Прогнозное значение",
			   "Верификатор", "Последнее обновление", "ФИО пользователя",
			   ]
	row_num = 0
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num])

	row_num=0
	for my_row in get_update_data_not_fix():
		row_num = row_num + 1
		ws.write(row_num, 0, row_num)
		ws.write(row_num, 1, my_row.organization)
		ws.write(row_num, 2, my_row.fio)
		ws.write(row_num, 3, my_row.role)
		ws.write(row_num, 4, my_row.type)
		ws.write(row_num, 5, my_row.name)
		ws.write(row_num, 6, my_row.method)
		ws.write(row_num, 7, my_row.low_level)
		ws.write(row_num, 8, my_row.target_level)
		ws.write(row_num, 9, my_row.high_level)
		ws.write(row_num, 10, my_row.weight)
		ws.write(row_num, 11, my_row.comment)
		ws.write(row_num, 12, my_row.first_quarter)
		ws.write(row_num, 13,  my_row.second_quarter)
		ws.write(row_num, 14, my_row.third_quarter)
		ws.write(row_num, 15, my_row.fourth_quarter)
		ws.write(row_num, 16, my_row.reason)
		ws.write(row_num, 17, my_row.measure)
		ws.write(row_num, 18, my_row.forecast)
		ws.write(row_num, 19, my_row.verificator)
		ws.write(row_num, 20, str(my_row.updated_at))
		ws.write(row_num, 21, my_row.name_of_user)

	workbook.close()
	return response


def download_excel_user(request):
	today = "KPI_pivot_{}".format(datetime.datetime.today().strftime("%d.%m.%Y"))
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(today)
	workbook = xlsxwriter.Workbook(response, {'in_memory': True})
	format = workbook.add_format()
	format.set_bg_color('#fdc433')
	ws = workbook.add_worksheet('Реестр')

	ws.set_column('A:A', 5)
	ws.set_column('B:B', 23)
	ws.set_column('C:C', 23, )
	ws.set_column('D:D', 23, )
	ws.set_column('E:E', 26, )
	ws.set_column('F:F', 11, )
	ws.set_column('G:G', 81, )
	ws.set_column('H:H', 16, )
	ws.set_column('I:I', 20, )
	ws.set_column('J:J', 20, )
	ws.set_column('K:K', 30, )
	ws.set_column('L:L', 20, )
	ws.set_column('M:M', 7, )
	ws.set_column('N:N', 17, )
	ws.set_column('O:O', 17, )
	ws.set_column('P:P', 40, )
	ws.set_column('Q:Q', 24, )
	ws.set_column('R:R', 24, )
	ws.set_column('S:S', 24, )
	columns = ['№ пп', 'Организация', 'ФИО сотрудника, в чью карту устанавливается КПЭ', 'Название должности',
			   'КПЭ / КлС2', 'Наименование КПЭ / КлС', 'Методика расчета',
			    'Нижний уровень', "Целевой уровень",
			   "Верхний уровень", "Вес", "Комментарий администратора",
			   "Прогноз 1 кв", "Прогноз 2 кв", "Прогноз 3 кв", "Прогноз 4 кв",
			   "Причина отклонения", "Предпринимаемые меры", "Прогнозное значение",
			   "Верификатор"
			   ]
	row_num = 0
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num])

	row_num=0
	for my_row in get_update_data_not_fix():
		row_num = row_num + 1
		ws.write(row_num, 0, row_num)
		ws.write(row_num, 1, my_row.organization)
		ws.write(row_num, 2, my_row.fio)
		ws.write(row_num, 3, my_row.role)
		ws.write(row_num, 4, my_row.type)
		ws.write(row_num, 5, my_row.name)
		ws.write(row_num, 6, my_row.method)
		ws.write(row_num, 7, my_row.low_level)
		ws.write(row_num, 8, my_row.target_level)
		ws.write(row_num, 9, my_row.high_level)
		ws.write(row_num, 10, my_row.weight)
		ws.write(row_num, 11, my_row.comment)
		ws.write(row_num, 12, my_row.first_quarter)
		ws.write(row_num, 13,  my_row.second_quarter)
		ws.write(row_num, 14, my_row.third_quarter)
		ws.write(row_num, 15, my_row.fourth_quarter)
		ws.write(row_num, 16, my_row.reason)
		ws.write(row_num, 17, my_row.measure)
		ws.write(row_num, 18, my_row.forecast)
		ws.write(row_num, 19, my_row.verificator)

	workbook.close()
	return response
