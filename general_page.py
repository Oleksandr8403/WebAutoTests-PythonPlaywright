from playwright.sync_api import expect


class GeneralPageLinks:
    def __init__(self, page, link_sait):
        self.page = page
        self.link_sait = link_sait

    def goto(self):
        self.page.goto(self.link_sait)

    # check upper line with links
    def verify_and_click_main_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Головна", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/')
        link.click()
        expect(self.page).to_have_url(self.link_sait)
        expect(self.page.get_by_role("heading", name="Український сервер Lineage 2")).to_be_visible()
        self.page.wait_for_timeout(1000)

    def verify_and_click_files_upper_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Файли", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=file')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "file")
        expect(self.page.get_by_role("heading", name="Файли для гри в Lineage")).to_be_visible()

    def verify_and_click_cabinet_upper_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Особистий кабінет", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=cabinet')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "cabinet")
        expect(self.page.get_by_role("link", name="Авторизуйтесь")).to_be_visible()

    def verify_and_click_donate_upper_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Пожертвування", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=pogertv')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "pogertv")
        expect(self.page.get_by_role("heading", name="Пожертва на розвиток сервера")).to_be_visible()

    # check left side links
    def verify_and_click_begin_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="ЯК ПОЧАТИ ГРАТИ", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=begin')
        link.click()
        expect(self.page).to_have_url(self.link_sait + 'begin')
        expect(self.page.get_by_role("heading", name="Почати грати в Lineage")).to_be_visible()

    def verify_and_click_registration_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="РЕЄСТРАЦІЯ", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=reg')
        link.click()
        expect(self.page).to_have_url(self.link_sait + 'reg')
        expect(self.page.get_by_role("heading", name="Реєстрація в Lineage 2 High")).to_be_visible()

    def verify_and_click_files_left_side_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="ФАЙЛИ", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=file')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "file")
        expect(self.page.get_by_role("heading", name="Файли для гри в Lineage")).to_be_visible()

    def verify_and_click_security_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Безпека", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=security')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "security")
        expect(self.page.get_by_role("heading",
                                     name="Необхідні заходи безпеки для збереження ваших персонажів")).to_be_visible()

    def verify_and_click_rules_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Правила", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=rules')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "rules")
        expect(self.page.get_by_role("heading", name="Правила сервера")).to_be_visible()

    def verify_and_click_serv30_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Сервер х30", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv30')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv30")
        expect(self.page.get_by_role("heading", name="Сервер Lineage 2 Мультипрофа")).to_be_visible()

    def verify_and_click_serv51_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Сервер х51", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv51")
        expect(self.page.get_by_role("heading", name="Lineage 2 High Five")).to_be_visible()

    def verify_and_click_serv1k_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Сервер х1000 (x1)", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv1k')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv1k")
        expect(self.page.get_by_role("heading", name="Lineage 2 х1-х1000 ПВП сервер")).to_be_visible()

    def verify_and_click_serv5_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Сервер х5", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv5')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv5")
        expect(self.page.get_by_role("heading", name="С4 класичний на клієнті High")).to_be_visible()

    def verify_and_click_donate_left_side_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Зробити АпГрейд до Фул Чара", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=pogertv')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "pogertv")
        expect(self.page.get_by_role("heading", name="Пожертва на розвиток сервера")).to_be_visible()

    def verify_and_click_pvp_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Топ ПвП", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=pvp&id=x51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "pvp-x51")
        expect(self.page.get_by_role("heading", name="Рейтинг гравців по кількості ПВП в Lineage")).to_be_visible()

    def verify_and_click_pk_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Топ ПК", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=pk&id=x51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "pk-x51")
        expect(self.page.get_by_role("heading", name="Рейтинг ПК")).to_be_visible()

    def verify_and_click_time_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Топ Часу", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=time&id=x51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "time-x51")
        expect(self.page.get_by_role("heading", name="Найулюбленіші наші гравці. Топ по часу у грі")).to_be_visible()

    def verify_and_click_clans_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Клани", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=clans&id=x51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "clans-x51")
        expect(self.page.get_by_role("heading", name="Рейтинг кланів на сервері")).to_be_visible()

    def verify_and_click_castle_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Замки", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=castle&id=x51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "castle-x51")
        expect(self.page.get_by_role("heading", name="Статистика Замків")).to_be_visible()

    def verify_and_click_cabinet_left_side_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Вхід у кабінет", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=autoriz')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "autoriz")
        expect(self.page.get_by_role("heading", name="Вхід у кабінет")).to_be_visible()

    def verify_and_click_forgot_pass_link(self):
        self.goto()
        link = self.page.get_by_role("link", name="Забули пароль?", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=lostpass')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "lostpass")
        expect(self.page.get_by_role("heading", name="Восстановление пароля")).to_be_visible()

