let alunos = []
let notas = []

let notasAcima5 = 0;
let contadorNotasAcima5 = 0
for(let c = 0; c < 5; c++){
    let nomeAluno = prompt("Digite o nome do aluno " + c)
    let notaAluno = Number(prompt("Digite a nota do aluno " + c))

    if(notaAluno > 5){
        notasAcima5 += notaAluno
        contadorNotasAcima5++
    }
}

let media = notasAcima5 / contadorNotasAcima5

alert(`A média das notas acima de 5 é: ${media}`)