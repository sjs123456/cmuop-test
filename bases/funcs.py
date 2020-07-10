#coding=utf-8
from openpyxl import load_workbook
from selenium.webdriver.support.select import Select

#dr:浏览器对象 id:操作元素id    txt：选中的文字内容
def selListTxt(dr,id,txt):
    if txt != "":
        Select(dr.find_element_by_id(id)).select_by_visible_text(txt)


def rowToList(row):
    case = []
    for r in row:
        if r.value == None:
            case.append("")
        else:
            case.append(str(r.value))  # append:末尾添加
    return case