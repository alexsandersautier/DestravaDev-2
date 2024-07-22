def calculate(size, heigth):
    heigth = heigth.replace(",", ".")
    size = size.replace(",", ".")
    result = float(size) / (float(heigth) * float(heigth))
    return f"{result:.2f}"