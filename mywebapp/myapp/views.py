from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # Context data to pass to the template
    context = {
        'item1': 'This is item 1',
        'item2': 'This is item 2',
        'item3': 'This is item 3',
    }

    # Render the homepage template with the context data
    return render(request, 'myapp/homepage.html', context)

def form_submission_page(request):
    if request.method == 'POST':
        # Handle form submission
        form_data = request.POST.get('form_data')
        return HttpResponse(f"Form submitted with data: {form_data}")
    else:
        # Render the form page
        return render(request, 'form_page.html')