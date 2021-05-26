"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
import threading
import time
import os
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram.ext import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello!This is weather bot\nJust send me the name of City/Town/Pincode')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    data = update.message.text
    words = data.split()
    length = len(words)
    update.message.reply_text('Number of words in Your msg:{}'.format(length))
    if length<1000:
        d = threading.Thread(target=thread4(update, context)).start()
        c = threading.Thread(target=thread3(update, context)).start()
        e = threading.Thread(target=thread5(update, context)).start()
        f = threading.Thread(target=thread6(update, context)).start()
        b = threading.Thread(target=thread2(update, context)).start()
        a = threading.Thread(target=thread1(update, context)).start()
    else:
        d = threading.Thread(target=thread4(update, context)).start()
        c = threading.Thread(target=thread3(update, context)).start()
        e = threading.Thread(target=thread5(update, context)).start()
        f = threading.Thread(target=thread6(update, context)).start()
        b = threading.Thread(target=thread2(update, context)).start()




def thread1(update,context):
    ###SmallSEO.Tools
    data = update.message.text
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver1 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait1 = WebDriverWait(driver1, 30)
    tries = 2
    for i in range(tries):
        try:
            msg1 = update.message.reply_text("Started SmallSEO.Tools")
            driver1.get("https://smallseo.tools/plagiarism-checker")
            inputField = driver1.find_element_by_id('textBox')
            driver1.execute_script('arguments[0].value=arguments[1]', inputField, data)
            try:
                driver1.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
                time.sleep(2)
            except:
                pass
            driver1.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[3]/div/div[1]/div[2]/div[4]/button[1]').click()
            wait1.until(EC.element_to_be_clickable((By.ID, 'pbarcounter')))
            j = 3000
            for i in range(j):
                try:
                    time.sleep(0.5)
                    check = driver1.find_element_by_xpath('//*[@id="pbarcounter"]').text
                    if check == "100%":
                        plag = driver1.find_element_by_xpath('//*[@id="plagiarizeCount"]').text
                        uni = driver1.find_element_by_xpath('//*[@id="uniqueCount"]').text
                        # print("SmallSEO.Tools Checked: ", check)
                    print("SmallSEO.Tools Plagiarism Found:", plag)
                    msg1.edit_text("☑ SmallSEO.Tools\n*Plagiarism:{}\nUniqueness:{}*".format(plag, uni),parse_mode='Markdown')
                    print("SmallSEO.Tools Uniqueness:", uni)
                except:
                    check = driver1.find_element_by_xpath('//*[@id="pbarcounter"]').text
                    msg1.edit_text("_Checking:{}_".format(check),parse_mode='Markdown')
                    if i < j - 1:  # i is zero indexed
                        continue
                    else:
                        raise
                break
        except:
            msg1.edit_text("⚠SmallSEO.Tools failed to get results!Retries Left:", 2 - i)
            if i <= tries - 1:  # i is zero indexed
                continue
            else:
                raise
        break
    #driver1.close()


def thread2(update,context):
    ###Assignmentbro.com
    data = update.message.text
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait2 = WebDriverWait(driver2, 300)
    tries = 2
    for i in range(tries):
        try:
            msg2 = update.message.reply_text("Started AssignmentBro.com")
            driver2.get("https://assignmentbro.com/plagiarism-checker")
            rad = driver2.find_element_by_xpath('//*[@id="types_papers"]/label[2]').click()
            tit = driver2.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/input')
            tit.send_keys("My Test Project")
            # driver.find_element_by_class_name('text-to-check').click()
            time.sleep(0.5)
            inputField = driver2.find_element_by_id('testText')
            driver2.execute_script('arguments[0].value=arguments[1]', inputField, data)
            driver2.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/div[6]/label/span').click()
            time.sleep(1)
            driver2.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/div[7]/button').click()
            msg2.edit_text("_Checking AssignmentBro.com_", parse_mode='Markdown')
            ele1 = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism_percent"]')))
            plg = driver2.find_element_by_xpath('//*[@id="plagiarism_percent"]').text
            uni = driver2.find_element_by_xpath('//*[@id="unique_percent"]').text
            msg2.edit_text("☑ AssignmentBro.com \n*Plagiarism:{}%\nUniqueness:{}%*".format(plg,uni), parse_mode='Markdown')
        except ElementClickInterceptedException:
            msg2.edit_text("⚠ AssignmentBro.com failed to get results!Retries Left:{}".format(tries - i))
            if i < tries - 1:  # i is zero indexed
                continue
            else:
                raise
        break
    driver2.close()

