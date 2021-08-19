from pygments import highlight
from pygments.lexers import YamlLexer
from pygments.formatters import TerminalFormatter
import re
import yaml
class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def _padleft(val, amount):
    strlen = len(val) + amount
    return val.rjust(strlen)

def out(val, indent=None, spacing=None):

    spacing_was_default = False
    indent_was_default = False

    if (indent is None):
        indent = 2
        indent_was_default = True

    if (spacing is None):
        spacing_was_default = True
        spacing = 2
        listspacing = 1

    if (type(val) is list):
        for s in val:
            if (indent_was_default == False):
                strlen = len(s)+indent
                print(f"- {s.rjust(strlen)}")
            else:
                print(f"- {s.rjust(len(s) + 4)}")
            if (spacing_was_default == False):
                for _ in range(1,spacing):
                    print()
    elif (type(val) is str):
        strlen = len(val)+indent
        print(val.rjust(strlen))
        for _ in range(1,spacing):
            print()
    
    elif (type(val) is dict):
        print()
        # print(highlight("\n".join(list(map(lambda x: f"  {x}", yaml.dump(val).split("\n")))), YamlLexer(), TerminalFormatter()))
        output = highlight(yaml.dump(val, default_flow_style=False, indent=2, Dumper=MyDumper), YamlLexer(), TerminalFormatter())
        padded = "\n".join(list(map(lambda x: f"  {x}", output.split("\n"))))
        print(re.sub("^\n", '', padded))

    elif (isinstance(val, type({}.keys()))):
        out(list(val))

def print_yaml_section(val, extra_top=None):
    output = highlight(yaml.dump(val, default_flow_style=False, indent=2, Dumper=MyDumper), YamlLexer(), TerminalFormatter())
    padded = "\n".join(list(map(lambda x: f"  {x}", output.split("\n"))))
    print(re.sub("^\n", '', padded))
    