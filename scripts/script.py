import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("issue_number", type=str, help="Issue number")
    args = parser.parse_args()

    print(args.issue_number)