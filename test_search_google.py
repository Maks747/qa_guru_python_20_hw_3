from selene import browser, have

def test_search_google_positive():
    browser.open('https://google.ru')
    browser.element('[name="q"]').type('mts').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_search_google_negative():
    browser.open('https://google.ru')
    browser.element('[name="q"]').type('rtyhgfcvbnmjkl').press_enter()
    browser.element('html').should(have.text('По запросу rtyhgfcvbnmjkl ничего не найдено.'))