import asyncio


def main():
    print("Running...")
    try:
        main_event_loop = asyncio.get_event_loop()
        main_event_loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        print("Exiting...")


if __name__ == "__main__":
    main()
