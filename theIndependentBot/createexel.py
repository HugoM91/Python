from heapq import merge
from turtle import width
import xlsxwriter

def create_exel():
    #workbook = xlsxwriter.Workbook('relatorio_'+self.estabelecimento+'_'+self.data_servico+'.xlsx')
    workbook = xlsxwriter.Workbook('relatorio.xlsx')
    worksheet = workbook.add_worksheet()
    merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'green',})
    merge_format2 = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'white',})

    merge_format3 = workbook.add_format({
    'bottom': 5,
    'left' : 5,
    'align': 'left',
    'valign': 'left',
    'fg_color': 'white',})


# Merge 3 cells.
    worksheet.merge_range('B2:I2', 'Decadente', merge_format)

    worksheet.write('B3', 'Data')
    #worksheet.write('B1', self.data_servico)
    worksheet.merge_range('B3:I3', 'self.data_servico', merge_format)
    worksheet.merge_range('B4:E4', ' ', merge_format)
    worksheet.merge_range('F4:I4', 'Relatorio', merge_format)
    worksheet.write('B5', 'MOD')
    worksheet.merge_range('C5:E5', ' ', merge_format2)
    worksheet.write('B6', 'Staff Sala')
    worksheet.merge_range('C6:E6', ' ', merge_format2)
    worksheet.write('B7', 'Staff Cozinha', merge_format3)
    worksheet.merge_range('C7:E7', ' ', merge_format3)
    worksheet.write('B8', 'Reservas Jantar')
    worksheet.merge_range('C8:E8', ' ', merge_format2)
    worksheet.write('B9', 'Walk-ins')
    worksheet.merge_range('C9:E9', ' ', merge_format2)
    worksheet.write('B10', 'Cancelamentos')
    worksheet.merge_range('C10:E10', ' ', merge_format2)
    worksheet.write('B11', 'No-shows')
    worksheet.merge_range('C11:E11', ' ', merge_format2)
    worksheet.write('B12', 'Jantares Servidos')
    worksheet.merge_range('C12:E12', ' ', merge_format2)
    worksheet.write('B13', 'Comidas')
    worksheet.merge_range('C13:E13', ' ', merge_format2)
    worksheet.write('B14', 'Bebidas S/ Alcool')
    worksheet.merge_range('C14:E14', ' ', merge_format2)
    worksheet.write('B15', 'Bebidas C/ Alcool')
    worksheet.merge_range('C15:E15', ' ', merge_format2)
    worksheet.write('B16', 'Vinhos')
    worksheet.merge_range('C16:E16', ' ', merge_format2)
    worksheet.write('B17', 'Eventos')
    worksheet.merge_range('C17:E17', ' ', merge_format2)
    worksheet.write('B18', 'Total Vendas')
    worksheet.merge_range('C18:E18', ' ', merge_format2)
    worksheet.write('B19', 'TM Comidas')
    worksheet.merge_range('C19:E19', ' ', merge_format2)
    worksheet.write('B20', 'TM Bebidas')
    worksheet.merge_range('C20:E20', ' ', merge_format2)
    worksheet.write('B21', 'Ticket Médio Geral')
    worksheet.merge_range('C21:E21', ' ', merge_format2)
    worksheet.write('B22', 'Nr pax')
    worksheet.merge_range('C22:E22', ' ', merge_format2)
    worksheet.write('B23', 'Total Facturado')
    worksheet.merge_range('C23:E23', ' ', merge_format2)
    worksheet.write('B24', 'Ticket Médio Evento')
    worksheet.merge_range('C24:E24', ' ', merge_format2)
    worksheet.write('B25', 'Transferências')
    worksheet.merge_range('C25:E25', ' ', merge_format2)
    worksheet.write('B26', 'MB')
    worksheet.merge_range('C26:E26', ' ', merge_format2)
    worksheet.write('B27', 'Cash')
    worksheet.merge_range('C27:E27', ' ', merge_format2)
    worksheet.write('B28', 'Comissões')
    worksheet.merge_range('C28:E28', ' ', merge_format2)
    worksheet.write('B29', 'Total Vendas')
    worksheet.merge_range('C29:E29', ' ', merge_format2)
    worksheet.write('B30', 'Budget Diário')
    worksheet.merge_range('C30:E30', ' ', merge_format2)
    worksheet.set_column('B5:B30', 21)
    worksheet.set_column('C:E', 15)
    worksheet.merge_range('F5:I21', 'self.descricao', merge_format2)
    worksheet.merge_range('F22:I25', '     ', merge_format)
    worksheet.merge_range('F26:I26', 'Manutenção', merge_format)
    worksheet.merge_range('F27:I31', 'self.manutenção', merge_format2)
    worksheet.merge_range('B32:I32', '' , merge_format)


    workbook.close()

create_exel()