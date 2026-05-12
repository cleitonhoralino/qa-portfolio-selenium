from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# abrir navegador
navegador = webdriver.Chrome()

# acessar site
navegador.get("https://www.hashtagtreinamentos.com/")

# maximizar janela
navegador.maximize_window()

# clicar no botão verde
botao_verde = navegador.find_element(
    By.CLASS_NAME,
    "botao-verde"
)

botao_verde.click()

# encontrar vários elementos
lista_botoes = navegador.find_elements(
    By.CLASS_NAME,
    "header__titulo"
)

# clicar em "Assinatura"
for botao in lista_botoes:
    if "Assinatura" in botao.text:

        navegador.execute_script(
            "arguments[0].click();",
            botao
        )

        break

# trocar de aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# acessar página do curso
navegador.get(
    "https://www.hashtagtreinamentos.com/curso-python"
)

# preencher formulário
navegador.find_element(
    By.ID,
    "firstname"
).send_keys("Cleiton")

navegador.find_element(
    By.ID,
    "email"
).send_keys("testeautomatizado@python.com")

navegador.find_element(
    By.ID,
    "phone"
).send_keys("2199999999")

# espera inteligente
espera = WebDriverWait(navegador, 10)

# localizar botão
botao_quero_clicar = espera.until(
    EC.element_to_be_clickable(
        (By.ID, "_form_8834_submit")
    )
)

# scroll até botão
navegador.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    botao_quero_clicar
)

# pequeno delay
time.sleep(2)

# clicar via JavaScript
navegador.execute_script(
    "arguments[0].click();",
    botao_quero_clicar
)

# aguardar envio
time.sleep(3)

# voltar para tela inicial
navegador.get(
    "https://www.hashtagtreinamentos.com/"
)

# remover popup
try:
    navegador.execute_script("""
        let popup = document.getElementById('gtm-popup');

        if (popup) {
            popup.remove();
        }
    """)
except:
    pass

# aguardar carregamento
time.sleep(2)

# encontrar menus novamente
lista_botoes = navegador.find_elements(
    By.CLASS_NAME,
    "header__titulo"
)

# clicar em Blog
for botao in lista_botoes:

    if "Blog" in botao.text:

        navegador.execute_script(
            "arguments[0].click();",
            botao
        )

        break

# validar URL
assert "blog" in navegador.current_url

print("Teste executado com sucesso!")

# aguardar visualização
time.sleep(10)

# fechar navegador
navegador.quit()