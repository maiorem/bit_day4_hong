

class Menu:

    def __init__(self, n, p):
        self.name = n
        self.price = p

class Kiosk:

    def __init__(self, mlist):
        self.menu_list = mlist
        self.order_list = []

    def start_service(self):
        print("================================")
        print("WELCOME........")
        num = 1
        print("--------------------------------")
        for menu in self.menu_list:
            print(num, menu.name, menu.price)
            num += 1
        print("================================")
        choice = int(input("메뉴 번호를 선택하세요, 0을 누르면 완료: "))

        if choice == 0:
            return
        self.order_list.append(self.menu_list[choice -1])
        self.start_service()

    def print_bill(self):
        total = 0
        print("---------------------------------")
        for order_menu in self.order_list:
            print(order_menu.name, order_menu.price)
            total += order_menu.price
        print("---------------------------------")
        print("TOTAL : ", total)
        print("---------------------------------")


class MainKiost:

    def __init__(self, dic):
        self.kiosks = dic

    def service(self):
        idx = int(input("0.커피 1.베이커리 :"))
        kiosk = self.kiosks[idx]
        kiosk.start_service()
        kiosk.print_bill()

kiosk1 = Kiosk([
            Menu('Americano', 1500),
            Menu('Cafe Latte', 3000),
            Menu('Chocolate Latte', 3500),
            Menu('Milk Tea', 4000)
        ])
kiosk2 = Kiosk([
            Menu('샌드위치', 5000),
            Menu('치아바타', 4000),
            Menu('스콘', 3500),
            Menu('마들렌', 2000)
        ])

mainKiosk = MainKiost([kiosk1,kiosk2])
mainKiosk.service()
