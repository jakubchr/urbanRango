from django.shortcuts import render
from django.forms import forms
from xmlvalidator.forms import XMLForm
from xmlvalidator.validator.XML import XML
from django.utils.translation import ugettext_lazy as _


def model_xml_upload(request):
    if request.method == 'POST':
        form = XMLForm(request.POST, request.FILES)
        if form.is_valid():
            decree_point = request.POST.get('decree_point')
            for filename, f in request.FILES.items():
                first_line = f.readline().strip()
                f.seek(0)
                print(first_line)
                if first_line != b'<?xml version="1.0" encoding="UTF-8"?>' and first_line != b'\xef\xbb\xbf<?xml version="1.0" encoding="UTF-8"?>': #first option is for UTF-8 without BOM and second with BOM
                    error = 'Pierwsza linia powinna zawierać atrybut wersji XML a plik powinien być zapisany zgodnie z kodowaniem UTF-8! <?xml version="1.0" encoding="UTF-8"?>'
                    context_dict = {'error': error}
                    return render(request, 'xmlvalidator/validation_result.html', context=context_dict)
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