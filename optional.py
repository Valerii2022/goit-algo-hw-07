class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, reply):
        if reply in self.replies:
            # Помічаємо відповідь як видалену
            reply.is_deleted = True
            reply.text = "Цей коментар було видалено."

    def display(self, indent=0):
        if self.is_deleted:
            # Виводимо стандартне повідомлення для видаленого коментаря
            print(' ' * indent + "Цей коментар було видалено.")
        else:
            print(' ' * indent + f"{self.author}: {self.text}")
            for reply in self.replies:
                reply.display(indent + 4)

# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо reply1_1
reply1.remove_reply(reply1_1)

# Виводимо дерево коментарів
root_comment.display()



