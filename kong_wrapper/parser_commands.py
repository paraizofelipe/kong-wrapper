import yaml
import argparse
import simplejson as json
from kong_wrapper.utils import read_conf
from pygments import highlight, lexers, formatters


class Command:

    def __init__(self, file_path):
        self.info_file = self.parser_file(file_path)
        # print(self.info_file)

    @staticmethod
    def show_json(json):
        colorful_json = highlight(json.encode('UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
        print(colorful_json)

    @staticmethod
    def parser_file(file_path):
        with open(file_path) as command_file:
            info = yaml.load(command_file)
            return info

    @staticmethod
    def extract_defines(ref, defines):
        args = []
        for define in defines:
            if ref in define:
                for arg in define[ref]['arguments']:
                    args.append(arg)
        return args

    def load_program(self):
        parser = argparse.ArgumentParser(description=self.info_file['description'])
        subparser = parser.add_subparsers(help="Commands")

        for arg in self.info_file['arguments']:
            parser.add_argument(arg['name'], help=arg['help'])

        for command in self.info_file['commands']:
            object_actions_ = command['actions'].__class__()
            aux_parser = subparser.add_parser(command['name'], help=command['help'])
            aux_sub_parser = aux_parser.add_subparsers(help='Commands')

            for sub_command in command['subcommands']:
                aux_sub_command = aux_sub_parser.add_parser(sub_command['name'], help=sub_command['help'])

                if {"arguments"}.issubset(sub_command):
                    for arg in sub_command['arguments']:
                        if 'define' in arg:
                            args_defines = self.extract_defines(arg['define'], self.info_file['define'])
                            for arg_define in args_defines:
                                aux_sub_command.add_argument(arg_define['name'], **arg_define['params'])
                        else:
                            aux_sub_command.add_argument(arg['name'], **arg['params'])

                if {"exec"}.issubset(sub_command):
                    func_exec = getattr(object_actions_, sub_command['exec'])
                else:
                    func_exec = getattr(object_actions_, sub_command['name'])
                aux_sub_command.set_defaults(func=func_exec)

        args = parser.parse_args()

        try:
            cli_conf = read_conf('default')
            if not args.host or not args.port:
                if cli_conf and cli_conf["host"] and cli_conf["port"]:
                    args.host = cli_conf["host"]
                    args.port = cli_conf["port"]

                    try:
                        result_request = args.func(args)
                        result_request = json.dumps(result_request, sort_keys=True, indent=True)
                        # print(result_request)
                        self.show_json(result_request)
                    except Exception as error:
                        raise error

                else:
                    raise argparse.ArgumentError(subparser, "host and port values have not been defined.")
        except FileNotFoundError:
            print('The file ".kong" not found in directory "home" of user!')
        except Exception as error:
            raise error


if __name__ == "__main__":
    command = Command("command.yaml")
    command.load_program()