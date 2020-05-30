# -*- coding: utf-8 -*-

__author__ = "Sampson"

from Api_Auto_Test import *

class GetData(object):

    __doc__ = "数据库操作"

    def __init__(self, conf_section):
        self.log = log
        self.conf = conf
        self.cursor = None
        self.connect = None
        self.conf_section = conf_section

    def connect_database(self):
        connect = pymysql.connect(
            host = self.conf.get(self.conf_section, "host"),
            port = int(self.conf.get(self.conf_section, "port")),
            user = self.conf.get(self.conf_section, "username"),
            password = self.conf.get(self.conf_section, "password"),
            charset = self.conf.get(self.conf_section, "charset"),
            cursorclass = pymysql.cursors.DictCursor
        )
        self.connect = connect
        self.cursor = self.connect.cursor()

    def execute_sql(self, sql):
        try:
            self.log.debug("执行SQL: %s" % sql)
            self.cursor.execute(sql)
            self.log.debug("执行结果： success")
            self.connect.commit()
        except Exception as msg:
            self.log.error("执行结果：fail， %s" % msg)
            return False
        data = self.cursor.fetchall()
        if not data:
            return None
        return data

    def connect_close(self):
        if self.connect and self.cursor:
            self.cursor.close()
            self.connect.close()
            self.log.warning("关闭数据库连接：success")
            return True
        else:
            self.log.warning("数据连接已关闭")
            return True

    def check_db(self):
        try:
            self.execute_sql("SHOW DATABASES")
            self.connect_close()
            self.log.info("连接数据库成功")
            return True
        except Exception as msg:
            self.log.error("连接失败：%s" % msg)
            return False


class sendMail(object):

    __doc__ = "发送邮件"

    def __init__(self):
        self.log = log
        self.conf = conf
        self.username = conf.get("mail", "username")
        self.password = conf.get("mail", "password")
        self.msg_to = conf.get("mail", "recv")
        self.smtp = None

    def close(self):
        self.smtp.quit()

    def send_mail(self, msg, subject,
                  email_host="smtp.qq.com",
                  file=None,
                  ssl=False,
                  port=25,
                  ssl_port=465):
        """
        发送邮件
        :param msg: 内容
        :param subject: 主题
        :param file: 附件路径
        :param ssl: 是否安全链接，默认为普通
        :param email_host: smtp服务器地址，默认为163服务器
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465
        :return:
        """
        smtpserver = email_host
        sender = "AutoMail <{}>".format(self.username)
        msgRoot = MIMEMultipart()
        msgRoot["Subject"] = subject
        msgRoot["From"] = sender.strip('"')
        msgRoot["To"] = ",".join(self.msg_to)
        msgText = MIMEText("{0}".format(msg), "html", "utf-8")
        msgRoot.attach(msgText)
        i, j = 1, 1

        while True:
            # 处理附件的
            if file:
                file_name = os.path.split(file)[-1]
                try:
                    f = open(file, 'rb').read()
                except Exception as e:
                    raise Exception('附件打不开！！！！')
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
                self.smtp = smtplib.SMTP_SSL(email_host, port=ssl_port)
            else:
                self.smtp = smtplib.SMTP(email_host, port=port)

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

            # 发送邮件
            try:
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


class Request(object):

    def __init__(self, server):
        self.server = server
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
        }

    def weixin_login(self, code):
        """微信登录"""
        url = self.server + '/openapi/vip/user/login'
        data = dict(authCode=code, channel='W', loginType='MINI')
        resp = requests.post(url=url, headers=self.headers, data=json.dumps(data)).json()
        if resp["code"] != 0:
            return False
        token = resp.get('data', dict()).get('token')
        authorization = 'Bearer {}'.format(token)
        return authorization

    def app_login(self, mobile, password='87654321'):
        """APP登录"""
        url = self.server + '/openapi/vip/user/login'
        data = dict(channel='A', loginType='APP_PWD', phone=mobile, password=password, smsCode='')
        resp = requests.post(url=url, data=json.dumps(data), headers=self.headers).json()
        if resp["code"] != 0:
            return False
        token = resp.get('data', dict()).get('token')
        authorization = 'Bearer {}'.format(token)
        return authorization

    def admin_login(self, username='admin', password='a12345678'):
        """后台登录"""
        url = self.server + '/api/service-upms/admin/user/login'
        data = dict(password=password, username=username)
        resp = requests.post(url=url, data=json.dumps(data), headers=self.headers).json()
        if resp["code"] != 0:
            return False
        token = resp.get('data', dict()).get('token')
        authorization = 'Bearer {}'.format(token)
        return authorization

    def helper_login(self, shop_no=755001, shop_code=5559):
        """门店助手登录"""
        url = self.server + '/device/canceler/login?shop_no={}&shop_code={}'.format(shop_no, shop_code)
        resp = requests.post(url=url, headers=self.headers).json()
        if resp["code"] != 0:
            return False
        token = resp.get('result', dict()).get('token')
        authorization = 'Bearer {}'.format(token)
        return authorization

    def password_login(self, mobile, password='a12345678'):
        """密码登录"""
        url = self.server + '/api/phone_login'
        data = dict(login_type='2', phone=mobile, password=password)
        resp = requests.post(url=url, data=json.dumps(data), headers=self.headers).json()
        token = resp["token"]
        authorization = 'Bearer {}'.format(token)
        return authorization

if __name__ == '__main__':
    m = sendMail()
    m.send_mail(
        subject='python发送邮件附件测试',
        msg='测试发送邮件，qq发件，接收方一个是126邮箱，20190724',
        file=None,
        ssl=True,
    )
    m.close()