// Calculate which two numbers in an array sum to the target, if they exist
// Brute force method
var twoSum = function(nums, target) {
    var numbers = new Array();
    for (var i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            if (nums[i] + nums[j] == target){
                numbers.push(i);
                numbers.push(j);
                return numbers;
            }
        }
    }
    if (i == nums.length){
        console.log("No solution found");
    }
};

console.log(twoSum([2,3,4,5], 12));

// Key-value method
var TwoSumTwo = (nums, target) => {
    let mapper = {}; //Creates object containing key-value pairs; typical Javascript object
    // Key will be the value to search for; Value will be index
    for (var i = 0; i < nums.length; i++){
        const keyValue = target - nums[i];

        if (keyValue in mapper){
            return [mapper[keyValue], i];
        }
        else {
            mapper[nums[i]] = i;
        }
    }
    // Case that nothing was found
    if (i == nums.length){
        console.log("Nothing found");
    }
 
}

console.log(TwoSumTwo([5, 5, 5, 9], 10));