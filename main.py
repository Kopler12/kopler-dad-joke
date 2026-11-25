import os

JOKE = (
    "My fridge won't talk to me anymore. I only ever show up when I want "
    "something, and I never call just to chat. So now it just gives me the "
    "cold shoulder."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
