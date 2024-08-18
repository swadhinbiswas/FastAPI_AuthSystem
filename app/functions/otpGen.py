import random
import string


class OtpClass:

    def degitOtp():
        otp = ''.join(random.choices(string.digits, k=6))
        return otp
  
    def stringOtp():
        otp = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return otp
    