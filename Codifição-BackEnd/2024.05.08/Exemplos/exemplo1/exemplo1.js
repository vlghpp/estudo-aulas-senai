let alunos = [[], [], []]

alunos[0][0] = "Henrique"
alunos[0][1] = "19"
alunos[1][0] = "Frábio"
alunos[1][1] = "22"
alunos[2][0] = "Frábio"
alunos[2][1] = "44"


//JEITO MAIS DIFICIL, USANDO FOR ANINHADO

// for(let i = 0; i < alunos.length; i++){
//     for(let j = 0; j < alunos[i].length; j++){
//         console.log(alunos[i][j]);
//     }
// }

// //USANDO JEITO MÉDIO, USANDO O FOR IN PARA RETORNAR O INDICE DO ELEMENTO DA VEZ E PRINTA-LO
// for(let elemento in alunos){
//     console.log(alunos[elemento].toString()); //toString() para transformar um array em String 
// }

// // USANDO O JEITO MAIS FÁCIL, USANDO O FOR OF PARA RETORNAR O VALOR DO ELEMENTO JÁ

// for(let elemento of alunos){
//     console.log(elemento);
// }

// NO EXEMPLO2.js TEM A FORMA PARA FAZER COM BOAS PRATICAS