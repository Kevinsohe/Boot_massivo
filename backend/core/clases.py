import pandas as pd
from datetime import datetime
from pathlib import Path
import re
import pyautogui
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Agenda:
    def __init__(self,max: int=100,backup_route: str="backup"):
        self.contacts={}
        self.max=max
        self.date_create=datetime.now()
        self.date_change = None
        self.backup_route = backup_route
        Path(self.backup_route).mkdir(parents=True, exist_ok=True)

    def add(self,nombre:str,telefono:str):
        if len(self.contacts)>=self.max:
            return 100
        elif not telefono.isdigit():
            return 200
        elif nombre in self.contacts:
            return 300
        else:
            self.contacts[nombre] = telefono
            self.date_change= datetime.now()
            return 1

    def delete(self, nombre: str):
        if nombre in self.contacts:
            del self.contacts[nombre]
            self.fecha_modificacion = datetime.now()
            return 1
        else:
            return 400
    
    def edit(self, nombre: str, nuevo_telefono: str):
        self.delete(nombre)
        self.add(nombre,nuevo_telefono)
    
    def import_contacts(self, route: str):
        cols = ["First Name","Middle Name","Last Name","Phone 1 - Value"]
        datos = pd.read_csv(route, usecols=cols)
        datos["Full Name"] = datos["First Name"].fillna("") + " " + datos["Middle Name"].fillna("") + " " + datos["Last Name"].fillna("")
        datos["Full Name"] = datos["Full Name"] .str.strip()
        for row in datos.itertuples():
            name=re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', f"{row._5}")
            telf=f"{row._4}".strip()[-8:]
            self.add(name,telf)

    def export_contacts(self,csv_name: str):
        columnas = ["First Name", "Middle Name", "Last Name", "Phonetic First Name", "Phonetic Middle Name",
        "Phonetic Last Name", "Name Prefix", "Name Suffix", "Nickname", "File As",
        "Organization Name", "Organization Title", "Organization Department", "Birthday",
        "Notes", "Photo", "Labels", "E-mail 1 - Label", "E-mail 1 - Value",
        "Phone 1 - Label", "Phone 1 - Value", "Phone 2 - Label", "Phone 2 - Value"]
        df = pd.DataFrame(columns=columnas)
        df["First Name"] = list(self.contacts.keys())
        df["Phone 1 - Value"] = list(self.contacts.values())
        df.to_csv(f"backup\\{csv_name}.csv", index=False, encoding='utf-8')

    def backup_contacts(self):
        time=str(datetime.now()).replace(":", "")
        backup_name=f"Backup {time}"
        self.export_contacts(backup_name)
        
    def show(self,n:int=5):
        df = pd.DataFrame(self.contacts.items(), columns=['Nombre', 'Telefono'])
        print(df.head(n))


"""route_test="C:\\Users\\usuario\\Downloads\\contacts.csv"
Agenda1=Agenda()
Agenda1.import_contacts(route_test)
Agenda1.show(20)
Agenda1.export_contacts("Prueba1")
Agenda1.backup_contacts()
print(Agenda1.contacts)"""

WINDOWS_UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
MAC_UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:109.0) Gecko/20100101 Firefox/116.0"
ANDROID_UA="Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
IOS_UA="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
UA=[{"agent":WINDOWS_UA,"x_size":1380,"y_size":780},
    {"agent":MAC_UA,"x_size":1440,"y_size":900},
    {"agent":ANDROID_UA,"x_size":412,"y_size":915},
    {"agent":IOS_UA,"x_size":390,"y_size":844}]

class BootMassivo:
#NOTA: Quedò pendiente conseguir iniciar secion desde algun usuario previuamente creado (Quitar cosas innecesarias del __init__)
    
    def __init__(self,agent_code:int=0,level_random:int=5,min_delay:int=2,max_delay:int=6,max_retries:int=10):
        #Atributos
        self.is_active=True
        self.level_random=level_random
        self.min_delay=min_delay
        self.max_delay=max_delay
        self.max_retries=max_retries
        self.agent=UA[agent_code]["agent"]
        self.x_size=UA[agent_code]["x_size"]
        self.y_size=UA[agent_code]["y_size"]      
        
        options = Options()
        options.add_argument(f"user-agent={self.agent}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        profile_path = "C:\\Users\\usuario\\AutomationProfile"
        os.makedirs(profile_path, exist_ok=True)
        options.add_argument(f"--user-data-dir={profile_path}")

        service = Service(
            executable_path="backend\\chromedriver.exe",
            service_args=["--verbose", "--log-path=chromedriver.log"]
        )


        self.driver=webdriver.Chrome(options=options,service=service) 
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.set_window_size(self.x_size,self.y_size)

    def tipear(self,element,string):
        for char in string:
            element.send_keys(char)
            delay=random.uniform(0.2,0.3)
            time.sleep(delay)
            if random.random() < min((self.level_random/10),0.3):
                element.send_keys(Keys.BACKSPACE)
                time.sleep(random.uniform(0.1, 0.5))
                element.send_keys(char)


    def open_whatsapp(self):
        try:
            self.driver.get("https://web.whatsapp.com")
            time.sleep(15+random.random()*self.level_random)
        except:
            print("Se presentaron problemas para abrir https://web.whatsapp.com")
    
    def open_chat(self,cell_phone,contact_name):
        try:
            search_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            search_box.click()
            time.sleep((random.uniform(self.min_delay,self.max_delay))/2)
            self.tipear(search_box,cell_phone)
            time.sleep((random.uniform(self.min_delay,self.max_delay))/2)
            try:
                chat = self.driver.find_element(By.XPATH, f'//span[contains(@title, "+591 {cell_phone}")]')
                chat.click()
            except:
                print("Número no encontrado")
                try:
                    chat = self.driver.find_element(By.XPATH, f'//span[contains(@title, "{contact_name}")]')
                    chat.click()
                except:
                    print("Nombre no encontrado")
        except:
            print("Buscador no encontrado")    

    def send_text(self,text):
        try:
            caja = self.driver.find_element(By.XPATH,'//div[@contenteditable="true"][@data-tab="10"]')
            caja.click()
            self.tipear(caja,text)
            caja.send_keys(Keys.ENTER)
            caja.clear()
        except:
            print("Caja de mensajes no encontrada")
"""    def send_picture(self,route):
        try:

            adjuntar = self.driver.find_element(By.XPATH, '//div[@title="Adjuntar"]')
            adjuntar.click()
            

            input= self.driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            self.tipear(input,route)
            
            time.sleep(random.uniform(self.min_delay,self.max_delay)) 
            

            boton_enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            boton_enviar.click()
        except:
            print("Lorem Ipsun")"""

Armando=BootMassivo()
Armando.open_whatsapp()
Armando.open_chat(cell_phone="60991159",contact_name="")
Armando.send_text("")
