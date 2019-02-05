import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
 
my_sender=''        # 发件人邮箱账号
my_passowrld = ''   # 发件人邮箱密码
to_user=''          # 收件人邮箱账号，我这边发送给自己
SMTP_server = ''    # SMTP服务器

# 图片路径
image_path = r''

def send(img_path,sender = my_sender , receivers = to_user):
    message =  MIMEMultipart()
    subject = '终于能发图片了'
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')  
    message.attach(content)

    with open(img_path, "rb") as f:
        img_data = f.read()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', '<image1>')
    message.attach(img)

    server=smtplib.SMTP_SSL(SMTP_server)                    # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender,my_passowrld)                       # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender,receivers,message.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()
    print ("邮件发送成功")
        


if __name__ == "__main__":
    send(image_path)
