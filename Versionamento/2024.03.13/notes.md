# Aula 13/03/2024

## Git e Github
 - Professor ensina a como fazer uma bio no github, usando o <a href="https://readme.so/pt" target="_blank">Readme.so</a>, com todas suas funcionalidades e facilidade de criação.
 - <a href="vectorlogo.zone">Vectorlogo</a> para buscar imagens logo e colocar na bio.
 - Comandos em linux

        ```
        cd Desktop -> Entra na pasta 'Desktop'

        cd Desktop/projeto/ -> Entra na pasta projeto, que está dentro de desktop

- Git ignore: faz com que dê comandos ao git para ele não adicionar arquivos específicos.
    ``` 
    .gitignore

    ```

- wind + V: Abre uma ferramenta em que possibilita ver a área de transferência, então consegue ter acesso a todas coisas copiadas.

- Token classic no github
    >- Settings > Developer Settings > Tokens > Token classic > Generate new token

- Comandos do Git

     ```
        git init -> Inicia o git na pasta atual

        git status -> Verifica se o repositório git teve modificações, caso tiver, indica a dar um git add para subir os arquivos para Stanging Area

        git add . -> Adiciona todos os arquivos untracked para a Stanging Area

        git add 'nome do arquivo' -> Leva apenas o arquivo específico para Stanging Area

        git remote remove origin -> Remove a origem para caso tenha um diretório já na máquina

        git remote add origin 'link do repositório' -> Linka o diretório da máquina com o repositório online no github

        git commit -m "mensagem que quer dar no commit" -> Commita o que foi feito, e adiciona uma frase objetiva com o que foi feito no commit (é obrigado ser específico a mensagem, para que não haja problemas depois em saber o que foi feito nesse commit)

        git push --set --upstream origin master -> Pega tudo feito e manda para o github, pede acesso ao github para fazer login também

    


        
    
