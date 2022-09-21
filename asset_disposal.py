import argparse


class Tools:
    name = ""
    name2 = ""

    def __init__(self, filename1, filename2):
        self.name = filename1
        self.name2 = filename2

    def remove(self):
        with open(self.name, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            number = 0
            for i in lines:
                if "http://" in i:
                    lines[number] = i.replace("http://", "")
                elif "https://" in i:
                    lines[number] = i.replace("https://", "")
                number = number + 1
            print(lines)
        # 去除前缀后，以列表创建集合并去重
        domain = set(lines)
        with open(self.name2, 'w', encoding='utf-8') as f2:
            for domain2 in domain:
                f2.write(domain2 + '\n')
        # print(lines)

    def quchong(self):

        with open(self.name, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            text = set(lines)
            with open(self.name2, 'w', encoding='utf-8') as f2:
                for text2 in text:
                    f2.write(text2 + '\n')


def main():
    parser = argparse.ArgumentParser(prog='IP域名去重脚本',
                                     usage='例如去重：python args_demo.py -f filename.txt -q 1 -o quchong.txt')
    parser.add_argument("-f", "--file", default="text.txt", help="输入待去重文本路径")
    parser.add_argument("-o", "--output", default="text2.txt", help="输出去重后文件名")
    parser.add_argument("-r", "--remove", help="去除http或https前缀 -r 1", type=int)
    parser.add_argument("-q", "--quchong", help="批量去重域名IP -q 1", type=int)
    args = parser.parse_args()
    if args.quchong == 1:
        tool = Tools(args.file, args.output)
        tool.quchong()
    elif args.remove == 1:
        tool = Tools(args.file, args.output)
        tool.remove()


if __name__ == '__main__':
    main()
