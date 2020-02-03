import argparse

parser = argparse.ArgumentParser(prog='ParserSample',
                                 description='简单实例程序，学习如何解析命令行参数',
                                 epilog='很简单就可以学会')

parser.add_argument('greeting', type=str, help='问候信息，必需')
parser.add_argument('-fromm', default='yitian', type=str, help='发送人，默认是易天')
parser.add_argument('-to', default='everyone', type=str, nargs='*', help='接收人，默认是所有人')
parser.add_argument('-p', action='store_true', help='是否添加感叹号')

args = parser.parse_args()

output = f'{args.fromm} say {args.greeting} to {args.to}'
if args.p:
    output = output + '!'

print(output)
