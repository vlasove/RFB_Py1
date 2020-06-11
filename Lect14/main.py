#### Check [0] and [-1] indexes

n = int(input())

queue = []

for _ in range(n):
    command = input()
    if "Кто последн" in command:
        # Кто последний? Я - Кузнецов.
        # Из сообщения выше - вычленить "Кузнецов" и добавить в конец queue
        messages = command.split(" - ") # ["Кто последний ... Я", "Кузнецов."]
        lastname = messages[-1].split(".")[0] # ["Кузнецов", ""]
        queue.append(lastname)

    elif "Я толь" in command:
        # Я только спросить! Я - Иванова.
        # Из сообщения выше - вычленить "Иванова" и добавить в начало queue
        messages = command.split(" - ") # ["Я только спросить! Я", "Иванова."]
        lastname = messages[-1].split(".")[0] # ["Иванова", ""]
        queue.insert(0, lastname)

    else:
        # Если очередь не пуста - удалить из головы первый элемент и написать "Заходит [УДАЛЕННЫЙ_ЭЛЕМЕНТ]!"
        # Если пуста - "В очереди никого нет!"
        if len(queue) != 0:
            queue = queue[::-1]
            current_name = queue.pop()
            queue = queue[::-1]
            print("Заходит", current_name + "!")

        else:
            print("В очереди никого нет.")