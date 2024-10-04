from django.db import migrations


def load_initial_menus(apps, schema_editor):
    menu_model = apps.get_model('menus', 'Menu')
    menu_item_model = apps.get_model('menus', 'MenuItem')

    # создание меню direct_link_menu и named_url_menu
    direct_menu = menu_model.objects.create(name='direct_link_menu')
    named_menu = menu_model.objects.create(name='named_url_menu')

    # создание пунктов меню для direct_link_menu
    topic_1 = menu_item_model.objects.create(
        name='Тема 1',
        url='/section/topic-1/',
        menu=direct_menu,
        parent=None
    )
    menu_item_model.objects.create(
        name='Страница 1.1',
        url='/section/page-1-1/',
        menu=direct_menu,
        parent=topic_1
    )
    page_1_2 = menu_item_model.objects.create(
        name='Страница 1.2',
        url='/section/page-1-2/',
        menu=direct_menu,
        parent=topic_1
    )
    menu_item_model.objects.create(
        name='Страница 1.2.1',
        url='/section/page-1-2-1/',
        menu=direct_menu,
        parent=page_1_2
    )
    topic_2 = menu_item_model.objects.create(
        name='Тема 2',
        url='/section/topic-2/',
        menu=direct_menu,
        parent=None
    )
    menu_item_model.objects.create(
        name='Страница 2.1',
        url='/section/page-2-1/',
        menu=direct_menu,
        parent=topic_2
    )
    menu_item_model.objects.create(
        name='Страница 2.2',
        url='/section/page-2-2/',
        menu=direct_menu,
        parent=topic_2
    )

    # создание пунктов меню для named_url_menu
    for_clients_page = menu_item_model.objects.create(
        name='Для клиентов',
        named_url='for_clients',
        menu=named_menu,
        parent=None
    )
    menu_item_model.objects.create(
        name='О нас',
        named_url='about',
        menu=named_menu,
        parent=for_clients_page
    )
    menu_item_model.objects.create(
        name='Контакты',
        named_url='contact',
        menu=named_menu,
        parent=for_clients_page
    )
    menu_item_model.objects.create(
        name='Отзывы',
        named_url='reviews',
        menu=named_menu,
        parent=for_clients_page
    )


class Migration(migrations.Migration):
    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_menus),
    ]
