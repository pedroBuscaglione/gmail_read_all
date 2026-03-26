import time
import pyautogui as py

def main():

    py.click(x=458, y=734)
    time.sleep(2)

    py.click(x=414, y=17)
    time.sleep(1)

    for _ in range(120):
        py.click(x=205, y=202)
        time.sleep(3)

        py.click(x=273, y=232)
        time.sleep(3)

        py.click(x=1209, y=204)
        time.sleep(3)

if __name__ == "__main__":
    main()