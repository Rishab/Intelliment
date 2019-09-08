function getFiles() {
const testFolder = '../static/upload/';
const fs = require('fs');

fs.readdirSync(testFolder).forEach(file => {
  console.log(file);
});
}