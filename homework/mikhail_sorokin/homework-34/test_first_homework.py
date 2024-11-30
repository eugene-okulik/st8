"""
 Мне нужно видео последние опересматривать я чет вообще не врубаюсь как использовать хэдлес в плейврайте на
 поздних примерах у тебя по умолчанию браузер работает в хедлес режиме всегда, а как сделать не хэдлес не указывая
  прямо как ранее было я хз, и чат jpt тоже мне в этом плане помочь не смог. Буду в отпуске сидеть разбираться
"""

from playwright.sync_api import Page, BrowserContext


def test_wait_for_color_change(context: BrowserContext):
    page: Page = context.new_page()
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator("#colorChange")
    button.wait_for(state="attached")
    page.wait_for_function(
        """
        document.querySelector('#colorChange').style.color === 'rgb(220, 53, 69)' ||
        window.getComputedStyle(document.querySelector('#colorChange')).color === 'rgb(220, 53, 69)'
        """
    )
    button.click()
    page.close()
