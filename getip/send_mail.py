import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

host,user,password,fromMail = "smtp.163.com", "thinkdna@163.com", "aaa123", "thinkdna@163.com"
mailto = "543357597@qq.com"

def sendMail(mailto,subject,body,format='plain'):
    if isinstance(body,unicode):
        body = str(body)

    me= ("%s<"+fromMail+">") % (Header(fromMail,'utf-8'),)
    msg = MIMEText(body,format,'utf-8')
    if not isinstance(subject,unicode):
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = mailto
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    try:
        s = smtplib.SMTP()
        s.connect(host)
        s.login(user,password)
        s.sendmail(me, mailto, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    subject = "Latest HULK IP"
    body = ""
    for line in open(sys.argv[1]):
        body += line
    for line in open(sys.argv[2]):
        body += line.strip()

    sendMail(mailto, subject, body)

# End script
