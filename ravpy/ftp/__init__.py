from ftplib import FTP

from ..config import FTP_SERVER_URL


class FTPClient:
    def __init__(self, host, user, passwd):
        self.ftp = FTP(host)
        print(self.ftp)
        print(self.ftp.welcome)
        print(self.ftp.connect(host="", port=21))
        print(self.ftp)
        self.ftp.set_pasv(True)
        self.ftp.login(user, passwd)

    def download(self, filename, path):
        print('Downloading')
        self.ftp.retrbinary('RETR ' + path, open(filename, 'wb').write)
        print("Downloaded")

    def upload(self, filename, path):
        self.ftp.storbinary('STOR ' + path, open(filename, 'rb'))

    def list_server_files(self):
        self.ftp.retrlines('LIST')

    def close(self):
        self.ftp.quit()


def get_client(username, password):
    return FTPClient(host=FTP_SERVER_URL, user=username, passwd=password)


def check_credentials(username, password):
    try:
        FTPClient(host=FTP_SERVER_URL, user=username, passwd=password)
        return True
    except Exception as e:
        print("Error:{}".format(str(e)))
        return False
