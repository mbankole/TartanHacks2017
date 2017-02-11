var count = 3;
function removebutton(){
    var elem = document.getElementById('button');
    elem.parentNode.removeChild(elem);
}
function addrow(){
    row = `<div class="row"><div class="inputfield col s12 l7"><input id="building`;
    row += count;
    row += `" type="text" class="validate" name=building`;
    row += count;
    row += `><label for="building`;
    row += count;
    row += `">Building</label></div><div class="inputfield col s12 l4"><input id="room`;
    row += count;
    row += `" type="text" class="validate" name=room`;
    row += count;
    row += `><label for="room`;
    row += count;
    row += `">Room</label></div><div id="button"><a onclick="removebutton();addrow()" class="btn-floating btn-large waves-effect waves-light red"><i class="material-icons">add</i></a></div></div>`;
    $("#newrows").append (row);
    count++;
    console.log(row);
}