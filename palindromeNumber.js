//isPalindrome function without using strings;
var isPalindrome = function(x){
    // If string has characters other than $ , . 0-9
    if (/[^$,\.\d]/.test(x)){
        return false;
    }
    // all values
    else {
        var output = [];
        while (x){
            output.push(x % 10);
            x = Math.floor(x/10);
        }
        lowerBound = 0;
        upperBound = output.length;

        while (lowerBound < upperBound){
            if (output[lowerBound] === output[upperBound - 1]){
                lowerBound += 1;
                upperBound -= 1;
            }
            else {
                return false;
            }
        }
        return true;
    }
};
