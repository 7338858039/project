import os
import xml.etree.ElementTree as ET
import csv


def xml_to_csv(xml_dir, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image_path', 'xmin', 'ymin', 'xmax', 'ymax', 'class'])

        for xml_file in os.listdir(xml_dir):
            if xml_file.endswith('.xml'):
                xml_path = os.path.join(xml_dir, xml_file)
                tree = ET.parse(xml_path)
                root = tree.getroot()

                image_path = root.find('filename').text

                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    bbox = obj.find('bndbox')
                    xmin = bbox.find('xmin').text
                    ymin = bbox.find('ymin').text
                    xmax = bbox.find('xmax').text
                    ymax = bbox.find('ymax').text
                    writer.writerow([image_path, xmin, ymin, xmax, ymax, class_name])

# Example usage
xml_dir = ''
csv_file = 'annotations.csv'
xml_to_csv(xml_dir, csv_file)






        
