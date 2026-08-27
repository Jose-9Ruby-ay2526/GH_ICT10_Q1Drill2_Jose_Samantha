from pyscript import display, document




def adding_number(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    sum = first_number + second_number

    display(
        f'The sum of {first_number} and {second_number} is {sum}',
        target='result'
    )






def subtracting_number(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    difference = first_number - second_number

    display(
        f'The difference of {first_number} and {second_number} is {difference}',
        target='result'
    )



def multiplying_number(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    product = first_number * second_number

    display(
        f'The product of {first_number} and {second_number} is {product}',
        target='result'
    )






def dividing_number(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    if second_number == 0:
        display(
            f'Division by zero is not allowed.',
            target='result'
        )






    else:
        quotient = first_number / second_number

        display(
            f'The quotient of {first_number} and {second_number} is {quotient}',
            target='result'
        )