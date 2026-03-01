import asyncio
from playwright.async_api import async_playwright

async def validar_roteamento():
    configuracao_proxy = {
        "server": "http://endereco_do_proxy:porta",
        "username": "seu_usuario",
        "password": "sua_senha"
    }

    async with async_playwright() as p:
        navegador = await p.chromium.launch(
            headless=True,
            proxy=configuracao_proxy
        )
        
        contexto = await navegador.new_context()
        pagina = await contexto.new_page()
        
        await pagina.goto("https://api.ipify.org")
        ip_detectado = await pagina.inner_text("body")
        
        print("Saida de rede operando com o IP:", ip_detectado)
        
        await navegador.close()

asyncio.run(validar_roteamento())