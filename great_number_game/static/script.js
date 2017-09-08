if(myhint == "low"){
    $('#wrong').html('<div id="too">TOO LOW!</div>')
}
if(myhint == "high"){
    $('#wrong').html('<div id="too">TOO HIGH!</div>')
}
if(myhint == "yes"){
    $('#wrong').html("<div id='correct'>"+mynum+" was the number!<br><form id='toreset' action='/reset'><button>Play again!</button></form></div>")
}
if(myhint == 'none'){
    $('#wrong').html('')
}