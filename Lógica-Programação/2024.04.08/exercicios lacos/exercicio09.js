for(let c = 0; c <= 100; c++){
    if(c % 3 == 0 && c % 5 !== 0){
        console.log("Fizz")
    }else if(c % 3 != 0 && c % 5 == 0){
        console.log("Buzz")
    }else if(c % 3 == 0 && c % 5 == 0){
        console.log("FizzBuzz")
    }else{
        console.log(c)
    }
    
    
}