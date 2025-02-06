from selene import browser, be, have

def test_search_1(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))
    #browser.element('html').should(have.text('About this page'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))