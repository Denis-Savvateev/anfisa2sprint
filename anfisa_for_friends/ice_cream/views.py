from django.shortcuts import get_object_or_404, render

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    # Вызываем .get() и в его параметрах указываем условия фильтрации:
    ice_cream = get_object_or_404(
        IceCream.objects.filter(is_published=True, category__is_published=True),
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')

    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
