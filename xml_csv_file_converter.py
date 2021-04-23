#Jonathan-WS
#XML_To_CSV_File_Converter
import csv
import xml.etree.ElementTree as ET


def xml_to_csv(file_path, csv_name) -> None:
    tree = ET.parse(file_path)
    root = tree.getroot()

    with open(csv_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[0])
        writer.writerow(headers)
        num_records = len(root)

        for record in range(num_records):
            rec = (child.text for child in root[record])
            writer.writerow(rec)


if __name__ == '_main_':
    import sys
    import pathlib

    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]

    except IndexError:
        sys.exit('Tow arguments required. One xml path and one save file name.')

    with pathlib.Path(file_path) as xml_file:
        if xml_file.is_file():
            xml_to_csv(file_path, csv_name)
        else:
            sys.exit(f'Did not find {file_path}')