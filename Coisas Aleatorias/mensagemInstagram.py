import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurações
ARQUIVO_CSV = "seguidores_ninh.404.csv"
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")
INTERVALO_ENTRE_USUARIOS = 60  # segundos
MENSAGEM_PADRAO = "Olá {nome}, tudo bem?"

# Carrega os dados do CSV
usuarios = []
with open(ARQUIVO_CSV, "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        usuarios.append({
            "username": linha["Username"],
            "nome": linha["Nome"].strip() or "amigo"
        })

# Inicia o navegador
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(1400, 870)
wait = WebDriverWait(driver, 20)

# Login
driver.get("https://www.instagram.com")
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USUARIO)
driver.find_element(By.NAME, "password").send_keys(SENHA)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').click()
time.sleep(10)

# Fecha pop-ups após login (se houver)
for _ in range(2):
    try:
        driver.find_element(By.XPATH, "//button[text()='Agora não']").click()
        time.sleep(2)
    except:
        pass

# Vai para a aba de mensagens
driver.get("https://www.instagram.com/direct/inbox/")
wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/direct/inbox')]")))
time.sleep(5)
# Fecha popup "Ativar notificações", se existir
try:
    btn_agora_nao = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Agora não']"))
    )
    btn_agora_nao.click()
    print("🔕 Popup de notificações fechado.")
    time.sleep(2)
except:
    pass

for pessoa in usuarios:
    username = pessoa["username"]
    nome = pessoa["nome"]
    mensagem = MENSAGEM_PADRAO.format(nome=nome)

    print(f"\n📨 Enviando mensagem para @{username}...")

    try:
        # Clica no botão de nova mensagem (ícone de lápis)
        novo_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Nova mensagem"]')))
        novo_btn.click()
        time.sleep(3)

        # Digita o nome do usuário
        campo_para = wait.until(EC.presence_of_element_located((By.NAME, "queryBox")))
        campo_para.clear()
        campo_para.send_keys(username)
        time.sleep(3)

        # Seleciona o primeiro resultado
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//div[@role='button']"))).click()
        time.sleep(1)

        # Clica no botão "Bate-papo"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//div[text()='Bate-papo']"))).click()
        time.sleep(5)

        # Digita a mensagem
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        textarea.send_keys(mensagem)
        time.sleep(1)

        # Clica no botão de enviar (ícone de avião)
        botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        botao_enviar.click()
        print(f"✅ Mensagem enviada para @{username}: {mensagem}")

    except Exception as e:
        print(f"❌ Erro ao enviar para @{username}: {e}")

    print("⏳ Aguardando antes de enviar a próxima mensagem...\n")
    time.sleep(INTERVALO_ENTRE_USUARIOS)

driver.quit()
print("✅ Processo finalizado com sucesso.")
