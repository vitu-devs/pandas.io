# install venv 

<h1> Crie um Venv <h1>
<p> !python -m venv .venv</p>

<strong> iniciar o venv </strong>

<p> .venv\Scripts\activate.bat </p>

<strong> intall pandas </strong>

---

# VIEWS 

Criei algumas views para melhorar a minha visualização, por exemplo a 

```
df = df.sort_values("id", ascending=True)
```



# Limpeza de Dados

1. Regra de Negocio para Nulos

    1.1 A coluina "License" ele já é nula por is só nisso acabei só dando filna e transformando e nada "".
    1.2 A "host_identity_verified" para verificar se tem confirmado o alocamento devido a isso o que for nulo é unconfirmed.


2. Coluna Price
    2.1
    Primeiro fazemos a remoção do $ que consta em todos as linhas, melhor forma de ser realizado isso seria utiliza código abaixo:

    ```
    df['price'] = df['price'].str.replace('$','')
    df['price'] = df['price'].str.replace(',','.')
    ```

    2.2
    Após a retirada fazemos ele se transformar num número flutuante com o seguinte código

    ```
    df["price"] = df["price"].astype(float)
    ```

    2.3
    Conseguimos puxar a mediana dos valores com o seguinte código

    ```
    df['price'].mean()
    ```

# TRANSFORMANDO EM EXCEL PARA VISUALIZAÇÃO

df.to_excel("dataframe_incompleto.xlsx", index=False)