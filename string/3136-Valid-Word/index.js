var isValid = function(word) {
    if(word.length < 3) return false;
    
    if(!/^[0-9a-zA-Z]+$/.test(word)) return false;
    if(!/[aeiou]/i.test(word)) return false;
    if(!/[bcdfghjklmnpqrstvwxyz]/i.test(word)) return false;
    
    return true;
};