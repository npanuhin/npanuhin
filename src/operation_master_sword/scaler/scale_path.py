import xml.etree.ElementTree as ET
from SVGPath.SVGPath import SVGPath


ET.register_namespace('', 'http://www.w3.org/2000/svg')

tree = ET.parse('input.svg')
root = tree.getroot()

if 'data-name' in root.attrib:
    del root.attrib['data-name']

# root.attrib['viewBox'] = ' '.join(
#     str(int(item) * COEFF) for item in root.attrib['viewBox'].split()
# )

for elem in root.iter():
    if not elem.tag.endswith('path'):
        continue

    initial_path = elem.attrib['d']
    with open("initial_path.txt", "w") as file:
        file.write(initial_path)

    path = SVGPath(initial_path)
    with open("result_path.txt", "w") as file:
        file.write(path.minify())
    assert path.minify() == initial_path

    # path.round(3)

    all_args = sorted(set(abs(arg) for item in path.d for arg in item.args))
    print(all_args)
    print()

    path.round(3)
    path.strip_less(0.028, absolute=True)

    all_args = sorted(set(abs(arg) for item in path.d for arg in item.args))
    print(all_args)

    print(len(all_args))

    result_path = path.minify()
    with open("result_path.txt", "w") as file:
        file.write(result_path)

    elem.attrib['d'] = result_path

tree.write('result.svg', encoding='utf-8', xml_declaration=True)
