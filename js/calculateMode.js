exports.calculateMode = (inputArray) => {
    eltObject = {}
    for (let elt of inputArray) {
        if (elt in eltObject) {
            eltObject[elt] ++ 
        } else {
            eltObject[elt] = 1
        } }
    
    const values = Object.values(eltObject)
    const mode = Math.max(...values)

    const output = []
    for (let[k,v] of Object.entries(eltObject)) {
        if (v === mode) {
            output.push(k)
        }}
    
    return output.sort()
}
// console.log(exports.calculateMode([4.5, 0, 0]))
