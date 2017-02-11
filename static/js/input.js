function addrow(){
    var count = 3;
    row = `<div class="inputfield col s6 13">
                <input id="building`;
    row += count;
    row += `" type="text" class="validate" name=building`;
    row += count;
    row += `>
                <label for="building`;
    row += count;
    row += `">Building</label>
            </div>
            <div class=""inputfield col s6 13>
                <input id="room`;
    row += count;
    row += `" type="text" class="validate" name=room`;
    row += count;
    row += `>
                <label for="room`;
    row += count;
    row += `">Room</label>
            </div>
        </div>`;
    $("#newrows").append (row);
    count++;
    console.log(row);
}