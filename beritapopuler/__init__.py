import requests
from bs4 import BeautifulSoup

description = 'To get most popular news in Indonesia from detik.com'


def ekstraksi_data():
    try :
        content = requests.get('https://detik.com')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'box cb-mostpop'})
        result = result.find('div', {'class': 'list-content'})
        result = result.findChildren ('a')
        i = 0
        for res in result :
            if i == 0 :
                pop1 = res.text
            elif i == 1:
                pop2 = res.text
            elif i == 2:
                pop3 = res.text
            elif i == 3:
                pop4 = res.text
            elif i == 4 :
                pop5 = res.text
            i = i + 1

        hasil = dict ()
        hasil ['pop1'] = pop1
        hasil ['pop2'] = pop2
        hasil ['pop3'] = pop3
        hasil ['pop4'] = pop4
        hasil ['pop5'] = pop5
        return hasil
    else :
        return None


def tampilkan_data(result):
    if result is None :
        print("Tidak bisa menampilkan data")
        return
    print('Berita Terpopuler Detik.com')
    print(f"#1 :{result['pop1']}")
    print(f"#2 :{result['pop2']}")
    print(f"#3 :{result['pop3']}")
    print(f"#4 :{result['pop4']}")
    print(f"#5 :{result['pop5']}")


if __name__ == '__main__' :
    result = ekstraksi_data ()
    tampilkan_data(result)