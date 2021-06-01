import os, argparse, glob
import xml.etree.ElementTree as ET

def make_labelmap(path, export_dir):
    """ Membuat label_map.pbtxt """
    labels = []
    for xml_file in glob.glob(path + '/*.xml'):
        root = ET.parse(xml_file).getroot()
        for member in root.findall('object'):
            if member[0].text not in labels:
                labels.append(member[0].text)
    
    with open(os.path.join(export_dir, 'label_map.pbtxt'), 'w') as w:
        for i, label in enumerate(labels):
            w.writelines('item {\n    id: ' + str(i + 1) +  '\n    name: ' + label + '\n}\n\n')
    print(f'[INFO] label_map.pbtxt exported to {export_dir}')

def counter(path):
    """ Menghitung jumlah masing - masing label dari setiap xml file """
    count = {}
    for xml_file in glob.glob(path + '/*.xml'):
        root = ET.parse(xml_file).getroot()
        for member in root.findall('object'):
            if member[0].text in count:
                count[member[0].text] += 1
            else:
                count[member[0].text] = 1
    
    print('[INFO] Label Counter')
    for key, value in count.items():
        print(f'  - {key} : {value}')

def search(path, indexs):
    """ Mencari image yang memiliki label tertentu """
    images = {}
    for xml_file in glob.glob(path + '/*.xml'):
        images[os.path.basename(xml_file)] = []
        root = ET.parse(xml_file).getroot()
        for member in root.findall('object'):
            images[os.path.basename(xml_file)].append(member[0].text)

    print('[INFO] Label Finder')
    for label in indexs.split(','):
        print(f' {label} '.center(20, '#'))
        for img in [x for x, y in images.items() if label in y]:
            print(f' - {img}')
        print()

def lower(path):
    """ lowering all label in the xml files """
    for xml_file in glob.glob(path + '/*.xml'):
        root = ET.parse(xml_file).getroot()
        for member in root.findall('object'):
            member[0].text = member[0].text.lower()
        element = ET.tostring(root)

        with open(xml_file, "wb") as w:
            w.write(element)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Labeling helper script")
    parser.add_argument("-d",
                        "--img_dir",
                        help="Path to the folder where the images is stored.",
                        type=str)
    parser.add_argument("-l",
                        "--to_lower",
                        help="Lower all labels in xml files.",
                        action='store_true')
    parser.add_argument("-c",
                        "--counter",
                        help="Menghitung jumlah setiap label dari semua xml file.",
                        action='store_true')
    parser.add_argument("-s",
                        "--search",
                        help="Mencari image file yang mengandung label tertentu.",
                        type=str)
    parser.add_argument("-lm",
                        "--label_map",
                        help="Membuat label_map.pbtxt",
                        type=str)

    args = parser.parse_args()

    if args.img_dir is None:
        raise KeyError('Harus menyertakan -d argument atau folder dimana images disimpan')

    if args.to_lower:
        lower(args.img_dir)

    if args.counter:
        counter(args.img_dir)

    if args.search:
        search(args.img_dir, args.search)

    if args.label_map:
        make_labelmap(args.img_dir, args.label_map)
