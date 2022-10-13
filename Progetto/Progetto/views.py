from django.template import loader

def show_description(x):
    number = 0
    template = loader.get_template('Coffees.html')
    for coffee in models.Coffee.objects.all():
        number += 1
        if number == x:
            print(coffee.producer)

