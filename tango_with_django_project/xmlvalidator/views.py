from django.shortcuts import render
from django.utils.encoding import smart_text
from xmlvalidator.forms import XMLForm

def model_xml_upload(request):
    if request.method == 'POST':
        form = XMLForm(request.POST, request.FILES)
        if form.is_valid():
            #result = validate_xml(request.FILES['xml'])
            #context_dict = { 'errors': result }
            for filename, f in request.FILES.items():
                context_dict = {'filename': filename, 'content': f.read().decode("utf-8").split('\n')}
            return render(request, 'xmlvalidator/validation_result.html', context=context_dict)
    else:
        form = XMLForm()
    return render(request, 'xmlvalidator/model_xml_upload.html', {'form': form})
            