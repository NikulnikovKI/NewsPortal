import random
from .models import Post, Author

# post_types = ['NW', 'AR']
#
# def gen_post():
#     author_ids = Author.objects.values_list('id', flat=True)
#
#     if not author_ids:
#         print("Нет доступных авторов для создания постов.")
#         return
#
#     for i in range(4, 50):
#         # Get random author
#         author_id = random.choice(author_ids)
#         author = Author.objects.get(pk=author_id)  # Получаем объект автора
#
#         kwargs = {
#             "author": author,  # Передаем объект автора, а не ID
#             "categoryType": random.choice(post_types),
#             "title": f"Заголовок поста{i}",
#             "text": f"Содержимое поста{i}",
#         }
#         Post.objects.create(**kwargs)
#     print("Посты созданы")


def create_or_edit(context, request_path):
    if "create" in request_path:
        title = " Добавление"
    else:
        title = " Редактирование"

    if "news" in request_path:
        title += " новости"
    else:
        title += " статьи"


    context['create_or_edit'] = title
    return context