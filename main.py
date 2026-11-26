"""Write the out-of-office auto-reply line to /output/entry.txt."""

import os

LINE = (
    "Out of office until the 12th — urgent emails will be answered on my "
    "return, in the exact order they stopped being urgent."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
