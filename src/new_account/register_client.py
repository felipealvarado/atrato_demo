from src.models.register import RegisterPage
from playwright.async_api import async_playwright, expect
import pytest
from random import randint


@pytest.mark.parametrize("wwith,height", [
    (1366, 768)
])
@pytest.mark.asyncio
async def test_register_client(wwith, height):
    range_start = 10**(10-1)
    range_end = (10**10)-1
    tag_email = randint(range_start, range_end)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=5000)
        context = await browser.new_context(viewport={"width": wwith, "height": height})
        page = await context.new_page()
        register_page = RegisterPage(page)
        await register_page.navigate()
        await register_page.register_email('mcdfelipea+{}@gmail.com'.format(tag_email))
        await expect(register_page.create_your_account_txt).to_have_text("Crea una cuenta")
        await expect(register_page.create_your_account_second_txt).to_have_text("Crea un usuario para registrarte y poder comprar con Atrato")
        await expect(register_page.email_create_txt).to_be_visible()
        await expect(register_page.cellphone_create_txt).to_be_visible()
        await expect(register_page.password_create_txt).to_be_visible()
        await context.close()
        await browser.close()
