let array = [1,2,3,4,5]
// 5,4,3,2,1
for(let i = array.length - 1; i >= 0 ; i++){
    array.unshift(array[i])
}
console.log(array)