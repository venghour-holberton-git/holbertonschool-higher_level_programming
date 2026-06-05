#!/usr/bin/python3
import xml.etree.ElementTree as ET
import pickle

def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        child =  ET.Element(key)
        child.text = str(value)
        root.append(child)

    print(ET.tostring(root))
    with open(filename, "wb") as f:
        f.write(ET.tostring(root))

def deserialize_from_xml(filename):
    with open(filename, "rb") as f:
        root = ET.parse(filename).getroot()
        xml_dic = {child.tag: child.text for child in root}
        return xml_dic


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")
    
    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
