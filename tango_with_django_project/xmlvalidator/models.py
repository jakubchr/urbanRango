from django.db import models

class XMLDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    xml = models.FileField(upload_to='xmls')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def display_content(self):
        with open(self.xml.path) as fp:
            return fp.read().replace('\n', '<br>')