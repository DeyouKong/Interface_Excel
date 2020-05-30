# -*- coding: utf-8 -*-

# @File: sendMail
# @Author : "Sampson"
# @Detail :

from Api_Auto_Test import *

def get_new_file(file_path):
    lists = os.listdir(file_path)
    lists.sort(key=lambda fn: os.path.getmtime(file_path + '/' + fn))
    file_dir = os.path.join(file_path, lists[-1])
    # return file_dir
    return "/Users/deyoukong/Desktop/Imocc/Api_Auto_Test/TestFiles/TestData/auto_test_case.xlsx"

class sendMail(object):

    __doc__ = "发送邮件"

    def __init__(self):
        self.log = log
        self.smtpserver = conf.get("mail", "smtpserver")
        self.username = conf.get("mail", "username")
        self.password = conf.get("mail", "password")
        self.msg_to = conf.get("mail", "recv")
        self.smtp = None
        self.report_path = report_path

    def close(self):
        self.smtp.quit()

    def send_mail(self,
                  main_msg='<h1 style="color: red">自动化测试报告</h1>',
                  subject='python自动化测试报告',
                  file=0,
                  ssl=True,
                  port=25,
                  ssl_port=465):
        """
        发送邮件
        :param subject: 主题
        :param main_msg: 内容
        :param file: 是否发送附件
        :param ssl: 是否安全链接，默认为ssl
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465
        :return:
        """
        msgRoot = MIMEMultipart()
        msgRoot["Subject"] = subject
        msgRoot["From"] = self.username.strip('"')
        msgRoot["To"] = self.msg_to
        msgText = MIMEText("{0}".format(main_msg), "html", "utf-8")
        msgRoot.attach(msgText)
        i, j = 1, 1

        while True:
            # 处理附件
            if file:
                files = get_new_file(self.report_path)
                file_name = os.path.split(files)[-1]
                try:
                    with open(files, 'rb') as fp:
                        f = fp.read()
                except Exception as msg:
                    raise Exception('附件打不开：{}'.format(msg))
                else:
                    att = MIMEText(f, "base64", "utf-8")
                    att["Content-Type"] = 'application/octet-stream'
                    # base64.b64encode(file_name.encode()).decode()
                    new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                    # 这里是处理文件名为中文名的，必须这么写
                    att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                    msgRoot.attach(att)

            # 登录邮件服务
            if ssl:
                self.smtp = smtplib.SMTP_SSL(self.smtpserver, port=ssl_port)
            else:
                self.smtp = smtplib.SMTP(self.smtpserver, port=port)

            try:
                self.smtp.login(self.username, self.password)
                self.log.info("email login success!")
            except Exception as msg:
                self.log.error("[%s]: email login error: [%s]" % (i, msg))
                if  i < 3:
                    i += 1
                    continue
                else:
                    return 400

            try:
                # 发送邮件
                self.log.info("开始发送邮件，发送参数{}".format(msgRoot))
                self.smtp.sendmail(self.username, msgRoot['To'].split(','), msgRoot.as_string())
                self.log.debug("mail send success!")
            except Exception as msg:
                self.log.error("[%s]:email send error: [%s]" % (j, msg))
                if j < 3:
                    j += 1
                    continue
                else:
                    return 401
            break
        return 200


if __name__ == '__main__':
    m = sendMail()
    m.send_mail(file=1)
    m.close()