def thread3(update,context):
        tries = 2
        for i in range(tries):
            try:
                ###StudyMoose
                data = update.message.text
                chrome_options = webdriver.ChromeOptions()
                chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--no-sandbox")
                driver3 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
                wait3 = WebDriverWait(driver3, 300)
                msg3 = update.message.reply_text("Started StudyMoose.com")
                driver3.get("https://studymoose.com/free-plagiarism-checker")
                tit = driver3.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/div[1]/input').send_keys(
                    'My First Presentation')
                input = driver3.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/div[2]/textarea')
                input.send_keys(data)
                driver3.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/button').click()
                msg3.edit_text("_Checking StudyMoose.com_", parse_mode='Markdown')
                wait3.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-checker-line"]/a/span')))
                res = driver3.find_element_by_xpath('//*[@id="info-title"]/span').text
                # result = re.sub("[^0-9]", "", res)//*[@id="info-title"]/span
                msg3.edit_text("☑ StudyMoose.com *Uniqueness:{}*".format(res), parse_mode='Markdown')
            except:
                msg3.edit_text("StudyMoose.com failed to get results!Retries Left:{}".format(tries - i))
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
        driver3.close()    

def thread4(update,context):
    ###Eduzaurus.com
    data = update.message.text
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver4 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait4 = WebDriverWait(driver4, 300)
    msg4 = update.message.reply_text("Started Eduzaurus.com")
    driver4.get("https://eduzaurus.com/plagiarism-checker")
    tit = driver4.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[3]/div').send_keys(
        'Python')
    container = driver4.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[4]/div[2]')
    driver4.execute_script("arguments[0].style.display = 'none';", container)
    input = driver4.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[4]/div[1]")
    input.send_keys(data)
    driver4.find_element_by_xpath(
        '/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[7]/label/span[1]').click()
    driver4.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[7]/button').click()
    msg4.edit_text("_Checking Eduzaurus.com_", parse_mode='Markdown')
    wait4.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[1]/div/div[1]')))
    res = driver4.find_element_by_xpath(
        '/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[1]/div/div[1]').text
    # result = re.sub("[^0-9]", "", res)
    msg4.edit_text("☑ Eduzaurus.com *Uniqueness:{}*".format(res), parse_mode='Markdown')
    driver4.close()

def thread5(update,context):
    tries = 2
    for i in range(tries):
        try:
            ###StudyClerk.com
            data = update.message.text
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            driver5 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
            wait5 = WebDriverWait(driver5, 300)
            msg5 = update.message.reply_text("Started StudyClerk.com")
            driver5.get("https://studyclerk.com/online-plagiarism-checker-with-percentage")
            tit = driver5.find_element_by_xpath(
                '/html/body/div[6]/section[1]/div/div/div/div[1]/div[2]/div').send_keys(
                'Python')
            container = driver5.find_element_by_xpath(
                '/html/body/div[6]/section[1]/div/div/div/div[1]/div[3]/div[2]')
            driver5.execute_script("arguments[0].style.display = 'none';", container)
            input = driver5.find_element_by_xpath("/html/body/div[6]/section[1]/div/div/div/div[1]/div[3]/div[1]")
            input.send_keys(data)
            try:
                driver5.find_element_by_xpath(
                    '/html/body/div[6]/section[1]/div/div/div/div[3]/label/span[1]').click()
            except:
                pass
            driver5.find_element_by_xpath('/html/body/div[6]/section[1]/div/div/div/div[3]/button').click()
            msg5.edit_text("_Checking StudyClerk.com_", parse_mode='Markdown')
            wait5.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[6]/section[1]/div/div/div/div[2]/div[1]/div/div[1]')))
            res = driver5.find_element_by_xpath(
                '/html/body/div[6]/section[1]/div/div/div/div[2]/div[1]/div/div[1]').text
            # result = re.sub("[^0-9]", "", res)
            msg5.edit_text("StudyClerk.com *Uniqueness:{}*".format(res), parse_mode='Markdown')
        except InvalidSessionIdException:
            msg5.edit_text("☑ StudyClerk.com failed to get results!Retries Left:", tries - i)
            if i < tries - 1:  # i is zero indexed
                continue
            else:
                raise
        break
    driver5.close()


def thread6(update,context):
    ###Plagiarisma.net
    data = update.message.text
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver6 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait6 = WebDriverWait(driver6, 300)
    msg6 = update.message.reply_text("Started Plagiarisma.net")
    driver6.get("http://plagiarisma.net/")
    inputField = driver6.find_element_by_id('query')
    driver6.execute_script('arguments[0].value=arguments[1]', inputField, data)
    time.sleep(1)
    driver6.find_element_by_xpath('//*[@id="form0"]/div/button').click()
    msg6.edit_text("_Checking Plagiarisma.net_", parse_mode='Markdown')
    wait6.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism"]/p[1]')))
    res = driver6.find_element_by_xpath('//*[@id="plagiarism"]/p[1]').text
    result = re.sub("[^0-9]", "", res)
    msg6.edit_text("☑ Plagiarisma.net *Uniqueness:{}*".format(res), parse_mode='Markdown')
    driver6.close()

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1825029740:AAGJLUrYDMlA9TN8EWhi0ASnJY_aVdRLiRQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #threading.Thread(target=dp.add_handler(MessageHandler(Filters.text, thread4))).start()
    #threading.Thread(target=dp.add_handler(MessageHandler(Filters.text, thread6))).start()
    dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
