from django.db import models

DECREE_CHOICES = (
    ('12_1_2', '12_1_2'),
    ('12_1_3', '12_1_3'),
)

class XMLDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    xml = models.FileField(upload_to='xmls')
    decree_point = models.CharField(max_length=30, choices=DECREE_CHOICES, default='12_1_2')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def display_content(self):
        with open(self.xml.path) as fp:
            return fp.read().replace('\n', '<br>')