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
    sync_parser = subparsers.add_parser("sync", help="Sync object metadata from Context7")
    sync_parser.add_argument("object", help="Name of the Max object to sync")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    if args.command == "new":
        from . import core
        core.create_project(args.name)
    elif args.command == "build":
        print(f"Building project {args.name}...")
    elif args.command == "validate":
        print(f"Validating project {args.name}...")
    elif args.command == "sync":
        print(f"Syncing object {args.object}...")

if __name__ == "__main__":
    main()
