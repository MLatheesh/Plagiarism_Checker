from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging
import os
from telegram.ext import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello!This is a Plagiarism Detector BOT\n'
                              'Copy Text in your Document and Paste it here!\n'
                              'The BOT will check in various plagiarism sites and gives yoy the Results\n'
                              'The sites are\n'
                              '\t1.  Eduzaurus.com\n'
                              '\t2. studymoose.com min 500,max 20000 words\n'
                              '\t3. studyclerk.com\n'
                              '\t4. assignmentbro.com\n'
                              '\t5. plagiarisma.net max 2000chars\n'
                              '\t6. smallseo.tools max 1000 words'
                              'NOTE:\n'
                              '1.Some Times due to site error,The above Testcases will be failed\n'
                              '2.The webpage loading and checking for plagiarism takes time(Max of 5min to complete all Testcases)\n'
                              'Made By: @LatheeshMangeri')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Send a Dummy text, Let the BOT Surprise you!')


def echo(update, context):

    """Echo the user message."""
    # Run Time to measure ExecutionTime
    begin = time.time()
    data = update.message.text
    words = data.split()
    update.message.reply_text('Number of words in text file :{}'.format(len(words)))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait = WebDriverWait(driver, 300)

    ###1.Eduzaurus.com

    try:
        msg1=update.message.reply_text("Started Eduzaurus.com")
        driver.get("https://eduzaurus.com/plagiarism-checker")
        tit = driver.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[3]/div').send_keys(
            'Python')
        container = driver.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[4]/div[2]')
        driver.execute_script("arguments[0].style.display = 'none';", container)
        input = driver.find_element_by_xpath("/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[4]/div[1]")
        input.send_keys(data)
        driver.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[7]/label/span[1]').click()
        driver.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[7]/button').click()
        msg1.edit_text("Checking Eduzaurus.com")
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[1]/div/div[1]')))
        res = driver.find_element_by_xpath('/html/body/div[5]/section[1]/div/div/div/div[2]/div/div[1]/div/div[1]').text
        # result = re.sub("[^0-9]", "", res)
        msg1.edit_text("✅ Eduzaurus.com Uniqueness:*{}*".format(res), parse_mode='Markdown')
    except:
        msg1.edit_text("🛑 Eduzaurus.com Failed")
        pass

    ###2.StudyMoose

    try:
        tries = 3
        for i in range(tries):
            try:
                msg2=update.message.reply_text("Started StudyMoose.com")
                driver.get("https://studymoose.com/free-plagiarism-checker")
                tit = driver.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/div[1]/input').send_keys(
                    'My First Presentation')
                input = driver.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/div[2]/textarea')
                input.send_keys(data)
                driver.find_element_by_xpath('//*[@id="plagiarismCheckerForm"]/button').click()
                msg2.edit_text("Checking StudyMoose.com")
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="info-checker-line"]/a/span')))
                res = driver.find_element_by_xpath('//*[@id="info-title"]/span').text
                # result = re.sub("[^0-9]", "", res)//*[@id="info-title"]/span
                msg2.edit_text("✅ StudyMoose.com Uniqueness:*{}*".format(res), parse_mode='Markdown')
            except:
                msg2.edit_text("⚠ StudyMoose.com failed to get results!Retries Left:{}".format(tries - i))
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
    except:
        msg2.edit_text("🛑 Studymoose.com Failed")
        pass

    ###3.StudyClerk.com

    try:
        tries = 3
        for i in range(tries):
            try:
                ###StudyClerk.com
                msg3=update.message.reply_text("Started StudyClerk.com")
                driver.get("https://studyclerk.com/online-plagiarism-checker-with-percentage")
                tit = driver.find_element_by_xpath(
                    '/html/body/div[6]/section[1]/div/div/div/div[1]/div[2]/div').send_keys('Python')
                container = driver.find_element_by_xpath(
                    '/html/body/div[6]/section[1]/div/div/div/div[1]/div[3]/div[2]')
                driver.execute_script("arguments[0].style.display = 'none';", container)
                input = driver.find_element_by_xpath("/html/body/div[6]/section[1]/div/div/div/div[1]/div[3]/div[1]")
                input.send_keys(data)
                try:
                    driver.find_element_by_xpath(
                        '/html/body/div[6]/section[1]/div/div/div/div[3]/label/span[1]').click()
                except:
                    pass
                driver.find_element_by_xpath('/html/body/div[6]/section[1]/div/div/div/div[3]/button').click()
                msg3.edit_text("Checking StudyClerk.com")
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[6]/section[1]/div/div/div/div[2]/div[1]/div/div[1]')))
                res = driver.find_element_by_xpath(
                    '/html/body/div[6]/section[1]/div/div/div/div[2]/div[1]/div/div[1]').text
                # result = re.sub("[^0-9]", "", res)
                msg3.edit_text("✅ StudyClerk.com Uniqueness:*{}*".format(res), parse_mode='Markdown')
            except:
                msg3.edit_text("⚠ StudyClerk.com failed to get results!Retries Left:{}".format(tries - i))
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
    except:
        msg3.edit_text("🛑 Studyclerk.com failed")
        pass

    ###4.Assignmentbro.com

    try:
        tries = 3
        for i in range(tries):
            try:
                msg4=update.message.reply_text("Started AssignmentBro.com")
                driver.get("https://assignmentbro.com/plagiarism-checker")
                rad = driver.find_element_by_xpath('//*[@id="types_papers"]/label[2]').click()
                tit = driver.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/input')
                tit.send_keys("My Test Project")
                # driver.find_element_by_class_name('text-to-check').click()
                time.sleep(0.5)
                inputField = driver.find_element_by_id('testText')
                driver.execute_script('arguments[0].value=arguments[1]', inputField, data)
                driver.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/div[6]/label/span').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="plagiarism_checker_wrapper"]/div/div[7]/button').click()
                msg4.edit_text("Checking AssignmentBro.com")
                ele1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism_percent"]')))
                plg = driver.find_element_by_xpath('//*[@id="plagiarism_percent"]').text
                uni = driver.find_element_by_xpath('//*[@id="unique_percent"]').text
                msg4.edit_text("✅ AssignmentBro.com \nPlagiarism:*{}%*\nUniqueness:*{}%*".format(plg,uni), parse_mode='Markdown')
            except:
                msg4.edit_text("⚠ AssignmentBro.com failed to get results!Retries Left:{}".format(tries - i))
                if i < tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
    except:
        msg4.edit_text("🛑 Assignmentbro.com Failed")
        pass

    ###5.Plagiarisma.net

    try:
        msg5=update.message.reply_text("Started Plagiarisma.net")
        driver.get("http://plagiarisma.net/")
        inputField = driver.find_element_by_id('query')
        driver.execute_script('arguments[0].value=arguments[1]', inputField, data)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="form0"]/div/button').click()
        msg5.edit_text("Checking Plagiarisma.net")
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plagiarism"]/p[1]')))
        res = driver.find_element_by_xpath('//*[@id="plagiarism"]/p[1]').text
        # result = re.sub("[^0-9]", "", res)
        msg5.edit_text("✅ Plagiarisma.net Uniqueness:*{}*".format(res), parse_mode='Markdown')
    except:
        msg5.edit_text("🛑 Plagiarisma.net Failed")
        pass
        ###6.SmallSEO.Tools

        try:
            tries = 3
            for i in range(tries):
                try:
                    msg6 = update.message.reply_text("Started SmallSEO.Tools")
                    driver.get("https://smallseo.tools/plagiarism-checker")
                    inputField = driver.find_element_by_id('textBox')
                    driver.execute_script('arguments[0].value=arguments[1]', inputField, data)
                    try:
                        driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
                        time.sleep(2)
                    except:
                        pass
                    driver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div/div[3]/div/div[1]/div[2]/div[4]/button[1]').click()
                    wait.until(EC.element_to_be_clickable((By.ID, 'pbarcounter')))
                    j = 3000
                    for a in range(j):
                        try:
                            time.sleep(0.5)
                            check = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                            time.sleep(20)
                            check1 = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                            if check == check1:
                                plag = driver.find_element_by_xpath('//*[@id="plagiarizeCount"]').text
                                uni = driver.find_element_by_xpath('//*[@id="uniqueCount"]').text
                                msg6.edit_text("\rSmallSEO.Tools Checked:{}".format(check))
                                update.message.reply_text(
                                    "✅ SmallSEO.Tools \nPlagiarism Found:{}\nUniquesness:{}".format(plag, uni),
                                    parse_mode='Markdown')
                            # print("✅ SmallSEO.Tools Uniqueness:", uni)
                            else:
                                raise
                        except:
                            check = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                            msg6.edit_text("\rChecking: ", check, end="")
                            if a < j - 1:  # i is zero indexed
                                continue
                            else:
                                raise
                        break
                except:
                    msg6.edit_text("⚠ SmallSEO.Tools failed to get results!Retries Left:{}".format(tries - a))
                    if a <= tries - 1:  # i is zero indexed
                        continue
                    else:
                        raise
                break
        except:
            msg6.edit_text("🛑 SmallSEO.Tools Failed")
            pass
    ###6.SmallSEO.Tools

    try:
        tries = 3
        for i in range(tries):
            try:
                msg6 = update.message.reply_text("Started SmallSEO.Tools")
                driver.get("https://smallseo.tools/plagiarism-checker")
                inputField = driver.find_element_by_id('textBox')
                driver.execute_script('arguments[0].value=arguments[1]', inputField, data)
                try:
                    driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
                    time.sleep(2)
                except:
                    pass
                driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div[3]/div/div[1]/div[2]/div[4]/button[1]').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'pbarcounter')))
                j = 3000
                for a in range(j):
                    try:
                        time.sleep(0.5)
                        check = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                        time.sleep(20)
                        check1 = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                        if check == check1:
                            plag = driver.find_element_by_xpath('//*[@id="plagiarizeCount"]').text
                            uni = driver.find_element_by_xpath('//*[@id="uniqueCount"]').text
                            msg6.edit_text("\rSmallSEO.Tools Checked:{}".format(check))
                            update.message.reply_text(
                                "✅ SmallSEO.Tools \nPlagiarism Found:{}\nUniquesness:{}".format(plag, uni),
                                parse_mode='Markdown')
                        # print("✅ SmallSEO.Tools Uniqueness:", uni)
                        else:
                            raise
                    except:
                        check = driver.find_element_by_xpath('//*[@id="pbarcounter"]').text
                        msg6.edit_text("\rChecking: ", check, end="")
                        if a < j - 1:  # i is zero indexed
                            continue
                        else:
                            raise
                    break
            except:
                msg6.edit_text("⚠ SmallSEO.Tools failed to get results!Retries Left:{}".format(tries - a))
                if a <= tries - 1:  # i is zero indexed
                    continue
                else:
                    raise
            break
    except:
        msg6.edit_text("🛑 SmallSEO.Tools Failed")
        pass



    update.message.reply_text("Done!")
    # get End time
    end = time.time()
    # printing execution time
    print("Time of Execution is ", end - begin)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1825029740:AAHS30h2OELZ4OP29YxjtbkJY4Vdtdf73Cw", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
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



"""        
plagscan = driver.find_element_by_xpath('//*[@id="plag"]').text
try:
    ele = wait.until(EC.visibility_of((By.XPATH, '//*[@id="counter"]/span[1]')))
    print(ele)
    print(ele.text)

    if plagscan == '100%':
        plag = driver.find_element_by_xpath('//*[@id="counter"]/span[1]')
        print(plag)
except:
    print("\rChecking:", plagscan, end="")


if plagscan == '100%':
    ele = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="counter"]/span[1]')))
    print("plagiarismdetector.net:",ele.text)
#driver.find_element_by_xpath('//*[@id="page"]/div/div/div/section/div/div[1]/div[3]/div[1]/div[1]/span/span/span')
#driver.find_element(By.CLASS_NAME,"recaptcha-checkbox-border").click()
"""
