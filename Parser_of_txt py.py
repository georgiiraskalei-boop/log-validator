import json
from pathlib import Path
#прием и проверка пути
def way_check():
    while True:
        user_way = input("Введи путь к файлу: ").strip(r'"/\ ')
        
        # Проверяем существование файла средствами pathlib
        if Path(user_way).is_file():
            print(f"Путь подтвержден: {user_way}")
            return user_way
        else:
            print("Файл не найден или это папка. Попробуй еще раз.")
def work(nway):
# пoдсчет для INFO, WARNING, ERROR,CRITICAL 
    Info_list=[]
    Info_count=0
    Warning_list=[]  
    Warning_count=0
    Error_list=[]
    Error_count=0
    Critical_list=[]
    Critical_count=0
    with open (nway, "r", encoding='utf8') as user_file:
        for line_num,line in enumerate (user_file, start=1):  
            if "INFO" in line:
                Info_list.append((line_num,line)) 
                Info_count=Info_count+1
            if"WARNING" in line:
                Warning_list.append((line_num,line)) 
                Warning_count=Warning_count+1
            if "ERROR"in line:
                Error_list.append((line_num,line))
                Error_count+=1
            if "CRITICAL" in line:
                Critical_list.append((line_num,line))  
                Critical_count+=1  
    print(f"INFO: {Info_count}, WARNING: {Warning_count}, ERROR: {Error_count}, CRITICAL: {Critical_count}")                
    for line_num,line in Info_list:
        print(f"Строка {line_num}: {line.strip()}")
    for line_num,line in Warning_list:
        print(f"Строка {line_num}: {line.strip()}")
    for line_num,line in Error_list:
        print(f"Строка {line_num}: {line.strip()}")
    for line_num,line in Critical_list:
        print(f"Строка {line_num}: {line.strip()}")
    logs_data = {
        "INFO": {"count": Info_count, "items": Info_list},
        "WARNING": {"count": Warning_count, "items": Warning_list},
        "ERROR": {"count": Error_count, "items": Error_list},
        "CRITICAL": {"count": Critical_count, "items": Critical_list}
    } 
    return logs_data   
def save_to_json(data, filename="report.json"):
    with open(filename, "w", encoding="utf8") as user_file:
        json.dump(data, user_file, ensure_ascii=False, indent=4)
def main():
    nway = way_check()
    parsed_data = work(nway)  # Вызываем один раз и сохраняем результат
    save_to_json(parsed_data) # Передаем сохраненные данные в JSON
    print("Отчет успешно сохранен в report.json!")
if __name__=="__main__":
    main()