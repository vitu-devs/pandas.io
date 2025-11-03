# install venv 

<h1> Crie um Venv <h1>
<p> !python -m venv .venv</p>

<strong> iniciar o venv </strong>

<p> .venv\Scripts\activate.bat </p>

<strong> intall pandas </strong>

---

# Limpeza de Dados

1. Coluna Price
    1.1
    Primeiro fazemos a remoção do $ que consta em todos as linhas, melhor forma de ser realizado isso seria utiliza código abaixo:

    ```
    df['price'] = df['price'].str.replace('$','')
    df['price'] = df['price'].str.replace(',','.')
    ```

    1.2
    Após a retirada fazemos ele se transformar num número flutuante com o seguinte código

    ```
    df["price"] = df["price"].astype(float)
    ```
    
    1.3
    Conseguimos puxar a mediana dos valores com o seguinte código

    ```
    df['price'].mean()
    ```
