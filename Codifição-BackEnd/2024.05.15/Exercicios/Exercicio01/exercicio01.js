function calculaAreaTerreno(largura, profundidade){
    let areaTotal = largura * profundidade
    return areaTotal
}

let resultadoAreaMansao = calculaAreaTerreno(100,100)
let resultadoAreaPadrao = calculaAreaTerreno(50,40)
let resultadoAreaSobrado = calculaAreaTerreno(30,40)
let resultadoAreaComercial = calculaAreaTerreno(40, 40)

console.log(resultadoAreaMansao + "m²")
console.log(resultadoAreaPadrao + "m²")
console.log(resultadoAreaSobrado + "m²")
console.log(resultadoAreaComercial + "m²")