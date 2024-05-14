
var findWordsContaining = function(words, x) {
    arr =[]
    for(i=0;i<words.length;i++){
        for(j=0;j<words[i].length;j++){
            if(words[i][j] === x){
                arr.push(i)
                break
            }
        }
    }

    return arr
};