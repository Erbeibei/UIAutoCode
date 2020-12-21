class Utils:
    """加减乘除等运算方法"""
    def process_text(str):
        return float(str.split('$')[1])

    def process_text_of_paypal(str):
        return float(str[1:99][:-3])

    def addition(A, B):
        return Utils.process_text(A) + Utils.process_text(B)

    def subtraction(A, B):

        return Utils.process_text(A) - Utils.process_text(B)

    def multiplication(A, B):
        return Utils.process_text(A) * Utils.process_text(B)

    def division(A, B):
        return Utils.process_text(A) / Utils.process_text(B)


if __name__ == '__main__':
    c = Utils.process_text('US $14.99')
    print(c)
    d = Utils.addition("US $14.99", "US $14.99")
    print(d)