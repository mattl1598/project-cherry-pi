
function clip_text(a_string){
    var input = document.createElement('input');
    input.id="__copyText__";
    input.value = a_string;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    var txt = input.value;
    input.remove();
    console.log("OK COPIED: '"+txt+"'");
}

function clip_key_64(length) {
	var url = 'http://larby.co.uk/bse64/' + length;
	console.log(url);
    fetch(url)
        .then(response => response.json())
		.then(data => {
			console.log(data);
			console.log(data.key);
			clip_text(data.key);
         });
}
