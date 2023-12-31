from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


#Conexion con Edge
def Instagram_bot(user:str, passw:str,post:str,return_follow=False):
    driver2 = webdriver.Edge()
    driver2.get(post) # Url del post para extraccion de megustas
    time.sleep(5)

    #Incio de sesion
    xpath_expression = "//a[contains(text(), 'Iniciar sesión')]"
    inicio_sesion = driver2.find_element(By.XPATH,xpath_expression)
    inicio_sesion.click()
    time.sleep(1)

    #Login
    username = driver2.find_element('css selector',"input[name='username']")
    passw = driver2.find_element('css selector',"input[name='password']")
    username.send_keys(user)
    passw.send_keys(passw)
    driver2.find_element('css selector',"button[type='submit']").click()
    time.sleep(5)

    #Volver al post
    xpath_expression = "//div[contains(text(), 'Ahora no')]"
    driver2.find_element(By.XPATH,xpath_expression).click()
    time.sleep(3)
    #Var los me gusta
    xpath_expression = "//span[contains(text(), 'Me gusta')]"
    a=driver2.find_element(By.XPATH,xpath_expression).click()


    #Extraccion de me gusta
    time.sleep(5)
    identificador_me_gusta = 'x1dm5mii'
    lista = []

    while True:
        elementos = driver2.find_elements(By.CLASS_NAME,identificador_me_gusta)
        time.sleep(2)
        # lista +=[elementos]
        for x in elementos:

            try:
                # EXtraccion de nombre de las personas y cuentas
                if not x.text =='Seguir':
                    print(x.text)
                    lista +=[x.text]
                    
                    if return_follow == True:
                        try:
                            #Seguir a las personas del  post
                            if not x.text =='Pendiente' or x.text =='Siguiendo':
                                x.find_element('css selector',"button[type='button']").click()
                                time.sleep(0.2)
                        except:pass
            except:pass

        try:
            # Encuentra el elemento que contiene la barra (por ejemplo, mediante XPath)
            elemento_barra = driver2.find_element(By.XPATH,"//div[contains(@style, 'height: 356px; overflow: hidden auto;')]")

            # Ejecuta un script de JavaScript para desplazar la barra
            driver2.execute_script("arguments[0].scrollBy(0, 200);", elemento_barra)
            time.sleep(1)

            script = """
            var elem = arguments[0];
            var scrollableHeight = elem.scrollHeight - elem.clientHeight;
            var scrolled = elem.scrollTop;

            if (scrolled === scrollableHeight) {
                return true;  // La barra está al 100%
            } else {
                return false;  // La barra no está al 100%
            }
            """
            esta_al_100_por_ciento = driver2.execute_script(script, elemento_barra)
            if esta_al_100_por_ciento:
                break
                
        except Exception as e:
            print(f"No se pudo realizar el desplazamiento. Error: {e}")
            break

    time.sleep(10)
    print(lista)


#Ejecutor
if __name__ =='__main__':
    u = input('Escribe tu nombre de usuario o tu correo asociado a la cuenta: ')
    p = input('Escribe te contraseña: ')
    po = input ('Coloca la url del post que quieras extraer: ')
    f =  True if input ('Escribe "si" si quieres darle follow a las personas del post: ').lower() == "si" else False
    print(f)
    Instagram_bot(u,p,po,f)

