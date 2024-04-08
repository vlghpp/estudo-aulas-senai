let contadorPares = 0;
let contadorImpares = 0;
for(let c = 1; c <= 100; c++){
    if(c % 2 == 0){
        contadorPares++;
    }else if(c % 2 == 1){
        contadorImpares++;
    }
}
console.log(`Tem ${contadorPares} pares e ${contadorImpares} impares`)