

var longestCommonPrefix = function(strs) {
    let x = strs[0];
    var z = 0;
    var array1 = "";
    const MIN = Math.min(...strs.map(({length}) => length));

    if (strs.length == 0){
        return "";
    }

    while(z < MIN){
        for (let y = strs.length - 1; y >= 0; y--){
            if ((strs[y].charAt(z) !== x.charAt(z))){
                if (array1 !== ""){
                    return array1;
                }
                return "";
            }
            else if (y === 0){
                array1 += x.charAt(z);
            }
        }
        z++;
    }
    return array1;
};

var char = longestCommonPrefix(["flure", "cat", 'dluff']);
console.log(char);

var chara = longestCommonPrefix(["fodo", "fo", "fooooo", "fool"]);
console.log(chara);

var charac = longestCommonPrefix(["dog", "racecar", "car"])
console.log(charac);

var cha = longestCommonPrefix([]);
console.log(cha);
