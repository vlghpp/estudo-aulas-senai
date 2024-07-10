let array_altura = [1.9,2.1,1.7,1.75,11]
let moveis = ["mesa", "armario", "pia","cristaleira", "geladeira", "Cabideiro"]
let moveis_objetos = [{tipo: "mesa"},{tipo: "armario"},{tipo: "cristaleiro"},{tipo: "pia"}]

console.log("Meus movies: " + JSON.stringify(moveis_objetos.sort((a,b) => a.tipo - b.tipo)))



// console.log(moveis.sort())
// console.log(array_altura.sort((a,b) => a - b))
