def ded():
    x = 10

    def papa():
        x = 20

        def sin():
            x = 30

            def malish():
                nonlocal x
                x = 40

            malish()
            print(x)

        sin()
        print(x)

    papa()
    print(x)


ded()
