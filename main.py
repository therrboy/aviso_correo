from bs4 import BeautifulSoup
import requests
import smtplib
import os


os.environ["to_email"] = "correoprueba@hotmail.com"
os.environ["password"] = "contraseñaprueba"
os.environ["email"] = "rodrigoradattitrabajo@hotmail.com"

to_email = os.environ["to_email"]
password = os.environ["password"]
email = os.environ["email"]

valor_deseado = 150
URL = "https://www.amazon.com/-/es/multiusos-programable-calentador-esterilizador-inoxidable/dp/B06Y1MP2PY/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B06Y1MP2PY&psc=1&pd_rd_w=0mKNs&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=NFZ2CBARMCZ3YTJ8RSRS&pd_rd_wg=rJiLy&pd_rd_r=964307ec-d2a3-4372-b832-bd182841a8b1&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699"

headers = {
    "Accept-Language": "es-ES,es;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

responce = requests.get(URL, headers=headers)

soup = BeautifulSoup(responce.content, "lxml")


valor = soup.find(class_="a-price-whole").getText()

valor_puro = int(valor.replace(".", ""))


mensaje = f"El precio bajo, ahora vale {valor_puro} puedes comprarlo"

if valor_puro <= valor_deseado:
    connection = smtplib.SMTP("smtp-mail.outlook.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=to_email,
    msg=f"Subject:Amazon Price Drop Alert\n\nYour ELECTRODOMESTIC, is now available for just $100")
