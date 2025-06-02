//js fucntion that takes a string and returns a string with the first letter of each word capitalized
function capitalizeFirstLetterOfEachWord(str) {
    return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}
