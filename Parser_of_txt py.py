#прием и проверка пути
def way_check():
    while True:
        user_way = input("Введи путь к файлу: ").strip('"/ ')
        try:
            with open(user_way, 'r') as user_file:
                print(f"Путь подтвержден: {user_way}")
                return user_way
        except FileNotFoundError:
            print("Not Found. Попробуй еще раз.")
def work(nway):pass            
def main():
    nway=way_check()
    work(nway)
if __name__=="__main__":
    main()            