from gspan_mining.config import parser
from gspan_mining.main import main

args_str = '-s 200 ./COX2_convert.txt'
FLAGS, _ = parser.parse_known_args(args=args_str.split())

gs = main(FLAGS)
