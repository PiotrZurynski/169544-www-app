Category.objects.all()
//<QuerySet [<Category: Ciekawe>, <Category: Nieciekawe>, <Category: Zabawne>]>
Category.objects.get(id=3)
//<Category: Nieciekawe>
Category.objects.filter(name__istartswith='Z')
//<QuerySet [<Category: Zabawne>]>
Topic.objects.values_list('category__name', flat=True).distinct()
//<QuerySet ['Nieciekawe', 'Ciekawe', 'Zabawne']>
Post.objects.order_by('-title').values_list('title', flat=True)
//<QuerySet ['Ślimakowe wyścigi', 'Kiwi ptak nielot', 'Grzybobranie']>

Category.objects.create(name='Poradniki', description='Jak złapać suma?')
//Category: Poradniki>