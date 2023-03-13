import csv
import datetime

# Pizza tabanları için üst sınıf olan Pizza'nın oluşumu.
class Pizza():
    # Bu sınıftan oluşan pizzaya açıklama ve fiyat bilgisi gönderilir.
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost

    # Sınıf içinde gizli tutulan cost ve description değerlerini okumaya yarayan fonksiyonlarımız.
    def get_cost(self):
        return self.__cost
    
    def get_description(self):
        return self.__description

class KlasikPizza(Pizza):
    # Bu pizza tabanının açıklaması ve fiyat bilgisini tutan gizli değişkenler.
    __description = "Klasik Pizza"
    __cost = 85
    
    # Bu pizzadan yapıcı fonksiyon oluştuğunda pizza tabanı ile bilgiler Pizza sınıfında tutulmak üzere gönderilir.
    def __init__(self):
        super().__init__(self.__description, self.__cost)

class Margarita(Pizza):
    __description = "Margarita"
    __cost = 90
    
    def __init__(self):
        super().__init__(self.__description, self.__cost)

class  TürkPizza(Pizza):
    __description = " TürkPizza"
    __cost = 99
    
    def __init__(self):
        super().__init__(self.__description, self.__cost)

class  SadePizza(Pizza):
    __description = " SadePizza"
    __cost = 70
    
    def __init__(self):
        super().__init__(self.__description, self.__cost)

# Tüm Pizza değişkenlerini, eklemelerini tutacak olan ana sınıf.
class Decorator(Pizza):
    # Bu sınıfın constructor metodunda parametre olarak bir pizza alır. (component)
    # İlgili değişkenin açıklamsı ve fiyatı da parametre olarak aktarılır.
    def __init__(self, component, description, cost):
        # Parametre olarak gelen component değeri, sınıfın component değişkenine aktarılıyor.
        self.__component = component
        super().__init__(description, cost)
    
    # Toplam fiyatı döndüren fonksiyon.
    def get_cost(self):
        return self.__component.get_cost() + Pizza.get_cost(self)
    
    # Bağlanan component açıklamasını ve değişken/sos açıklamasını birlikte döndüren fonksiyon.
    def get_description(self):
        return self.__component.get_description() + ' ' + Pizza.get_description(self)

# Decorator sınıfına bağlı Zeytin değişkeni.
class Zeytin(Decorator):
    # Bu eklemenin açıklaması ve fiyat bilgisi gizli olarak tutulmaktadır.
    __description = 'Zeytin'
    __cost = 8
    
    # Sınıftan bir nesne oluşurken, değişkenin etki edeceği pizza component değişkeni tarafından tutulur.
    def __init__(self, component):
        # Decorator sınıfına parametreleri vererek Decorator sınıfının get_description ve get_cost metodlarını düzgün bir biçimde kullanır oluruz.
        super().__init__(component, self.__description, self.__cost)

class KeçiPeyniri(Decorator):
    __description = 'Keçi Peyniri'
    __cost = 8
    
    def __init__(self, component):
        super().__init__(component, self.__description, self.__cost)

class Et(Decorator):
    __description = 'Et'
    __cost = 9
    
    def __init__(self, component):
        super().__init__(component, self.__description, self.__cost)

class Soğan(Decorator):
    __description = 'Soğan'
    __cost = 5
    
    def __init__(self, component):
        super().__init__(component, self.__description, self.__cost)

class Mısır(Decorator):
    __description = ' Mısır'
    __cost = 6
    
    def __init__(self, component):
        super().__init__(component, self.__description, self.__cost)

class Mantar(Decorator):
    # Bu eklemenin açıklaması ve fiyat bilgisi gizli olarak tutulmaktadır.
    __description = 'Mantar'
    __cost = 15
    
    # Sınıftan bir nesne oluşurken, değişkenin etki edeceği pizza component değişkeni tarafından tutulur.
    def __init__(self, component):
        # Decorator sınıfına parametreleri vererek Decorator sınıfının get_description ve get_cost metodlarını düzgün bir biçimde kullanır oluruz.
        super().__init__(component, self.__description, self.__cost)

def print_menu():
    with open('menu.txt', 'r', encoding='utf-8') as file:
        print(file.read())
        
def show_pizza(pizza):
    print("Oluşturulan Pizza:", pizza.get_description())
    print("Pizzanın Ücreti:", pizza.get_cost())
    
    print("_.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._")
    print("_.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._")
    print("_.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._")

    print("Ödeme bilgilerini giriniz;")
    isim = input("İsminizi giriniz: ")
    soyisim = input("Soyisminizi giriniz: ")
    tc = int(input("TC Kimlik No giriniz: "))
    kartNo = input("Kart Numarası giriniz: ")
    kartŞifre = input("Kart Şifresi giriniz: ")
    
    with open("Orders_Database.csv", "a", encoding="utf-8") as database: #CSV dosyamız
        başlık = ['İsim', 'Soyisim', 'TC', 'Kart Numarası', 'Kart Şifresi', 'Pizza Açıklama', 'Pizza Fiyat', 'Zaman']
        writer = csv.DictWriter(database, fieldnames=başlık)
        
        # Eğer dosya ilk defa oluşmuş ise başlıkları yaz.
        if database.tell() == 0:
            writer.writeheader()
        
        # Verileri yaz:
        writer.writerow({
            'İsim' : isim,
            'Soyisim' : soyisim,
            'TC' : tc,
            'Kart Numarası' : kartNo,
            'Kart Şifresi' : kartŞifre,
            'Pizza Açıklama' : pizza.get_description(),
            'Pizza Fiyat' : pizza.get_cost(),
            'Zaman' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

def main():    
    while True:
        print_menu()
        
        pizzaTabanı = int(input("Pizza Tabanı: "))
        
        if pizzaTabanı == 1:
            pizzaTabanı = KlasikPizza()
        elif pizzaTabanı == 2:
            pizzaTabanı = Margarita()
        elif pizzaTabanı == 3:
            pizzaTabanı = TürkPizza()
        elif pizzaTabanı == 4:
            pizzaTabanı = SadePizza()
        else:
            print("Hatalı sos seçimi, tekrar seçime yönlendiriliyorsunuz...")
            continue
        
        sos = int(input("Sos: "))
        
        if sos == 11:
            pizza = Zeytin(pizzaTabanı)
            show_pizza(pizza)
        elif sos == 12:
            pizza = Mantar(pizzaTabanı)
            show_pizza(pizza)
        elif sos == 13:
            pizza = KeçiPeyniri(pizzaTabanı)
            show_pizza(pizza)
        elif sos == 14:
            pizza = Et(pizzaTabanı)
            show_pizza(pizza)
        elif sos == 15:
            pizza = Soğan(pizzaTabanı)
            show_pizza(pizza)
        elif sos == 16:
            pizza = Mısır(pizzaTabanı)
            show_pizza(pizza)
        else:
            print("Hatalı sos seçimi, tekrar seçime yönlendiriliyorsunuz...")
            continue
        
        tuş = input("Tekrar pizza seçmek için e tuşuna basınız: ")
        
        if tuş == 'e' or tuş == 'E':
            continue
        else:
            break

if __name__ == "__main__":
    main()
