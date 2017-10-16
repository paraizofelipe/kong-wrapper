import yaml
import argparse


class Command:

    def __init__(self, file_path):
        self.info_file = self.parser_file(file_path)
        print(self.info_file)

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
            aux_parser = subparser.add_parser(command['name'], help=command['help'])
            aux_sub_parser = aux_parser.add_subparsers(help='Commands')

            for sub_command in command['subcommands']:
                aux_sub_command = aux_sub_parser.add_parser(sub_command['name'], help=sub_command['help'])

                for arg in sub_command['arguments']:
                    if 'define' in arg:
                        args_defines = self.extract_defines(arg['define'], self.info_file['define'])
                        for arg_define in args_defines:
                            aux_sub_command.add_argument(arg_define['name'], **arg_define['params'])
                    else:
                        aux_sub_command.add_argument(arg['name'], **arg['params'])

        args = parser.parse_args()


if __name__ == "__main__":
    command = Command("command.yaml")
    command.load_program()