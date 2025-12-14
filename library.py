# library.py
# Module 1 Assignment - 修改了文件内容

# 定义一个空列表，用来存储所有的书
library_data = []
print("图书馆初始化完成，当前书籍数量：", len(library_data))


# 工具1：添加书籍
def add_book(library, title, author):
    """功能：向图书馆添加一本书"""
    new_book = {"title": title, "author": author}
    library.append(new_book)
    print(f"✅ 成功添加书籍：《{title}》")


# 工具2：列出所有书籍
def list_books(library):
    print("\n--- 📚 当前馆藏 ---")
    if not library:
        print("（暂无书籍）")
    else:
        for book in library:
            print(f"书名：{book['title']} | 作者：{book['author']}")
    print("-------------------\n")


# 工具3：查找书籍
def find_book(library, search_title):
    print(f"\n🔍 正在查找：《{search_title}》...")

    found = False
    for book in library:
        if book["title"].lower() == search_title.lower():
            print(f"✅ 找到啦！作者是：{book['author']}")
            found = True
            break

    if not found:
        print("❌ 抱歉，查无此书。")


# --- 主程序逻辑 ---
print("欢迎使用 Python 迷你图书馆！")
print("可用指令：add (添加), list (查看), find (查找), quit (退出)")

while True:
    command = input("\n请输入指令 > ").strip().lower()

    if command == "quit":
        print("👋 再见！程序已退出。")
        break

    elif command == "add":
        input_title = input("请输入书名：").strip()
        input_author = input("请输入作者：").strip()
        add_book(library_data, input_title, input_author)

    elif command == "list":
        list_books(library_data)

    elif command == "find":
        search_term = input("请输入要查找的书名：").strip()
        find_book(library_data, search_term)

    else:
        print("⚠️ 指令无法识别，请重新输入。")
