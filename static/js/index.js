$('#start-color').on('change input', () => {
  printValues();
  updateImage();
});

$('#end-color').on('change input', () => {
  printValues();
  updateImage();
});

$('#emoji').on('change input', () => {
  printValues();
  updateImage();
});

$('#flavour').on('change input', () => {
  printValues();
  updateImage();
});

function printValues() {
  console.log('Start:', $('#start-color').val());
  console.log('End  :', $('#end-color').val());
  console.log('Emoji:', $('#emoji').val());
}

function updateImage() {
  let start = $('#start-color').val().replace('#', '');
  let end   = $('#end-color').val().replace('#', '');
  let emoji = $('#emoji').val();
  let vendor = $('#flavour').val();
  
  let new_src = `/image?start=${start}&end=${end}&emoji=${emoji}&vendor=${vendor}`;
  let new_href = `/${start}/${end}/${emoji}/${vendor}`;
  
  $('.image-result img').attr('src', new_src);
  $('.download-link a').attr('href', new_src);
  $('.share-link a').attr('href', new_href);
}


function convertToHex(rgbString) {
  let rbg = rgbString.split("(")[1].split(")")[0];
  let hex = rbg.split(',').map((x) => {
    x = parseInt(x).toString(16);      //Convert to a base16 string
    return (x.length==1) ? "0"+x : x;
  })
  return '#' + hex.join('')
}


$('.start-palette .color').click(function () {
  let color = $(this).css('background-color');
  let convd = convertToHex(color);
  $('#start-color').val(convd).change();
})

$('.end-palette .color').click(function () {
  let color = $(this).css('background-color');
  let convd = convertToHex(color);
  $('#end-color').val(convd).change();
})
