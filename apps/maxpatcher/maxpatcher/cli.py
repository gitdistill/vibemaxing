import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="MaxPatcher CLI")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # new command
    new_parser = subparsers.add_parser("new", help="Create a new MaxPatcher project")
    new_parser.add_argument("name", help="Name of the project")
    
    # build command
    build_parser = subparsers.add_parser("build", help="Build a MaxPatcher project")
    build_parser.add_argument("name", help="Name of the project")
    
    # validate command
    validate_parser = subparsers.add_parser("validate", help="Validate a generated patch")
    validate_parser.add_argument("name", help="Name of the project")
    
    # sync command
    sync_parser = subparsers.add_parser("sync", help="Sync project metadata with Context7 intelligence")
    sync_parser.add_argument("name", help="Name of the project")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    if args.command == "new":
        from . import core
        core.create_project(args.name)
    elif args.command == "build":
        from . import core
        core.build_project(args.name)
    elif args.command == "validate":
        from . import core
        core.validate_project(args.name)
    elif args.command == "sync":
        from . import core
        core.sync_project(args.name)

if __name__ == "__main__":
    main()
