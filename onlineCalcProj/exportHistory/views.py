
from datetime import datetime
from datetime import timedelta
import xlwt
from xlwt import Workbook,XFStyle,Borders, Pattern, Font, easyxf
from django.http import HttpResponse

from operationsHistory.models import History

def export_history_to_xlsx(request):
       startDate=request.GET.get('startDate')
       print(startDate)
       history_queryset = History.objects.all()
       headers_style=easyxf('pattern: pattern solid, fore_colour blue;'
                       'font: colour white, bold True;''borders: top thin , bottom thin, left thin, right thin;')

       data_style = xlwt.easyxf('pattern: pattern solid, fore_colour white;'
                'font: colour black;''borders: top thin, bottom thin, left thin, right thin;',num_format_str='D-MMM-YY HH:MM:SS')
       
       
       response = HttpResponse(
           content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
       )
       response['Content-Disposition'] = 'attachment; filename={date}-operations-history.xls'.format(
           date=datetime.now().strftime('%Y-%m-%d'),
       )
       book = xlwt.Workbook()
       
       # Get active worksheet/tab
       worksheet =book.add_sheet("operations History")

       # Define the titles for columns
       columns = [
           'ID',
           'Expression',
           'Ans',
           'Error',
           'Executed_at',

       ]
       row_num = 0

       # Assign the titles for each cell of the header
       for col_num, column_title in enumerate(columns, 0):
           worksheet.write(row_num,col_num,column_title,headers_style)


       # Iterate through all movies
       for operation in history_queryset:
              row_num += 1

           # Define the data for each cell in the row 
              row = [
              str(operation.pk),
              operation.expression,
              operation.ans,
              operation.error,
              operation.updated_at.replace(tzinfo=None),

              ]

           # Assign the data for each cell of the row 
              for col_num, cell_value in enumerate(row, 0):
                     worksheet.write(row_num,col_num,cell_value,data_style)


       book.save(response)

       return response