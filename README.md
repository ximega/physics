# Physics

[Links](#anchor-links)
[How to install](#anchor-how-to-install)
[How to use](#anchor-how-to-use)
[Values](#anchor-values)

<a id = 'anchor-how-to-install'></a>
# How to install

#### Steps:
1. Open cmd or Git Bash
    1.1. (`Win + R` and write to opened window `cmd`)
    1.2. Open Git Bash
2. Open your project's repository
    by `cd [project path]`
3. Write:
    ```
    git clone https://github.com/ximega/physics
    ```

<a id = 'anchor-how-to-use'></a>
# How to use
Steps:
1. open file, where you want to use module
2. write:
    ```
    from physic.physics import *
    ```
3. use!
    ```
    result = Physics.method(args)

    print(result)
    ```

<a id = 'anchor-values'></a>
# Values
##### You can receive 2 results:

###### First: normal result with unit
For example:
    `print(Physics.density(10, 10))`
It gives:
    `1.0 кг/см^3`
###### Second: only value (int or float)
Needs for combine one or more methods

How it works:
    `Physics.method(args).toValue()`

For example:
    `print(Physics.density(10, 10))`
It gives:
    `1.0`

<a id = 'anchor-links'></a>
# Links

[GitHub](https://github.com/ximega/physics)