from django.shortcuts import render
from xmlvalidator.forms import XMLForm
from xmlvalidator.validator.XML import XML

def model_xml_upload(request):
    if request.method == 'POST':
        form = XMLForm(request.POST, request.FILES)
        if form.is_valid():
            decree_point = request.POST.get('decree_point')
            for filename, f in request.FILES.items():
                context_dict = validate_xml(request.FILES[filename].name, "\n".join(f.read().decode("utf-8").split("\n")[1:]), decree_point)
            return render(request, 'xmlvalidator/validation_result.html', context=context_dict)
    else:
        form = XMLForm()
    return render(request, 'xmlvalidator/model_xml_upload.html', {'form': form})

def validate_xml(filename, content, decree_point):
    xml = XML(content, decree_point)
    result = xml.xml_errors
    if len(result) == 0:
        message = "Nie znaleziono błędów w pliku XML"
        context_dict = {'filename': filename, 'message': message}
        return context_dict
    context_dict = {'filename': filename, 'result': result}
    return context_dict