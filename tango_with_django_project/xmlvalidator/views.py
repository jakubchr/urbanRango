from django.shortcuts import render
from xmlvalidator.forms import XMLForm
from xmlvalidator.validator.XML import XML

def model_xml_upload(request):
    if request.method == 'POST':
        form = XMLForm(request.POST, request.FILES)
        if form.is_valid():
            for filename, f in request.FILES.items():
                xml = XML("\n".join(f.read().decode("utf-8").split("\n")[1:]), "12_1_2")
                result = xml.xml_errors
                if len(result) == 0:
                    result = "No errors in XML found!"
                context_dict = {'filename': filename, 'content': result}
            return render(request, 'xmlvalidator/validation_result.html', context=context_dict)
    else:
        form = XMLForm()
    return render(request, 'xmlvalidator/model_xml_upload.html', {'form': form})
            