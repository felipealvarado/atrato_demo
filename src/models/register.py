class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.email_txt = page.locator("input#emailOrPhone")
        self.btn_continue = page.locator(".MuiButton-root.MuiButton-text.MuiButtonBase-root.dAZREl.sc-dhKdcB > .MuiButton-label")
        self.cell_phone = page.locator("input#cellphone")
        self.password = page.locator("input#password")
        self.create_your_account_txt = page.locator(".eSqPcj.iwAtlF.sc-gsFSXq.sc-imWYAI")
        self.create_your_account_second_txt = page.locator(".eSqPcj.hbZTEb.sc-gsFSXq.sc-kAyceB")
        self.email_create_txt = page.locator("input#email")
        self.cellphone_create_txt = page.locator("input#cellphone")
        self.password_create_txt = page.locator("input#password")
        self.start_session_btn = page.locator(".MuiButton-label")



    async def navigate(self):
        await self.page.goto("https://app-beta.atratotech.com/v3/accounts/getstarted")

    async def register_email(self, email):
        await self.email_txt.fill(email)
        await self.btn_continue.click()
