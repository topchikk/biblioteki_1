from selene import browser, be, have

def test_search_1(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id=react-layout]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_duckduckgo_click(open_browser):
    browser.element('[name=q]').clear().type('kjfhdjkhfjkhssовавлавоаылдаоы18').press_enter()
    browser.element('[id=react-layout]').should(have.text('результаты не найдены.'))

def test_duckduckgo_enter(open_browser):
    browser.element('[name=q]').clear().type(' ').press_enter()
    browser.element('[id=__next]').should(have.text('No search query text entered. Please try again.'))
