from django.shortcuts import render


def section_view(request, section_name):
    """Простая вьюха для страниц тестовой меню с одним шаблоном"""
    return render(request, 'section.html', {'section_name': section_name})
