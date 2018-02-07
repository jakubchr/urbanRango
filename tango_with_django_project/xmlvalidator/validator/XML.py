from io import StringIO
from django.conf import settings
import os
from lxml import etree

class XML:

    def __init__(self, content, decreePoint):
        self.text = content
        self.decreePoint = decreePoint
        self.xml_errors = list()

        if(self.decreePoint == "12_1_3"):
            self.validate("12_1_3")
        elif(self.decreePoint == "12_1_2"):
            self.validate("12_1_2")


    def validate(self, decreePoint):
        xmlparser = self.__getXMLParserForSchema(self.decreePoint)
        try:
            etree.fromstring(self.text, xmlparser)
        except (etree.XMLSchemaError, etree.XMLSyntaxError) as e:
            pass
        for error in xmlparser.error_log:
            self.xml_errors.append('Typ błędu: ' + str(error.type)  + ' treść: ' + error.message)

    def __getXMLParserForSchema(self, schema_name):
        schema_file = schema_name + '_schema.xsd'
        schema = os.path.join(settings.MEDIA_ROOT, schema_file)
        with open(schema, 'rb') as f:
            schemaxsd = etree.XML(f.read())
        schema = etree.XMLSchema(schemaxsd)
        xmlparser = etree.XMLParser(schema=schema)
        return xmlparser