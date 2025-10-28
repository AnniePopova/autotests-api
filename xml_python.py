import xml.etree.ElementTree as ET

xml_data = """
<user>
<id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>john.doe@gmail.com</email>
</user>
"""

root = ET.fromstring(xml_data)

print("user ID: ", root.find('id').text)
print("user name: ", root.find('first_name').text, root.find('last_name').text)
print("user email: ", root.find('email').text)