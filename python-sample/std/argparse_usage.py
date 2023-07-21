# %%
import argparse

# py argparse_usage.py -h

parser = argparse.ArgumentParser(
    prog="ParserSample", description="简单示例程序，学习如何解析命令行参数", epilog="很简单就可以学会"
)

parser.add_argument("greeting", type=str, help="问候信息，必需")
parser.add_argument(
    "-fromm", "-f", default="techstay", type=str, help="发送人，默认是techstay"
)
parser.add_argument(
    "-to", "-t", default="everyone", type=str, nargs="*", help="接收人，默认是所有人"
)
parser.add_argument("-p", action="store_true", help="是否添加感叹号")

# %%
parser.parse_args(["-h"])

# %%
parser.parse_args("helloworld".split(" "))
# %%
parser.parse_args("666 -f jack -t tom -p".split(" "))
# %%
