"""
Script for labeling purposes

Usage :
    python label_processing.py -d [PATH TO IMAGES FOLDER] [PARAMS]

Parameters:
    -d : Path to the folder where the images is stored
    -l : Lower all labels in xml files.
    -c : Count each label of all the xml files
    -s : Find images with specific label
    -lm : Create label_map.pbtxt
    -ar : Remove xml piles without images

RangRang - Machine Learning - 2021
"""

import os, argparse, glob
import xml.etree.ElementTree as ET

def auto_remove(path):
    """ Menghapus file xml tanpa gambar """
    images = [os.path.splitext(x) for x in os.listdir(path)]
    images = [x for x, y in images]
    for x in set(images):
        if images.count(x) < 2:
            os.remove(os.path.join(path, x + '.xml'))

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
            w.writelines('item {\n    id: ' + str(i + 1) +  "\n    name: '" + label + "'\n}\n\n")
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
    for i, (key, value) in enumerate(count.items()):
        print(f'  {i + 1}. {key} : {value}')

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

def UA(path):
    """ lowering all label in the xml files """
    for xml_file in glob.glob(path + '/*.xml'):
        root = ET.parse(xml_file).getroot()
        img_file = list(os.path.splitext(os.path.basename(root.find('filename').text)))
        xml_file_ = list(os.path.splitext(os.path.basename(xml_file)))
        if img_file[0] != xml_file_[0]:
            img_file[0] = xml_file_[0]
            if os.path.isfile(os.path.join(path, img_file[0] + '.jpg')):
                img_file[1] = '.jpg'
            else:
                img_file[1] = '.jpeg'
            img_file = img_file[0] + img_file[1]
            root.find('filename').text = img_file

            print(f'[INFO] Writing {xml_file}')
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
                        help="Count each label of all the xml files",
                        action='store_true')
    parser.add_argument("-s",
                        "--search",
                        help="Find images with specific label",
                        type=str)
    parser.add_argument("-lm",
                        "--label_map",
                        help="Create label_map.pbtxt",
                        type=str)
    parser.add_argument("-ar",
                        "--auto_remove",
                        help="Delete xlm files without img",
                        action='store_true')
    parser.add_argument("-ua",
                        "--update_annotation",
                        help="Update annotation",
                        action='store_true')

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

    if args.auto_remove:
        auto_remove(args.img_dir)

    if args.update_annotation:
        UA(args.img_dir)