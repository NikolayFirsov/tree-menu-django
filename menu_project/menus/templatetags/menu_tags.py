from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Рисует древовидное меню для указанного меню на основе текущего URL.

    Аргументы:
    - context: Контекст шаблона, содержащий текущий запрос.
    - menu_name: Название меню для отображения.

    Возвращает:
    - Словарь с ключом 'menu_tree', содержащим структуру дерева меню.
    """
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').order_by('parent', 'order')

    menu_tree = build_menu_tree(menu_items)
    update_menu_status(menu_tree, current_url)

    return {'menu_tree': menu_tree}


def build_menu_tree(menu_items):
    """
    Строит дерево меню из списка объектов MenuItem.

    Аргументы:
    - menu_items: QuerySet с элементами меню.

    Возвращает:
    - Древовидную структуру меню в виде списка словарей.
    """
    menu_dict = {}
    tree = []

    for item in menu_items:
        menu_dict[item.id] = {
            'item': item,
            'children': [],
            'active': False,
            'expanded': False
        }

    for item in menu_items:
        if item.parent_id:
            menu_dict[item.parent_id]['children'].append(menu_dict[item.id])
        else:
            tree.append(menu_dict[item.id])

    return tree


def update_menu_status(menu_tree, current_url):
    """
    Обновляет статус элементов меню: отмечает активные и раскрывает родителей активных пунктов.

    Аргументы:
    - menu_tree: Древовидная структура меню (список словарей).
    - current_url: Текущий URL для определения активного элемента.

    Возвращает:
    - True, если в текущем поддереве есть активный элемент.
    """
    is_any_active = False

    for node in menu_tree:
        if node['item'].get_absolute_url() == current_url:
            node['active'] = True
            is_any_active = True

        if node['children']:
            child_active = update_menu_status(node['children'], current_url)
            if child_active:
                node['expanded'] = True
                is_any_active = True

    return is_any_active
