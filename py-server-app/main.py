from src.text_parser import parse_txt
from src.json_parser import parse_json
from src.yaml_parser import parse_yaml
from src.xml_parser import parse_xml
from src.csv_parser import parse_csv

print("............................................")
print("TXT FILE CONTENT:")

text_person = parse_txt()
print(text_person)
print(text_person.greet())


print("............................................")
print("JSON FILE CONTENT:")

json_person = parse_json()
print(json_person)
print(json_person.greet())


print("............................................")
print("YAML FILE CONTENT:")

yaml_person = parse_yaml()
print(yaml_person)
print(yaml_person.greet())


print("............................................")
print("XML FILE CONTENT:")

xml_person = parse_xml()
print(xml_person)
print(xml_person.greet())


print("............................................")
print("CSV FILE CONTENT:")

csvPerson = parse_csv()
print(csvPerson)
print(csvPerson.greet())

print("............................................")

