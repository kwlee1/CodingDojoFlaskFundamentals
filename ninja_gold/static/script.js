console.log(rand)
console.log(build)

if(build != 'none'){
    if(rand>0){
        $("#act").append('<p class="win">Earned ' + rand + ' gold from the ' + build + '!</p>')
    }
    if(rand<0){
        $("#act").append('<p class="loss">Lost ' + (rand * -1) + ' gold from the ' + build + '... Ouch... </p>')
    }
    if(rand == 0){
        $("#act").append('<p>Broke even at the casino...</p>')
    }
}

// $('form').submit(function(){
//     return false; 
// })