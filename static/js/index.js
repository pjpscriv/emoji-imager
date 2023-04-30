 $('#start-color').on('input', () => {
   printValues();
   updateImage();
 });

 $('#end-color').on('input', () => {
   printValues();
   updateImage();
 });

 $('#emoji').on('input', () => {
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
  
  let new_src = `/image?start=${start}&end=${end}&emoji=${emoji}`;
  
  $('.image-result img').attr('src', new_src);
  $('.download-link a').attr('href', new_src);
}

$('.start-palette .color').on('click', () => {
  let color = $(this).css('background-color');
  $('#start-color').val(color);
})

$('.end-palette .color').on('click', () => {
  let color = $(this).css('background-color');
  $('#end-color').val(color);
})
