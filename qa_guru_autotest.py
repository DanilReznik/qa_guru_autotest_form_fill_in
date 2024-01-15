from selene import browser, be


def test_selene():
    browser.open_url('https://demoqa.com/text-box')
    browser.element('[type="text"]').should(be.blank).type("Danil Reznikov")
    browser.element('[type="email"]').should(be.blank).type("test1@mail.ru")
    browser.element('#currentAddress').should(be.blank).type("Hello world")
    browser.element('[id="permanentAddress"]').should(be.blank).type(":)")
    browser.element('[id="submit"]').click()