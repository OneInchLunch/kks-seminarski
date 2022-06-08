from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def test_setup_and_teardown():
    # TEST SETUP
    global driver 
    global a
    driver = webdriver.Firefox()
    a = ActionChains(driver)
    driver.implicitly_wait(5)
    driver.get('https://www.python.org')
    # TEST TEARDOWN
    yield
    driver.close()
    driver.quit()
    print('Test Completed')

# SUCCEDING TESTS
# TEST 1: Test social media links
def test_socials(test_setup_and_teardown):
    e = driver.find_element(By.CLASS_NAME, 'winkwink-nudgenudge')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Facebook').click()
    assert driver.current_url == 'https://www.facebook.com/pythonlang?fref=ts'
    driver.back()
    e = driver.find_element(By.CLASS_NAME, 'winkwink-nudgenudge')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Twitter').click()
    assert driver.current_url == 'https://twitter.com/ThePSF'
    driver.back()
    e = driver.find_element(By.CLASS_NAME, 'winkwink-nudgenudge')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Chat on IRC').click()
    assert driver.current_url == 'https://www.python.org/community/irc/'
    driver.back()

# TEST 2: Test navbar links
def test_navbar(test_setup_and_teardown):
    driver.find_element(By.CLASS_NAME, 'psf-meta').click()
    assert driver.title == 'Python Software Foundation'
    driver.find_element(By.CLASS_NAME, 'docs-meta').click()
    assert driver.title.split()[-1] == 'Documentation'
    driver.back()
    driver.find_element(By.CLASS_NAME, 'pypi-meta').click()
    assert driver.title.split()[0] == 'PyPI'
    driver.back()
    driver.find_element(By.CLASS_NAME, 'jobs-meta').click()
    assert driver.title.split()[1] == 'Job'
    driver.find_element(By.CLASS_NAME, 'shop-meta').click()
    assert driver.title.split()[0] == 'Community'
    driver.find_element(By.CLASS_NAME, 'python-meta').click()
    assert driver.title.split()[0] == 'Welcome'

# TEST 3: Test home navbar ::hover
def test_home_navbar_hover(test_setup_and_teardown):
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Applications').text
    assert text == 'Applications'
    e = driver.find_element(By.ID, 'downloads')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'All releases').text
    assert text == 'All releases'
    e = driver.find_element(By.ID, 'documentation')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Docs').text
    assert text == 'Docs'
    e = driver.find_element(By.ID, 'community')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Diversity').text
    assert text == 'Diversity'
    e = driver.find_element(By.ID, 'success-stories')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Arts').text
    assert text == 'Arts'
    e = driver.find_element(By.ID, 'news')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Python News').text
    assert text == 'Python News'
    e = driver.find_element(By.ID, 'events')
    a.move_to_element(e).perform()
    text = driver.find_element(By.LINK_TEXT, 'Python Events').text
    assert text == 'Python Events'

# TEST 4: Test home navbar clicks
def test_home_navbar_click(test_setup_and_teardown):
    driver.find_element(By.ID, 'about').click()
    assert driver.current_url == 'https://www.python.org/about/'
    driver.find_element(By.ID, 'downloads').click()
    assert driver.current_url == 'https://www.python.org/downloads/'
    driver.find_element(By.ID, 'documentation').click()
    assert driver.current_url == 'https://www.python.org/doc/'
    driver.find_element(By.ID, 'community').click()
    assert driver.current_url == 'https://www.python.org/community/'
    driver.find_element(By.ID, 'success-stories').click()
    assert driver.current_url == 'https://www.python.org/success-stories/'
    driver.find_element(By.ID, 'news').click()
    assert driver.current_url == 'https://www.python.org/blogs/'
    driver.find_element(By.ID, 'events').click()
    assert driver.current_url == 'https://www.python.org/events/'

# TEST 5: Test individual list items of home navbar element
def test_home_navbar_list_item(test_setup_and_teardown):
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Applications').click()
    assert driver.current_url == 'https://www.python.org/about/apps/'
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Quotes').click()
    assert driver.current_url == 'https://www.python.org/about/quotes/'
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Getting Started').click()
    assert driver.current_url == 'https://www.python.org/about/gettingstarted/'
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Help').click()
    assert driver.current_url == 'https://www.python.org/about/help/'
    e = driver.find_element(By.ID, 'about')
    a.move_to_element(e).perform()
    driver.find_element(By.LINK_TEXT, 'Python Brochure').click()
    assert driver.current_url == 'https://brochure.getpython.info/'


# FAILING TESTS
# TEST 6: Check if error is thrown on empty search
def test_empty_search(test_setup_and_teardown):
    driver.find_element(By.ID, 'submit').click()
    assert driver.find_element(By.ID, 'error-search')

# TEST 7: Check if partner images are clickable on the jobs page 
def test_partner_image_click(test_setup_and_teardown):
    driver.find_element(By.CLASS_NAME, 'jobs-meta').click()
    with pytest.raises(Exception):
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div/aside/div[3]/div/div[1]/img'))

# TEST 8: Check if buttons are aligned properly on psf page
def test_button_alignment(test_setup_and_teardown):
    driver.find_element(By.CLASS_NAME, 'psf-meta').click()
    btn = []
    btn.append(list(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[1]/p[2]').location.values())[1])
    btn.append(list(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/p[2]').location.values())[1])
    btn.append(list(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[3]/p[2]').location.values())[1])
    btn.append(list(driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[4]/p').location.values())[1])
    for it in btn:
        assert it == btn[0]

# TEST 9: Check if account sign/register in is available on the home page
def test_sign_in_available(test_setup_and_teardown):
    assert driver.find_element(By.CLASS_NAME, 'account-signin').click()

# TEST 10: Check if search allows special characters
def test_search_validation(test_setup_and_teardown):
    driver.find_element(By.ID, 'id-search-field').send_keys(')&^!)$(*@&#*(&@!#*(!":')
    driver.find_element(By.ID, 'submit').click()
    text = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/form/p/input[1]').get_attribute('value')
    assert not text == ')&^!)$(*@&#*(&@!#*(!":'