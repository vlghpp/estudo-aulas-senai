let funcionario = ["Ana", "Paudo", "Jaime", "Estrela"]

let salario = []

salario[0] = 1500.5
salario[1] = 2300.87
salario[2] = 4200.18
salario[3] = 3350.14

let nomeFuncionario = ""
let maiorSalario = 0
for(let i = 0; i < salario.length; i++){
    if(salario[i] > maiorSalario){
        maiorSalario = salario[i]
        nomeFuncionario = funcionario[i]
    }
}

console.log(nomeFuncionario)
console.log(maiorSalario)       