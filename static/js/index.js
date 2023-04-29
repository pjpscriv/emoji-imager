 $('#start-color').on('input', () => {
   printValues()
 });

 $('#end-color').on('input', () => {
   printValues()
 });

 $('#emoji').on('input', () => {
   printValues()
 });

function printValues() {
  console.log('Start:', $('#start-color').val());
  console.log('End  :', $('#end-color').val());
  console.log('Emoji:', $('#emoji').val());
}