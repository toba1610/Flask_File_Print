
import win32print # pip install win32printing
import os
import json_data_process as jdp

def get_printer(printer_name: str) -> str:

    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS, None, 1)
    printer_name = os.path.normpath(printer_name)

    for num_list, printer_data in enumerate(printers):
        for pos_name, printer_bez in enumerate(printer_data):
            if printer_name == printer_bez:
                print('OK')
                printer = printers[num_list][pos_name]


    if printer != '':

        return printer
    
    else:

        raise NameError

def print_pdf(file_path: str = None, printer_name: str = None) -> None:

    file_path = os.path.abspath(file_path)

    if printer_name == None:
        printer_name = jdp.read_JSON_Data('config.json', 'Config_Programm', 'Printer')

    printer = get_printer(printer_name=printer_name)
    
    file_handle = open(file_path, 'rb')
    printer_handle = win32print.OpenPrinter(printer)

    job_info = win32print.StartDocPrinter(printer_handle,1,(file_path,None, "RAW"))

    win32print.StartPagePrinter(printer_handle)
    win32print.WritePrinter(printer_handle, file_handle.read())
    win32print.EndPagePrinter(printer_handle)
    win32print.EndDocPrinter(printer_handle)


# print_pdf('.\\Reports\\Report_JM_V2214612_11009238010.pdf')

# print('Path')
# print(os.path.normpath('//JM-SPOOL6/FollowME'))




